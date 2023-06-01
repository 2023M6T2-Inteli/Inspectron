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
    scans: Scan[];
}

const Room = ({ scans }: Props) => {
    const scansMemo = useMemo(() => {
        return scans.map((scan) => {
            return {
                title: scan._id.$oid,
                subtitle: "86% de oxigênio",
                info: "01/09/2002 - 14:33:40",
            };
        });
    }, [scans]);

    return (
        <Wrapper title={"Sala #9083"}>
            <CardList columns={"grid-cols-4"} items={scansMemo} />
        </Wrapper>
    );
};
export const getServerSideProps = async (ctx: GetServerSidePropsContext<ParsedUrlQuery, PreviewData>) => {
    return await withAuth(ctx, async () => {
        const axios = await createServerSideAxiosInstance(ctx);
        const { data: scans } = await axios.get("/scans");

        return {
            props: { scans },
        };
    });
};

export default Room;
