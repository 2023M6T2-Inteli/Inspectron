/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable @next/next/no-img-element */
import React, { useEffect, useState } from "react";
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
    const [gps, setGps] = useState<string | undefined>(undefined);
    const [eco2, setEco2] = useState<string | undefined>(undefined);

    const emergencyStop = () => {
        toast.info("Varredura finalizada com sucesso!");
        socket.disconnect();
        setStage(0);
    };

    const handleSensorData = (valueSetter: React.Dispatch<React.SetStateAction<string | undefined>>) => {
        return (value: string) => {
            console.log(value)
            valueSetter(value);
        };
    };

    const onCamera = handleSensorData(setVideoImage);
    const onTvoc = handleSensorData(setTvoc);
    const onBattery = handleSensorData(setBattery);
    const onTemperature = handleSensorData(setTemperature);
    const onEco2 = handleSensorData(setEco2);
    const onGps = handleSensorData(setGps);

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
            <SimpleInfo label="Gps" value={gps ? gps : "..."} />
            <SimpleInfo label="Temperatura" value={temperature ? temperature : "..."} />
        </div>
    );

    const Actions = () => (
        <div className="flex justify-end">
            <Button buttonType={ButtonTypes.danger} onClick={emergencyStop}>
                Parada de emergência
            </Button>
        </div>
    );

    const LocationInfo = () => (
        <div className="h-[40vh]">
            <MapWithNoSSR position={[form.location.coordinates.x, form.location.coordinates.y]} />
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
