import React, { useEffect, useState } from "react";
import Card from "../card";
import Link from "next/link";
import { motion } from "framer-motion";
import Loader from "../loader";

const container = {
    hidden: { opacity: 1, scale: 0 },
    visible: {
        opacity: 1,
        scale: 1,
        transition: {
            when: "beforeChildren",
        },
    },
};

const itemVariants = {
    hidden: { y: 20, opacity: 0 },
    visible: { y: 0, opacity: 1 },
};

interface Props {
    items: {
        title: string;
        subtitle?: string;
        infos: string[] | JSX.Element[];
        link?: string;
    }[];
    columns: string;
    loading?: boolean;
}

const CardList: React.FC<Props> = ({ items, columns, loading }) => {
    let content: JSX.Element | JSX.Element[] = (
        <div className="mx-auto">
            <Loader />
        </div>
    );

    if (!loading) {
        content =
            items.length > 0 ? (
                <motion.div variants={container} initial="hidden" animate="visible" className={`grid gap-4 ${columns}`}>
                    {items.map((item, index) => (
                        <motion.div
                            variants={itemVariants}
                            key={index}
                            transition={{ delay: index * 0.2 }} // Delay each card by 0.2 seconds
                        >
                            {item.link ? (
                                <div className="hover:-translate-y-1 transition-all">
                                    <Link href={item.link} key={index}>
                                        <Card {...item} />
                                    </Link>
                                </div>
                            ) : (
                                <Card key={index} {...item} />
                            )}
                        </motion.div>
                    ))}
                </motion.div>
            ) : (
                <div className="text-center text-black-400">Nenhum item encontrado</div>
            );
    }

    return content;
};

export default CardList;
