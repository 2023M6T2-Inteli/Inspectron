import React from "react";

interface Props {
    title: string;
    subtitle?: string;
    info?: string;
    simple?: boolean;
    simpleInfos?: string[];
}

const Card: React.FC<Props> = ({ title, subtitle, info, simple, simpleInfos }) => {
    if (simple && simpleInfos) {
        return (
            <div className="bg-white rounded-xl shadow-xl p-6 flex flex-col text-center justify-center">
                <p className="text-2xl mb-4">{title}</p>
                <div className="flex flex-col gap-2">
                    {simpleInfos.map((info) => (
                        <p key={info} className="text-stone-700 text-xl">
                            {info}
                        </p>
                    ))}
                </div>
            </div>
        );
    }

    return (
        <div className="bg-white rounded-xl shadow-xl p-6">
            <p className="text-lg mb-2">{title}</p>
            <p className="text-zinc-500 mb-24">{subtitle}</p>
            <p className="text-zinc-500">{info}</p>
        </div>
    );
};

export default Card;
