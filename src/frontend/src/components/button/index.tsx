import React, { ButtonHTMLAttributes } from "react";

export enum ButtonTypes {
    primary,
    danger,
}

interface Props extends ButtonHTMLAttributes<HTMLButtonElement> {
    children?: React.ReactNode;
    buttonType: ButtonTypes;
}

const Button: React.FC<Props> = ({ children, buttonType, ...rest }) => {
    let classes =
        "py-3 hover:scale-[1.03] transition-all rounded-lg block text-xl px-8 disabled:bg-slate-400 disabled:cursor-not-allowed ";

    switch (buttonType) {
        case ButtonTypes.primary:
            return (
                <button
                    {...rest}
                    className={`${classes} bg-blue-800 text-white`}
                >
                    {children}
                </button>
            );
        case ButtonTypes.danger:
            return (
                <button {...rest} className={`${classes} bg-red-600 text-white`}>
                    {children}
                </button>
            );
        default:
            return <button>{children}</button>;
    }
};

export default Button;
