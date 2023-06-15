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
    return (
        <Wrapper title={scan._id.$oid}>
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
