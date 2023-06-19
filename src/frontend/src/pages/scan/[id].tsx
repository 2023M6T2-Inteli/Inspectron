import Image from "next/image";
import Wrapper from "@/components/wrapper";
import Card from "@/components/card";
import CardList from "@/components/cardList";
import { useEffect, useMemo, useState } from "react";
import { toast } from "react-toastify";
import { createServerSideAxiosInstance } from "@/config/axios";
import { withAuth } from "@/HOC/withAuth";
import { GetServerSidePropsContext, PreviewData } from "next";
import { ParsedUrlQuery } from "querystring";
import { Scan } from "../dashboard";
import dynamic from "next/dynamic";

interface Props {
    scan: Scan;
}

const ScanInfo = ({ scan }: Props) => {
    const MapWithNoSSR = dynamic(() => import("../../components/map"), {
        ssr: false,
    });

    const mean = (a: number, b: number) => {
        return ((a + b) / 2).toFixed(2);
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

    const renderRobotCard = () => (
        <Card simple alignLeft title={"Robô"} infos={["Nome: " + scan.robot.name, `Ip: ${scan.robot.ip}`]} />
    );

    const renderHumidityCard = () => (
        <Card
            simple
            title={"Humidade"}
            infos={[
                `Mínima: ${scan.humidity_min}`,
                `Média: ${mean(scan.humidity_min, scan.humidity_max)}`,
                `Máxima: ${scan.humidity_max}`,
            ]}
        />
    );

    const renderOxygenCard = () => (
        <Card
            simple
            title={"Oxigênio"}
            infos={[
                `Mínimo: ${scan.oxygen_min}`,
                `Médio: ${mean(scan.oxygen_min, scan.oxygen_max)}`,
                `Máximo: ${scan.oxygen_max}`,
            ]}
        />
    );

    const renderTemperatureCard = () => (
        <Card
            simple
            title={"Temperatura"}
            infos={[
                `Mínima: ${scan.temperature_min}`,
                `Média: ${mean(scan.temperature_min, scan.temperature_max)}`,
                `Máxima: ${scan.temperature_max}`,
            ]}
        />
    );

    return (
        <Wrapper title={scan.name}>
            <h3 className="text-2xl my-8">Informações detectadas pelos sensores</h3>
            <div className="grid grid-cols-3 gap-8">
                {renderHumidityCard()}
                {renderOxygenCard()}
                {renderTemperatureCard()}
            </div>
            <h3 className="text-2xl mb-8 mt-10">Informações gerais da varredura</h3>
            <div className="grid grid-cols-3 grid-rows-7 gap-8">
                {renderRobotCard()}
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
