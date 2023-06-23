/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable @next/next/no-img-element */
import React, {  useState, useEffect, useCallback } from "react";
import { toast } from "react-toastify";
import dynamic from "next/dynamic";
import Card from "../card";
import SimpleInfo from "../simpleInfo";
import Button, { ButtonTypes } from "../button";

const MapWithNoSSR = dynamic(() => import("../../components/map"), {
    ssr: false,
});

interface Props {
    socket: any;
    setStage: React.Dispatch<React.SetStateAction<number>>;
    form: any;
}

const LiveScan: React.FC<Props> = ({ socket, setStage, form }) => {
    const [videoImage, setVideoImage] = useState<string | undefined>(undefined);
    const [battery, setBattery] = useState<string | undefined>(undefined);
    const [tvoc, setTvoc] = useState<string | undefined>(undefined);
    const [gps, setGps] = useState<{ x: number; y: number } | undefined>(undefined);
    const [eco2, setEco2] = useState<string | undefined>(undefined);

    const endScan = () => {
        toast.info("Varredura salva com sucesso!");
        socket.disconnect();
        setStage(0);
    };

    const handleSensorData = (
        valueGetter: string | undefined,
        valueSetter: React.Dispatch<React.SetStateAction<string | undefined>>
    ) => {
        return (value: string) => {
            if (valueGetter === value) return;
            valueSetter(value);
        };
    };

    const onCamera = handleSensorData(videoImage, setVideoImage);
    const onTvoc = handleSensorData(tvoc, setTvoc);
    const onBattery = handleSensorData(battery, setBattery);
    const onEco2 = handleSensorData(eco2, setEco2);

    const onGps = (value: string) => {
        const gpsData = JSON.parse(value);
        if (gps && gpsData.x != gps.x && gpsData.y != gps.y) {
            setGps(gpsData);
        }
    };

    useEffect(() => {
        socket.on("camera", onCamera);
        socket.on("tvoc", onTvoc);
        socket.on("battery", onBattery);
        socket.on("eco2", onEco2);
        socket.on("gps", onGps);

        return () => {
            socket.off("camera", onCamera);
            socket.off("tvoc", onTvoc);
            socket.off("battery", onBattery);
            socket.off("eco2", onEco2);
            socket.off("gps", onGps);
        };
    }, [socket]);

    const ImageInfo = useCallback(() => (
        <div className="bg-gray-300 rounded-lg">
            <img
                className="w-full h-[50vh] object-contain border flex justify-center items-center grow mb-8"
                src={`data:image/png;base64,${videoImage}`}
                alt="Vídeo da varredura"
            />

        </div>
    ), [videoImage]);

    const SensorsInfo = useCallback(() => (
        <div className="flex gap-4 justify-around">
            <SimpleInfo label="Bateria" value={battery ? `${parseInt(battery).toFixed(2)}%` : "..."} />
            <SimpleInfo label="Tvoc" value={tvoc ? `${tvoc} PPB` : "..."} />
            <SimpleInfo label="Eco2" value={eco2 ? `${eco2} PPM` : "..."} />
        </div>
    ), [battery, tvoc, eco2]);

    const Actions = useCallback(() => (
        <div className="flex justify-end">
            <Button buttonType={ButtonTypes.danger} onClick={endScan}>
                Parada de emergência
            </Button>
        </div>
    ), []);

    const LocationInfo = useCallback(() => (
        <div className="h-[40vh]">
            <MapWithNoSSR
                position={[form.location.coordinates.x, form.location.coordinates.y]}
            />
        </div>
    ), [form.location]);

    return (
        <div className="flex flex-col gap-4">
            <Card title="Vídeo" content={<ImageInfo />} classes={"min-h-[40vh] grow"} />
            <Card title="Sensores" content={<SensorsInfo />} />
            <Card title={`Localização: ${form.location.name}`} content={<LocationInfo />} />
            <Card title="Ações" content={<Actions />} />
        </div>
    );
};

export default LiveScan;
