import Image from "next/image";
import Wrapper from "@/components/wrapper";
import Card from "@/components/card";
import CardList from "@/components/cardList";
import { useEffect, useMemo, useState } from "react";
import { toast } from "react-toastify";
import { axios } from "@/config/axios";
import { Scan } from "../dashboard";
import withAuth, { getServerSideProps } from "@/HOC/withAuth";

const Room = () => {
    const [loading, setLoading] = useState<boolean>(true);
    const [scans, setScans] = useState<Scan[]>([]);

    const getScans = async () => {
        try {
            const { data } = await axios.get("/scans");
            setScans(data);
        } catch (err) {
            toast.error("Erro ao carregar varreduras");
        }
        setLoading(false);
    };

    useEffect(() => {
        getScans();
    }, []);

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
            <CardList columns={"grid-cols-4"} items={scansMemo} loading={loading} />
        </Wrapper>
    );
};

export { getServerSideProps };

export default withAuth(Room);
