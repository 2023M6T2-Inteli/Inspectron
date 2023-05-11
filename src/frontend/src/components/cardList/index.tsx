import React, { useEffect, useState } from "react";
import Card from "../card";
import Link from "next/link";
import { Variants, motion } from "framer-motion";

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
}

const CardList: React.FC<Props> = ({ items, columns }) => {
    return (
        <motion.div
            variants={container}
            initial="hidden"
            animate="visible"
            className={"grid gap-4 " + columns}
        >
            {items.map((item, index) => (
                <motion.div variants={itemVariants} key={index}>
                    {item.link ? (
                        <Link href={item.link} key={index}>
                            <Card {...item} />
                        </Link>
                    ) : (
                        <Card key={index} {...item} />
                    )}
                </motion.div>
            ))}
        </motion.div>
    );
};

export default CardList;
