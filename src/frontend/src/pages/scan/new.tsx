import Wrapper from "@/components/wrapper";
import React, { useEffect } from "react";
import { toast } from "react-toastify";
import StartScan from "@/components/startScan";
import LiveScan from "@/components/liveScan";
import Loader from "@/components/loader";
import { withAuth } from "@/HOC/withAuth";
import { GetServerSidePropsContext, PreviewData } from "next";
import { ParsedUrlQuery } from "querystring";
import { io } from "socket.io-client";

const NewSimulation: React.FC = (props) => {
    const [stage, setStage] = React.useState(0);
    const [loading, setLoading] = React.useState(false);
    const [socket, setSocket] = React.useState<any>(null);
    const [videoImage, setVideoImage] = React.useState<string | undefined>(undefined);

    function onConnect() {
        toast.success("Varredura iniciada com sucesso!");
        setStage(1);
        console.log("Connected to websocket!");
        setLoading(false);
    }

    function onDisconnect() {
        console.log("Disconnected to websocket!");
        setLoading(false);
    }

    const startScan = () => {
        setLoading(true);
        socket.connect();
    };

    const emergencyStop = () => {
        toast.info("Varredura finalizada com sucesso!");
        socket.disconnect();
        setStage(0);
    };

    function onCamera(value: string) {
        if (videoImage == undefined) {
            console.log(value)
            setVideoImage(value);

        }
    }

    useEffect(() => {
        const socket = io(process.env.NEXT_PUBLIC_APP_URL!, { autoConnect: false, transports: ["websocket"] });
        setSocket(socket);

        socket.on("connect", onConnect);
        socket.on("disconnect", onDisconnect);
        socket.on("camera", onCamera);

        return () => {
            socket.off("connect", onConnect);
            socket.off("disconnect", onDisconnect);
            socket.off("camera", onCamera);
            socket.disconnect();
        };
    }, []);

    let content = null;
    switch (stage) {
        case 0:
            content = <StartScan buttonHandler={startScan} />;
            break;
        case 1:
            content = <LiveScan buttonHandler={emergencyStop} videoImage={videoImage}/>;
            break;
    }

    return (
        <Wrapper title={"Nova varredura"}>
            <div className="bg-white rounded-xl shadow-2xl p-8 grow">{loading ? <Loader /> : content}</div>
        </Wrapper>
    );
};
export const getServerSideProps = async (ctx: GetServerSidePropsContext<ParsedUrlQuery, PreviewData>) => {
    return await withAuth(ctx);
};

export default NewSimulation;
