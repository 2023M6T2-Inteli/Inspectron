import React from "react";
import Select from "@/components/select";
import { PlusSquare } from "lucide-react";
import Button, { ButtonTypes } from "../button";
import LocationModal from "@/components/locationModal";
import RobotModal from "../robotModal";

interface Option {
    value: string;
    label: string;
}

const robotOptions: Option[] = [
    { value: "chocolate", label: "Robô #8932" },
    { value: "strawberry", label: "Robô #3421" },
    { value: "vanilla", label: "Robô #9743" },
];

const options: Option[] = [
    { value: "chocolate", label: "Duto #9823" },
    { value: "strawberry", label: "Duto #4932" },
    { value: "vanilla", label: "Sala #9123" },
];

interface Props {
    buttonHandler: () => void;
}

const StartScan: React.FC<Props> = ({ buttonHandler }) => {
    const [showLocationModal, setShowLocationModal] = React.useState(false);
    const [showRobotModal, setShowRobotModal] = React.useState(false);
    const [selectedOption, setSelectedOption] = React.useState<string | null>(
        null
    );

    return (
        <>
            <div className="h-full flex justify-center items-center">
                <div className="w-96 flex flex-col gap-6">
                    <Select
                        options={robotOptions}
                        label="Robô"
                        placeholder={"Selecione um robô..."}
                        addIcon={
                            <PlusSquare
                                onClick={() => setShowRobotModal(true)}
                                color="#1E40AF"
                                className="!w-10 h-10 cursor-pointer hover:scale-105 transition-all"
                            />
                        }
                        onChange={(event: any) =>
                            setSelectedOption(event.value)
                        }
                    />
                    <Select
                        options={options}
                        label="Localização"
                        placeholder={"Selecione uma localização..."}
                        addIcon={
                            <PlusSquare
                                onClick={() => setShowLocationModal(true)}
                                color="#1E40AF"
                                className="!w-10 h-10 cursor-pointer hover:scale-105 transition-all"
                            />
                        }
                        onChange={(event: any) =>
                            setSelectedOption(event.value)
                        }
                    />
                    <Button
                        buttonType={ButtonTypes.primary}
                        onClick={buttonHandler}
                        disabled={selectedOption == null}
                    >
                        Iniciar varredura
                    </Button>
                </div>
            </div>
            <RobotModal showModal={showRobotModal} setShowModal={setShowRobotModal} />
            <LocationModal showModal={showLocationModal} setShowModal={setShowLocationModal} />
        </>
    );
};

export default StartScan;
