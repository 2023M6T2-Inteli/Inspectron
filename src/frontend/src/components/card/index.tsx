import React from "react";

interface Props {
    info: string;
}

const InfoItem: React.FC<Props> = ({ info }) => <p className="text-stone-700 text-lg">{info}</p>;

interface CardProps {
    title?: string;
    subtitle?: string;
    simple?: boolean;
    infos?: string[];
    content?: React.ReactNode;
    rows?: string;
    columns?: string;
    alignLeft?: boolean;
    classes?: string;
}

const SimpleCard: React.FC<CardProps> = ({ title, infos, content, rows, columns, alignLeft }) => (
    <div
        className={`bg-white rounded-xl shadow-xl p-6 flex h-full flex-col ${
            !alignLeft && `text-center justify-center`
        } ${rows && rows} ${columns && columns}`}
    >
        {title && <p className="text-2xl mb-4">{title}</p>}

        {infos && (
            <div className="flex flex-col gap-2">
                {infos.map((info) => (
                    <InfoItem key={info} info={info} />
                ))}
            </div>
        )}
        {content && <div className="mt-4">{content}</div>}
    </div>
);

const DefaultCard: React.FC<CardProps> = ({ title, subtitle, infos, content, classes }) => (
    <div className={`bg-white rounded-xl shadow-xl p-6 ${classes && classes}`}>
        {title && <p className="text-lg mb-2">{title}</p>}
        {subtitle && <p className="text-zinc-500 mb-24">{subtitle}</p>}
        {infos && infos.map((info) => <InfoItem key={info} info={info} />)}
        {content && content}
    </div>
);

const Card: React.FC<CardProps> = (props) => {
    const { simple } = props;
    if (simple) {
        return <SimpleCard {...props} />;
    }

    return <DefaultCard {...props} />;
};

export default Card;
