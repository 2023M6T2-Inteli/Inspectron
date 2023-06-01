import Wrapper from "@/components/wrapper";
import React, { useEffect } from "react";
import { toast } from "react-toastify";
import StartScan from "@/components/startScan";
import LiveScan from "@/components/liveScan";
import Loader from "@/components/loader";
import { socket } from "@/config/socket";
import { withAuth } from "@/HOC/withAuth";
import { GetServerSidePropsContext, PreviewData } from "next";
import { ParsedUrlQuery } from "querystring";

const NewSimulation: React.FC = (props) => {
    const [stage, setStage] = React.useState(0);
    const [loading, setLoading] = React.useState(false);

    useEffect(() => {
        function onConnect() {
            setLoading(false);
        }

        function onDisconnect() {
            setLoading(false);
        }

        function onStreaming(value: string) {
            console.log(value);
        }

        socket.on("connect", onConnect);
        socket.on("disconnect", onDisconnect);
        socket.on("foo", onStreaming);

        return () => {
            socket.off("connect", onConnect);
            socket.off("disconnect", onDisconnect);
            socket.off("foo", onStreaming);
        };
    }, []);

    const startScan = () => {
        setLoading(true);
        toast.success("Varredura iniciada com sucesso!");
        setStage(1);

        setTimeout(() => {
            setLoading(false);
        }, 2000);
    };

    const emergencyStop = () => {
        setLoading(true);
        toast.info("Varredura finalizada com sucesso!");
        setStage(0);

        setTimeout(() => {
            setLoading(false);
        }, 2000);
    };

    let content = null;
    switch (stage) {
        case 0:
            content = <StartScan buttonHandler={startScan} />;
            break;
        case 1:
            content = <LiveScan buttonHandler={emergencyStop} />;
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
