import React from "react";
import Sidebar from "../sidebar";
import Head from "next/head";
import { Variants, motion } from "framer-motion";

interface Props {
    children: React.ReactNode;
    rightSide?: React.ReactNode;
    title: string;
    subtitle?: string;
}

const container: Variants = {
    hidden: { opacity: 0, scale: 0.8 },
    visible: {
        opacity: 1,
        scale: 1,
        transition: {
            ease: "easeInOut",
        }
    },
};

const Wrapper: React.FC<Props> = ({ children, title, subtitle, rightSide }) => {
    return (
        <>
            <Head>
                <title>{title}</title>
            </Head>
            <div className="relative min-h-[100vh]">
                <Sidebar />
                <motion.div
                    variants={container}
                    initial="hidden"
                    animate="visible"
                    className="flex absolute left-[20vw] w-[80vw] min-h-[100vh]"
                >
                    <div className="p-12 px-8 grow flex flex-col">
                        {subtitle && (
                            <h2 className="text-xl font-medium mb-4">
                                {subtitle}
                            </h2>
                        )}
                        <h1 className="text-4xl font-medium mb-10">{title}</h1>
                        {children}
                    </div>
                    {rightSide!}
                </motion.div>
            </div>
        </>
    );
};

export default Wrapper;
