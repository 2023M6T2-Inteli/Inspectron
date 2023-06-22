import Wrapper from "@/components/wrapper";
import CardList from "@/components/cardList";
import { useMemo } from "react";
import { withAuth } from "@/HOC/withAuth";
import { GetServerSidePropsContext, PreviewData } from "next";
import { ParsedUrlQuery } from "querystring";
import { createServerSideAxiosInstance } from "@/config/axios";
import Moment from 'react-moment';

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
    name: string
    temperature_min: number;
    temperature_max: number;
    eco2_min: number;
    eco2_max: number;
    tvoc_min: number;
    tvoc_max: number;
    location: Location;
    robot: Robot;
    created_at: {
        $date: number;
    }
    video_filename: string;
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
    console.log(scans)
    const scansMemo = useMemo(() => {
        return scans.map((scan) => {
            return {
                title: scan.name,
                subtitle: "86% de oxigênio",
                infos: [<Moment format="DD/MM/YYYY - HH:mm:ss" key={scan._id.$oid}>{scan.created_at.$date}</Moment>],
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
