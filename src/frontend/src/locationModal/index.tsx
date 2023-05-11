import Button, { ButtonTypes } from "@/components/button";
import Input from "@/components/input";
import Modal from "@/components/modal";
import React from "react";
import { useForm } from "react-hook-form";
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from "yup";

const schema = yup.object({
  name: yup.string().required("Esse campo é obrigatório."),
  x: yup.number().required("Esse campo é obrigatório."),
  y: yup.number().required("Esse campo é obrigatório."),
}).required();


interface Props {
    showModal: boolean;
    setShowModal: (show: boolean) => void;
}

const LocationModal: React.FC<Props> = ({ showModal, setShowModal }) => {
    const {
        register,
        handleSubmit,
        watch,
        formState: { errors },
    } = useForm({
      resolver: yupResolver(schema),
    });
    const onSubmit = (data: any) => console.log(data);
    
    return (
        <Modal showModal={showModal} title="Criar novo lugar" closeModal={() => setShowModal(false)}>
            <form
                className="flex flex-col gap-4"
                onSubmit={handleSubmit(onSubmit)}
            >
                <Input
                    label="Nome"
                    placeholder="Digite aqui o nome..."
                    {...register("name")}
                    error={errors.name?.message as string}
                />
                <Input
                    label="Latitude"
                    placeholder="Digite aqui a latitude..."
                    {...register("x")}
                    error={errors.x?.message as string}

                />
                <Input
                    label="Longitude"
                    placeholder="Digite aqui a longitude..."
                    {...register("y")}
                    error={errors.y?.message as string}

                />
                <Button buttonType={ButtonTypes.primary}>Criar</Button>
            </form>
        </Modal>
    );
};

export default LocationModal;
