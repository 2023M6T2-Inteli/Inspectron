import React from "react";
import Button, { ButtonTypes } from "../button";
import { FieldError, FieldErrorsImpl, Merge } from "react-hook-form";

interface Props extends React.InputHTMLAttributes<HTMLInputElement> {
    label?: string;
    error?: string;
}

const Input: React.FC<Props> = ({ label, error, ...rest }) => {
    return (
        <div>
            {label && <label className=" text-lg block">{label}</label>}
            <input className="py-1 outline-none border-b-2 w-full" {...rest} />
            {error && <span className="text-red-800 mt-1 block">{error}</span>}
        </div>
    );
};

export default Input;
