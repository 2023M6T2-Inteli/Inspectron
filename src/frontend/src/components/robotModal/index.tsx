import Button, { ButtonTypes } from "@/components/button";
import Input from "@/components/input";
import Modal from "@/components/modal";
import React from "react";
import { set, useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";
import { toast } from "react-toastify";
import { axios } from "@/config/axios";

const schema = yup
    .object({
        name: yup.string().required("Esse campo é obrigatório."),
        ip: yup.string().required("Esse campo é obrigatório."),
    })
    .required();

interface Props {
    showModal: boolean;
    setShowModal: (show: boolean) => void;
}

const RobotModal: React.FC<Props> = ({ showModal, setShowModal }) => {
    const {
        register,
        handleSubmit,
        reset,
        formState: { errors },
    } = useForm({
        resolver: yupResolver(schema),
    });

    const onSubmit = async (data: any) => {
        try {
            await axios.post("/robots/create", data);
            toast.success("Robô cadastrado com sucesso.");
            setShowModal(false);
            reset()
        } catch (err) {
            toast.error("Erro ao cadastrar robô.");
        }
    };

    return (
        <Modal showModal={showModal} title="Cadastrar novo robô" closeModal={() => setShowModal(false)}>
            <form className="flex flex-col gap-4" onSubmit={handleSubmit(onSubmit)}>
                <Input
                    label="Nome"
                    placeholder="Digite aqui o nome..."
                    error={errors.name?.message as string}
                    register={{...register("name")}}
                    
                />
                <Input
                    label="Ip"
                    placeholder="Digite aqui o ip..."
                    error={errors.ip?.message as string}
                    register={{...register("ip")}}
                />

                <Button buttonType={ButtonTypes.primary}>Criar</Button>
            </form>
        </Modal>
    );
};

export default RobotModal;
