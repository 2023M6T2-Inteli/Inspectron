import React from "react";
import Sidebar from "../sidebar";

interface Props {
    children: React.ReactNode;
    title: string;
    subtitle?: string;
}

const Wrapper: React.FC<Props> = ({ children, title, subtitle }) => {
    return (
        <div className="flex gap-2 min-h-[100vh]">
            <Sidebar />
            <div className="p-12">
                {subtitle && (
                    <h2 className="text-xl font-medium mb-4">{subtitle}</h2>
                )}
                <h1 className="text-3xl font-medium mb-10">{title}</h1>
                {children}
            </div>
        </div>
    );
};

export default Wrapper;
