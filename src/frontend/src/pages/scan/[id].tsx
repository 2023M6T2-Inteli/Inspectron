import Image from "next/image";
import Wrapper from "@/components/wrapper";
import Card from "@/components/card";
import CardList from "@/components/cardList";
import { useEffect, useMemo, useState } from "react";
import { toast } from "react-toastify";
import { createServerSideAxiosInstance } from "@/config/axios";
import { Scan } from "../dashboard";
import { withAuth } from "@/HOC/withAuth";
import { GetServerSidePropsContext, PreviewData } from "next";
import { ParsedUrlQuery } from "querystring";

interface Props {
    scan: Scan;
}

const Scan = ({scan}: Props) => {

    const mean = (a: number, b: number) => {
        return ((a + b) / 2).toFixed(2);
    };

    return (
        <Wrapper title={scan.name}>
            <h3 className="text-2xl mb-8 mt-10">Informações gerais</h3>
            <div className="grid grid-cols-3 gap-8">
                <Card
                    simple
                    title={"Localização"}
                    infos={[
                        "Nome: " + scan.location.name,
                        `Latitude: ${scan.location.coordinates.x}`,
                        `Longitude: ${scan.location.coordinates.y}`,
                    ]}
                />
                <Card
                    simple
                    title={"Robô"}
                    infos={["Nome: " + scan.robot.name, `Ip: ${scan.robot.ip}`]}
                />
            </div>
            <h3 className="text-2xl mb-8 mt-20">Informações detectadas pelos sensores</h3>
            <div className="grid grid-cols-3 gap-8">
            <Card
                    simple
                    title={"Humidade"}
                    infos={[
                        `Mínima: ${scan.humidity_min}`,
                        `Média: ${mean(scan.humidity_min, scan.humidity_max)}`,
                        `Máxima: ${scan.humidity_max}`,
                    ]}
                />
                <Card
                    simple
                    title={"Oxigênio"}
                    infos={[
                        `Mínimo: ${scan.oxygen_min}`,
                        `Médio: ${mean(scan.oxygen_min, scan.oxygen_max)}`,
                        `Máximo: ${scan.oxygen_max}`,
                    ]}
                />
                <Card
                    simple
                    title={"Temperatura"}
                    infos={[
                        `Mínima: ${scan.temperature_min}`,
                        `Média: ${mean(scan.temperature_min, scan.temperature_max)}`,
                        `Máxima: ${scan.temperature_max}`,
                    ]}
                />
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

export default Scan;
