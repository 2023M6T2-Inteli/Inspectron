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

interface Props {
    scans: Scan[];
    location: Location
}

const Location = ({ scans,location }: Props) => {
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

    return (
        <Wrapper title={location.name}>
            <CardList columns={"grid-cols-4"} items={scansMemo} />
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
