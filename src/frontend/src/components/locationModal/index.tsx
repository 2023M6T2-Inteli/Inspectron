import Button, { ButtonTypes } from "@/components/button";
import Input from "@/components/input";
import Modal from "@/components/modal";
import React from "react";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";
import { axios } from "@/config/axios";
import { toast } from "react-toastify";

const schema = yup
    .object({
        name: yup.string().required("Esse campo é obrigatório."),
        x: yup.number().typeError("Esse campo deve ser um número.").required("Esse campo é obrigatório."),
        y: yup.number().typeError("Esse campo deve ser um número.").required("Esse campo é obrigatório."),
    })
    .required();

interface Props {
    showModal: boolean;
    setShowModal: (show: boolean) => void;
}

const LocationModal: React.FC<Props> = ({ showModal, setShowModal }) => {
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
            await axios.post("/locations/create", data);
            toast.success("Localização cadastrada com sucesso.");
            setShowModal(false);
            reset();
        } catch (err) {
            toast.error("Erro ao cadastrar robô.");
        }
    };

    return (
        <Modal showModal={showModal} title="Cadastrar nova localização" closeModal={() => setShowModal(false)}>
            <form className="flex flex-col gap-4" onSubmit={handleSubmit(onSubmit)}>
                <Input
                    label="Nome"
                    placeholder="Digite aqui o nome..."
                    register={{ ...register("name") }}
                    error={errors.name?.message as string}
                />
                <Input
                    label="Latitude"
                    placeholder="Digite aqui a latitude..."
                    register={{ ...register("x") }}
                    error={errors.x?.message as string}
                />
                <Input
                    label="Longitude"
                    placeholder="Digite aqui a longitude..."
                    error={errors.y?.message as string}
                    register={{ ...register("y") }}
                />
                <Button buttonType={ButtonTypes.primary}>Criar</Button>
            </form>
        </Modal>
    );
};

export default LocationModal;
