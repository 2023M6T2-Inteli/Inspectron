import React, { useEffect } from "react";
import SimpleInfo from "../simpleInfo";
import Button, { ButtonTypes } from "../button";

interface Props {
  buttonHandler: () => void;
  videoImage?: string
}

const LiveScan: React.FC<Props> = ({buttonHandler, videoImage}) => {
    // useEffect(() => {
    //     console.log(videoImage)
    // }, [videoImage])
    return (
        <div className="flex flex-col p-4 h-full">
            <h3 className="text-2xl mb-2">Vídeo</h3>
            <img className="w-full bg-slate-400 rounded-md grow mb-8" src={`data:image/png;base64,${videoImage}`} alt="Base64 Image"/>
            <div className="flex gap-4 justify-around">
                <SimpleInfo label="Bateria" value="80%" />
                <SimpleInfo label="Nível de oxigênio" value="89%" />
                <SimpleInfo label="Local" value="Sala #8958" />
                <Button buttonType={ButtonTypes.danger} onClick={buttonHandler}>
                    Parada de emergência
                </Button>
            </div>
        </div>
    );
};

export default LiveScan;
