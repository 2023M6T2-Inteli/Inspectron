/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable @next/next/no-img-element */
import React, {  useState, useEffect } from "react";
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
    const [temperature, setTemperature] = useState<string | undefined>(undefined);
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
    const onTemperature = handleSensorData(temperature, setTemperature);
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
        socket.on("temperature", onTemperature);
        socket.on("eco2", onEco2);
        socket.on("gps", onGps);

        return () => {
            socket.off("camera", onCamera);
            socket.off("tvoc", onTvoc);
            socket.off("battery", onBattery);
            socket.off("temperature", onTemperature);
            socket.off("eco2", onEco2);
            socket.off("gps", onGps);
        };
    }, [socket]);

    const ImageInfo = () => (
        <img
            className="w-full border-slate-700 border flex justify-center items-center rounded-md grow mb-8"
            src={`data:image/png;base64,${videoImage}`}
            alt="Vídeo da varredura"
        />
    );

    const SensorsInfo = () => (
        <div className="flex gap-4 justify-around">
            <SimpleInfo label="Bateria" value={battery ? `${battery}%` : "..."} />
            <SimpleInfo label="Tvoc" value={tvoc ? `${tvoc}%` : "..."} />
            <SimpleInfo label="Eco2" value={eco2 ? `${eco2}%` : "..."} />
            <SimpleInfo label="Temperatura" value={temperature ? temperature : "..."} />
        </div>
    );

    const Actions = () => (
        <div className="flex justify-end">
            <Button buttonType={ButtonTypes.danger} onClick={endScan}>
                Parada de emergência
            </Button>
        </div>
    );

    const LocationInfo = () => (
        <div className="h-[40vh]">
            <MapWithNoSSR
                position={[gps ? gps.x : form.location.coordinates.x, gps ? gps.y : form.location.coordinates.y]}
            />
        </div>
    );

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
