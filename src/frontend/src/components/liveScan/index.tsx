import React from "react";
import SimpleInfo from "../simpleInfo";
import Button, { ButtonTypes } from "../button";

interface Props {
  buttonHandler: () => void;
}

const LiveScan: React.FC<Props> = ({buttonHandler}) => {
    return (
        <div className="flex flex-col p-4 h-full">
            <div className="w-full bg-slate-400 rounded-md grow mb-8">
                &nbsp;
            </div>
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
