/* eslint-disable @next/next/no-img-element */
import React, { useEffect } from "react";
import SimpleInfo from "../simpleInfo";
import Button, { ButtonTypes } from "../button";
import { toast } from "react-toastify";

interface Props {
    socket: any;
    setStage: React.Dispatch<React.SetStateAction<number>>;
    form:any
}

const LiveScan: React.FC<Props> = ({ socket, setStage, form }) => {
    const [videoImage, setVideoImage] = React.useState<string | undefined>(undefined);
    const [battery, setBattery] = React.useState<string | undefined>(undefined);
    const [oxygen, setOxygen] = React.useState<string | undefined>(undefined);
    const [temperature, setTemperature] = React.useState<string | undefined>(undefined);

    const emergencyStop = () => {
        toast.info("Varredura finalizada com sucesso!");
        socket.disconnect();
        setStage(0);
    };

    const onCamera = (value: string) => {
        setVideoImage(value);
    };

    const onOxygen = (value: string) => {
        setOxygen(value);
    };

    const onBattery = (value: string) => {
        setBattery(value);
    };

    const onTemperature = (value: string) => {
        setTemperature(value);
    }

    useEffect(() => {
        socket.on("camera", onCamera);
        socket.on("oxygen", onOxygen);
        socket.on("battery", onBattery);
        socket.on("temperature", onTemperature);

        return () => {
            socket.off("camera", onCamera);
            socket.off("oxygen", onOxygen);
            socket.off("battery", onBattery);
            socket.off("temperature", onTemperature);
        };
    }, []);

    return (
        <div className="flex flex-col p-4 h-full">
            <h3 className="text-2xl mb-2">Vídeo</h3>
            <img
                className="w-full bg-slate-400 rounded-md grow mb-8"
                src={`data:image/png;base64,${videoImage}`}
                alt="Base64 Image"
            />
            <div className="flex gap-4 justify-around">
                <SimpleInfo label="Bateria" value={`${battery}%`} />
                <SimpleInfo label="Oxigênio" value={`${oxygen}%`} />
                <SimpleInfo label="Local" value={form.location.label} />
                <SimpleInfo label="Temperatura" value={temperature ? temperature : "..."} />
                <Button buttonType={ButtonTypes.danger} onClick={emergencyStop}>
                    Parada de emergência
                </Button>
            </div>
        </div>
    );
};

export default LiveScan;
