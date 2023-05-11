import Image from "next/image";
import Wrapper from "@/components/wrapper";
import Card from "@/components/card";
import CardList from "@/components/cardList";

export default function Home() {
    const routes = [
        {
            title: "Rota 1",
            subtitle: "86% de oxigênio",
            info: "01/09/2002 - 14:33:40",
        },
        {
            title: "Rota 1",
            subtitle: "86% de oxigênio",
            info: "01/09/2002 - 14:33:40",
        },
        {
            title: "Rota 1",
            subtitle: "86% de oxigênio",
            info: "01/09/2002 - 14:33:40",
        },
        {
            title: "Rota 1",
            subtitle: "86% de oxigênio",
            info: "01/09/2002 - 14:33:40",
        },
        {
            title: "Rota 1",
            subtitle: "86% de oxigênio",
            info: "01/09/2002 - 14:33:40",
        },
    ];

    const rooms = [
        {
            title: "Sala #9048",
            subtitle: "Rua Professor Almeida Prado, 520",
            info: "4 simulações realizadas",
            link: "/room/1",
        },
        {
            title: "Sala #9048",
            subtitle: "Rua Professor Almeida Prado, 520",
            info: "4 simulações realizadas",
            link: "/room/1",
        },
        {
            title: "Sala #9048",
            subtitle: "Rua Professor Almeida Prado, 520",
            info: "4 simulações realizadas",
            link: "/room/1",
        },
        {
            title: "Sala #9048",
            subtitle: "Rua Professor Almeida Prado, 520",
            info: "4 simulações realizadas",
            link: "/room/1",
        },
    ];

    const rightSide = (
        <div className="p-10 bg-[#F5FBFF]">
            <h1 className="text-3xl mt-10 font-medium mb-10">Salas</h1>
            <CardList columns={"grid-cols-1"} items={rooms} />
        </div>
    );

    return (
        <Wrapper
            title={"Histórico de rotas"}
            subtitle="Bem vindo,"
            rightSide={rightSide}
        >
            <CardList columns={"grid-cols-3"} items={routes} />
        </Wrapper>
    );
}
