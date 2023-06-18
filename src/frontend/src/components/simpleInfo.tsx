import React from "react";

interface Props {
  label: string;
  value: string;
}

const SimpleInfo: React.FC<Props> = ({label, value}) => {
    return (
        <div className="flex flex-col items-center">
            <label className="text-xl">{label}</label>
            <p className="text-xl">{value}</p>
        </div>
    );
};

export default SimpleInfo;
