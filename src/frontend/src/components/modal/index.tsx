import React from "react";
import { X } from "lucide-react";
import Backdrop from "../backdrop";

interface Props {
    title: string;
    subtitle?: string;
    children: React.ReactNode;
    closeModal: () => void;
}

const Modal: React.FC<Props> = ({ title, subtitle, children, closeModal }) => {
    return (
        <>
            <div className="z-20 fixed top-[50%] left-[50%] translate-x-[-50%] translate-y-[-50%] bg-white p-10 rounded-lg min-w-[30vw] min-h-[40vh]">
                <div className="flex items-center justify-between mb-6">
                    <h4 className="text-3xl">{title}</h4>
                    <X size={30} className="cursor-pointer hover:scale-110 transition-all" onClick={closeModal} />
                </div>
                <div>{children}</div>
            </div>
            <Backdrop closeModal={closeModal} />
        </>
    );
};

export default Modal;
