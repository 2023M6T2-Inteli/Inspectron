import Image from "next/image";
import Wrapper from "@/components/wrapper";
import Card from "@/components/card";
import CardList from "@/components/cardList";
import { useEffect, useMemo, useState } from "react";
import { toast } from "react-toastify";
import { createServerSideAxiosInstance } from "@/config/axios";
import { Location, Scan } from "../dashboard";
import { withAuth } from "@/HOC/withAuth";
import { GetServerSidePropsContext, PreviewData } from "next";
import { ParsedUrlQuery } from "querystring";
import dynamic from "next/dynamic";
import Moment from "react-moment";

const MapWithNoSSR = dynamic(() => import("../../components/map"), {
    ssr: false,
});

interface Props {
    scans: Scan[];
    location: Location;
}

const Location = ({ scans, location }: Props) => {
    const scansMemo = useMemo(() => {
        return scans.map((scan) => {
            return {
                title: scan.name,
                subtitle: "86% de oxigênio",
                infos: [<Moment format="DD/MM/YYYY HH:mm" key={scan._id.$oid}>{scan.created_at.$date}</Moment>],
                link: `/scan/${scan._id.$oid}`,
            };
        });
    }, [scans]);

    const LocationInfo = () => (
        <div className="h-[40vh]">
            <MapWithNoSSR position={[location.coordinates.x, location.coordinates.y]} />
        </div>
    );

    return (
        <Wrapper title={location.name}>
            <p className="text-2xl mb-4">Varreduras realizadas nessa localização</p>
            <CardList columns={"grid-cols-4"} items={scansMemo} />
            <p className="text-2xl mt-8 mb-4">Mapa</p>
            <Card content={<LocationInfo />} />
        </Wrapper>
    );
};
export const getServerSideProps = async (ctx: GetServerSidePropsContext<ParsedUrlQuery, PreviewData>) => {
    return await withAuth(ctx, async () => {
        const axios = await createServerSideAxiosInstance(ctx);
        const { data } = await axios.get("/scans/location/" + ctx.query.id);

        return {
            props: { scans: data.scans, location: data.location },
        };
    });
};

export default Location;
