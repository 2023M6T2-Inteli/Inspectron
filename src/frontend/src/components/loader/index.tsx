import React from "react";
import { BeatLoader } from "react-spinners";

interface Props {}

const Loader: React.FC<Props> = (props) => {
    return (
        <div className="h-full w-full flex items-center justify-center">
            <BeatLoader size={20} color="#1E40AF" />
        </div>
    );
};

export default Loader;
