import React, { useEffect, useState } from "react";
import Card from "../card";
import Link from "next/link";
import { Variants, motion } from "framer-motion";
import Loader from "../loader";

const container: Variants = {
    hidden: { opacity: 1, scale: 0 },
    visible: {
        opacity: 1,
        scale: 1,
        transition: {
            delayChildren: 0.3,
            staggerChildren: 0.2,
        },
    },
};

const itemVariants: Variants = {
    hidden: { y: 20, opacity: 0 },
    visible: {
        y: 0,
        opacity: 1,
    },
};

interface Props {
    items: {
        title: string;
        subtitle: string;
        info: string;
        link?: string;
    }[];
    columns: string;
    loading?: boolean;
}

const CardList: React.FC<Props> = ({ items, columns, loading }) => {
    let content: JSX.Element | JSX.Element[] = <div className="mx-auto"><Loader /></div>

    if (!loading) {
        content = items.length > 0 ? (
            items.map((item, index) => (
                <motion.div variants={itemVariants} key={index}>
                    {item.link ? (
                        <Link href={item.link} key={index}>
                            <Card {...item} />
                        </Link>
                    ) : (
                        <Card key={index} {...item} />
                    )}
                </motion.div>
            ))
        ) : (
            <div className="text-center text-black-400">Nenhum item encontrado</div>
        )
    }
    console.log(loading)
    return (
        <motion.div variants={container} initial="hidden" animate="visible" className={`grid gap-4 ${loading ? 'items-center grow' : columns}`}>
            {content}
        </motion.div>
    );
};

export default CardList;
