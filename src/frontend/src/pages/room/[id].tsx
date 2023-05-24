import Image from "next/image";
import Wrapper from "@/components/wrapper";
import Card from "@/components/card";
import CardList from "@/components/cardList";

export default function Room() {
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

   

    return (
        <Wrapper title={"Sala #9083"} >
            <CardList columns={'grid-cols-4'} items={routes} />
        </Wrapper>
    );
}
