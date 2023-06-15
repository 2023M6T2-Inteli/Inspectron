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
    const [form, setForm] = React.useState(undefined);

    const [socket, setSocket] = React.useState<any>(null);

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

    const startScan = (data: any) => {
        setLoading(true);
        socket.connect();
        console.log(data);
        setForm(data);
        socket.emit("new_scan_data", JSON.parse(data));
    };

    useEffect(() => {
        const socket = io(process.env.NEXT_PUBLIC_APP_URL!, { autoConnect: false, transports: ["websocket"] });
        setSocket(socket);

        socket.on("connect", onConnect);
        socket.on("disconnect", onDisconnect);

        return () => {
            socket.off("connect", onConnect);
            socket.off("disconnect", onDisconnect);

            socket.disconnect();
        };
    }, []);

    let content = null;
    switch (stage) {
        case 0:
            content = <StartScan buttonHandler={startScan} />;
            break;
        case 1:
            content = <LiveScan form={form} socket={socket} setStage={setStage} />;
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
