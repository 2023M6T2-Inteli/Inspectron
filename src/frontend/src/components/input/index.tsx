import React from "react";
import { LucideIcon } from "lucide-react";

interface Props extends React.InputHTMLAttributes<HTMLInputElement> {
    label?: string;
    error?: string;
    Icon?: LucideIcon;
    register?: any;
    selectDesign?: boolean;
}

const Input: React.FC<Props> = ({ label, error, Icon, register, selectDesign, ...rest }) => {
    let content = (
        <>
            {label && <label className={"text-[#7A7A96] text-lg mb-1 block"}>{label}</label>}
            <div className="border-2 p-3 w-full flex items-center gap-4 text-[#B9BCC7] rounded-lg">
                {Icon && <Icon />}
                <input
                    className="grow py-1 bg-transparent outline-none placeholder-[#B9BCC7] text-gray-950"
                    {...rest}
                    {...register}
                />
            </div>
        </>
    );

    if (selectDesign) {
        content = (
            <>
                {label && <label className={"text-lg mb-1 block"}>{label}</label>}
                <div className="border p-2 px-4 w-full flex items-center gap-4 rounded-[4px] border-[#cccbcb]">
                    {Icon && <Icon />}
                    <input
                        className="grow py-1 bg-transparent outline-none placeholder-[#808080] text-gray-950"
                        {...rest}
                        {...register}
                    />
                </div>
            </>
        );
    }

    return (
        <div>
            {content}
            {error && <span className="text-red-800 mt-1 block">{error}</span>}
        </div>
    );
};

export default Input;
