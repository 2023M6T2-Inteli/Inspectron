import React, { useEffect } from "react";
import Select from "@/components/select";
import { PlusSquare } from "lucide-react";
import Button, { ButtonTypes } from "../button";
import LocationModal from "@/components/locationModal";
import RobotModal from "../robotModal";
import AsyncSelect from "../asyncSelect";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";
import Input from "../input";

const schema = yup
    .object({
        name: yup.string().required("Esse campo é obrigatório."),
        robot: yup.string().required("Esse campo é obrigatório."),
        location: yup.string().required("Esse campo é obrigatório."),
    })
    .required();

export interface Option {
    value: string;
    label: string;
}

interface Props {
    buttonHandler: (data: any) => void;
}

const StartScan: React.FC<Props> = ({ buttonHandler }) => {
    const [showLocationModal, setShowLocationModal] = React.useState(false);
    const [showRobotModal, setShowRobotModal] = React.useState(false);

    const {
        register,
        control,
        handleSubmit,
        reset,
        formState: { errors },
    } = useForm({
        resolver: yupResolver(schema),
    });

    return (
        <>
            <div className="h-full flex justify-center items-center">
                <form onSubmit={handleSubmit(buttonHandler)} className="w-96 flex flex-col gap-6">
                    <Input placeholder="Digite um nome..." selectDesign register={{...register("name")}} error={errors.name?.message as string} label="Nome" />
                    <AsyncSelect
                        link="/robots"
                        label="Robô"
                        placeholder={"Selecione um robô..."}
                        addIcon={
                            <PlusSquare
                                onClick={() => setShowRobotModal(true)}
                                color="#1E40AF"
                                className="!w-10 h-10 cursor-pointer hover:scale-105 transition-all"
                            />
                        }
                        reload={showRobotModal}
                        control={control}
                        name="robot"
                        error={errors.robot?.message as string}
                    />
                    <AsyncSelect
                        link="/locations"
                        placeholder={"Selecione uma localização..."}
                        label="Localização"
                        addIcon={
                            <PlusSquare
                                onClick={() => setShowLocationModal(true)}
                                color="#1E40AF"
                                className="!w-10 h-10 cursor-pointer hover:scale-105 transition-all"
                            />
                        }
                        reload={showLocationModal}
                        control={control}
                        name="location"
                        error={errors.location?.message as string}
                    />
                    <Button buttonType={ButtonTypes.primary}>Iniciar varredura</Button>
                </form>
            </div>
            <RobotModal showModal={showRobotModal} setShowModal={setShowRobotModal} />
            <LocationModal showModal={showLocationModal} setShowModal={setShowLocationModal} />
        </>
    );
};

export default StartScan;
