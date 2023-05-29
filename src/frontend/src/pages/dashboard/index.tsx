import Image from "next/image";
import Wrapper from "@/components/wrapper";
import Card from "@/components/card";
import CardList from "@/components/cardList";
import { useCallback, useEffect, useMemo, useState } from "react";
import { toast } from "react-toastify";
import { axios } from "@/config/axios";

export interface Scan {
    _id: {
        $oid: string;
    };
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

export default function Home() {
    const routes = [
        {
            title: "Varredura 1",
            subtitle: "86% de oxigênio",
            info: "01/09/2002 - 14:33:40",
        },
        {
            title: "Varredura 1",
            subtitle: "86% de oxigênio",
            info: "01/09/2002 - 14:33:40",
        },
        {
            title: "Varredura 1",
            subtitle: "86% de oxigênio",
            info: "01/09/2002 - 14:33:40",
        },
        {
            title: "Varredura 1",
            subtitle: "86% de oxigênio",
            info: "01/09/2002 - 14:33:40",
        },
        {
            title: "Varredura 1",
            subtitle: "86% de oxigênio",
            info: "01/09/2002 - 14:33:40",
        },
    ];

    const [rooms, setRooms] = useState<Room[]>([]);
    const [scans, setScans] = useState<Scan[]>([]);
    const [scansLoading, setScansLoading] = useState<boolean>(true);
    const [roomsLoading, setRoomsLoading] = useState<boolean>(true);

    const getScans = async () => {
        try {
            const {data} = await axios.get("/scans");
            setScans(data);
        } catch(err) {
            toast.error("Erro ao carregar varreduras");
        }
        setScansLoading(false)
    }

    const scansMemo = useMemo(() => {
        return scans.map((scan) => {
            return {
                title: scan._id.$oid,
                subtitle: "86% de oxigênio",
                info: "01/09/2002 - 14:33:40",
            }
        })
    }, [scans])
    
    const roomsMemo = useMemo(() => {
        return rooms.map((room) => {
            return {
                title: room.name,
                subtitle: `x: ${room.coordinates.x} | y: ${room.coordinates.y}`,
                info: `${room.scans ? room.scans.length : 0} varreduras realizadas`,
                link: `/room/${room._id.$oid}`,
            };
        });
    }, [rooms]);


    const getRooms = async () => {
        try {
            const { data } = await axios.get("/locations");
            setRooms(data);
        } catch (err) {
            toast.error("Erro ao carregar dados");
        }
        setRoomsLoading(false);
    };

    useEffect(() => {
        Promise.all([getRooms(), getScans()])
    }, []);

    const rightSide = (
        <div className="p-10 bg-[#F5FBFF] min-w-[20vw] flex flex-col">
            <h1 className="text-3xl mt-10 font-medium mb-10">Locais</h1>
            <CardList columns={"grid-cols-1"} items={roomsMemo} loading={roomsLoading} />
        </div>
    );

    return (
        <Wrapper title={"Histórico de varreduras"} subtitle="Bem vindo," rightSide={rightSide}>
            <CardList columns={"grid-cols-3"} items={scansMemo} loading={scansLoading} />
        </Wrapper>
    );
}
