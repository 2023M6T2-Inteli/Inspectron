import React from "react";

interface Props {
    title: string;
    subtitle: string;
    info?: string;
}

const Card: React.FC<Props> = ({ title, subtitle, info }) => {
    return (
        <div className="bg-white rounded-xl shadow-xl p-6">
            <p className="text-lg mb-2">{title}</p>
            <p className="text-zinc-500 mb-24">{subtitle}</p>
            <p className="text-zinc-500">{info}</p>
        </div>
    );
};

export default Card;
