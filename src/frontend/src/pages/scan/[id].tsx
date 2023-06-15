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

const Scan = (props: Props) => {
    return (
        <Wrapper title={"Sala #9083"}>
            <div className="grid grid-cols-3 gap-8">
                <Card
                    simple
                    title={"Localização"}
                    simpleInfos={[
                        "Nome: " + props.scan.location.name,
                        `Latitude: ${props.scan.location.coordinates.x}`,
                        `Longitude: ${props.scan.location.coordinates.y}`,
                    ]}
                />
                <Card
                    simple
                    title={"Robô"}
                    simpleInfos={["Nome: " + props.scan.robot.name, `Ip: ${props.scan.robot.ip}`]}
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
