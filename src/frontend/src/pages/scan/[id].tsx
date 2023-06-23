import { useEffect, useState } from "react";
import Wrapper from "@/components/wrapper";
import Card from "@/components/card";
import { createServerSideAxiosInstance } from "@/config/axios";
import { withAuth } from "@/HOC/withAuth";
import { GetServerSidePropsContext, PreviewData } from "next";
import { ParsedUrlQuery } from "querystring";
import { Scan } from "../dashboard";
import dynamic from "next/dynamic";
import Moment from "react-moment";
import { createClient } from "@supabase/supabase-js";

const supabase = createClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL as string,
    process.env.NEXT_PUBLIC_SUPABASE_KEY as string
);

interface Props {
    scan: Scan;
}

const ScanInfo = ({ scan }: Props) => {
    const [videoUrl, setVideoUrl] = useState<string>("");

    const getVideoUrl = async () => {
        const { data } = await supabase.storage.from("Videos").getPublicUrl(scan.video_filename);
        setVideoUrl(data.publicUrl)
    };

    useEffect(() => {
        getVideoUrl()
    }, []);

    const MapWithNoSSR = dynamic(() => import("../../components/map"), {
        ssr: false,
    });

    const mean = (a: number, b: number) => {
        // create e mean of two numbers but checking if they exist
        if (!a && !b) return "não coletado";
        if (!a) return b.toFixed(2);
        if (!b) return a.toFixed(2);

        return ((a + b) / 2).toFixed(2);
    };

    const sensorValue = (value: number | undefined) => {
        if (!value) return "não coletado";
        return value;
    };

    const renderLocationCard = () => (
        <Card
            simple
            alignLeft
            title={`Localização: ${scan.location.name}`}
            content={
                <div className="h-[60vh]">
                    <MapWithNoSSR position={[scan.location.coordinates.x, scan.location.coordinates.y]} />
                </div>
            }
            rows="row-span-5"
            columns="col-span-full"
        />
    );

    const renderVideoCard = () => (
        <Card
            simple
            alignLeft
            title={`Vídeo`}
            content={
                    <div className="flex justify-center"><video controls> <source src={videoUrl ? videoUrl : ""}  type="video/mp4" /> </video></div>
            }
            rows="row-span-5"
            columns="col-span-full"
        />
    );

    const renderRobotCard = () => (
        <Card simple alignLeft title={"Robô"} infos={["Nome: " + scan.robot.name, `Ip: ${scan.robot.ip}`]} />
    );

    const renderMoment = (label: string, format: string) => (
        <div className="flex items-center gap-2">
            <span>{label}:</span>
            <Moment format={format}>{scan.created_at.$date}</Moment>
        </div>
    );

    const renderDateTimeCard = () => (
        <Card
            simple
            alignLeft
            title={"Data e hora"}
            infos={[renderMoment("Data", "DD/MM/YYYY"), renderMoment("Hora", "HH:mm")]}
        />
    );

    const renderEco2Card = () => (
        <Card
            simple
            title={"Dióxido de carbono"}
            infos={[
                `Mínimo: ${sensorValue(scan.eco2_min)}`,
                `Média: ${mean(scan.eco2_min, scan.eco2_max)}`,
                `Máximo: ${sensorValue(scan.eco2_max)}`,
            ]}
        />
    );

    const renderOxygenCard = () => (
        <Card
            simple
            title={"Oxigênio"}
            infos={[
                `Mínimo: ${sensorValue(scan.tvoc_min)}`,
                `Médio: ${mean(scan.tvoc_min, scan.tvoc_max)}`,
                `Máximo: ${sensorValue(scan.tvoc_max)}`,
            ]}
        />
    );

    return (
        <Wrapper title={scan.name}>
            <h3 className="text-2xl my-8">Informações detectadas pelos sensores</h3>
            <div className="grid grid-cols-3 gap-8">
                {renderEco2Card()}
                {renderOxygenCard()}
            </div>
            <h3 className="text-2xl mb-8 mt-10">Informações gerais da varredura</h3>
            <div className="grid grid-cols-3 grid-rows-7 gap-8">
                {renderRobotCard()}
                {renderDateTimeCard()}
                {renderVideoCard()}
                {renderLocationCard()}
            </div>
        </Wrapper>
    );
};

export const getServerSideProps = async (ctx: GetServerSidePropsContext<ParsedUrlQuery, PreviewData>) => {
    return await withAuth(ctx, async () => {
        const axios = await createServerSideAxiosInstance(ctx);
        const { data: scan } = await axios.get("/scans/" + ctx.query.id);

        return {
            props: { scan },
        };
    });
};

export default ScanInfo;
