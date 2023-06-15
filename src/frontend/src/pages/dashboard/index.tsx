import Wrapper from "@/components/wrapper";
import CardList from "@/components/cardList";
import { useMemo } from "react";
import { withAuth } from "@/HOC/withAuth";
import { GetServerSidePropsContext, PreviewData } from "next";
import { ParsedUrlQuery } from "querystring";
import { createServerSideAxiosInstance } from "@/config/axios";

export interface Location {
    _id: {
        $oid: string;
    };
    name: string;
    coordinates: {
        x: number;
        y: number;
    };
}

export interface Robot {
    _id: {
        $oid: string;
    };
    name: string;
    ip: string;
}

export interface Scan {
    _id: {
        $oid: string;
    };
    location: Location;
    robot: Robot;
}

interface Room {
    _id: {
        $oid: string;
    };
    name: string;
    coordinates: {
        x: number;
        y: number;
    };
    scans: Scan[];
}

interface Props {
    locations: Room[];
    scans: Scan[];
}

const Home = ({ locations, scans }: Props) => {
    console.log(locations)
    const scansMemo = useMemo(() => {
        return scans.map((scan) => {
            return {
                title: scan._id.$oid,
                subtitle: "86% de oxigênio",
                infos: ["01/09/2002 - 14:33:40"],
                link: `/scan/${scan._id.$oid}`,
            };
        });
    }, [scans]);

    const locationsMemo = useMemo(() => {
        return locations.map((room) => {
            return {
                title: room.name,
                subtitle: `x: ${room.coordinates.x} | y: ${room.coordinates.y}`,
                infos: [`${room.scans ? room.scans.length : 0} varreduras realizadas`],
                link: `/location/${room._id.$oid}`,
            };
        });
    }, [locations]);

    const rightSide = (
        <div className="p-10 bg-[#F5FBFF] min-w-[20vw] flex flex-col">
            <h1 className="text-3xl mt-10 font-medium mb-10">Locais</h1>
            <CardList columns={"grid-cols-1"} items={locationsMemo} />
        </div>
    );

    return (
        <Wrapper title={"Histórico de varreduras"} subtitle="Bem vindo," rightSide={rightSide}>
            <CardList columns={"grid-cols-3"} items={scansMemo} />
        </Wrapper>
    );
};

export const getServerSideProps = async (ctx: GetServerSidePropsContext<ParsedUrlQuery, PreviewData>) => {
    return await withAuth(ctx, async () => {
        const axios = await createServerSideAxiosInstance(ctx);
        const { data: locations } = await axios.get("/locations");
        const { data: scans } = await axios.get("/scans");

        return {
            props: { locations, scans },
        };
    });
};

export default Home;
