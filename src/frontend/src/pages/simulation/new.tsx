import Wrapper from "@/components/wrapper";
import React, { useEffect } from "react";
import { toast } from "react-toastify";
import StartScan from "@/components/startScan";
import LiveScan from "@/components/liveScan";
import Loader from "@/components/loader";
import { socket } from "@/config/socket";

const NewSimulation: React.FC = (props) => {
    const [stage, setStage] = React.useState(0);
    const [loading, setLoading] = React.useState(false);

    function onConnect() {
        toast.success("Varredura iniciada com sucesso!");
        setStage(1);
        console.log("conectado")
        setLoading(false);
    }

    function onDisconnect() {
        setLoading(false);
    }

    function onStreaming(value: string) {
      console.log(value)
    }
    
    useEffect(() => {
        socket.on('connect', onConnect);
        socket.on('disconnect', onDisconnect);
        socket.on('foo', onStreaming);

        return () => {
            socket.off('connect', onConnect);
            socket.off('disconnect', onDisconnect);
            socket.off('foo', onStreaming);
            socket.disconnect()
          };
        
      }, []);

    const startScan = () => {
        setLoading(true)
        socket.connect()
       

        setTimeout(() => {
            setLoading(false)
        }, 2000)
    };

    const emergencyStop = () => {
        setLoading(true)
        toast.info("Varredura finalizada com sucesso!");
        setStage(0);
    };

    let content = null;
    switch (stage) {
        case 0:
            content = (
                <StartScan
                    buttonHandler={startScan}
                />
            );
            break;
        case 1:
            content = <LiveScan buttonHandler={emergencyStop} />;
            break;
    }

    return (
        <Wrapper title={"Nova varredura"}>
            <div className="bg-white rounded-xl shadow-2xl p-8 grow">
                {loading ? <Loader /> : content}
            </div>
        </Wrapper>
    );
};

export default NewSimulation;
