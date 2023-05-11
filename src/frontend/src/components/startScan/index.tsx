import React from "react";
import Select from "@/components/select";
import { PlusSquare } from "lucide-react";
import Button, { ButtonTypes } from "../button";

interface Option {
    value: string;
    label: string;
}

const options: Option[] = [
    { value: "chocolate", label: "Chocolate" },
    { value: "strawberry", label: "Strawberry" },
    { value: "vanilla", label: "Vanilla" },
];

interface Props {
  buttonHandler: () => void;
  setShowModal: (show: boolean) => void
}

const StartScan: React.FC<Props> = ({buttonHandler, setShowModal}) => {
    const [selectedOption, setSelectedOption] = React.useState<string | null>(null);
    
    return (
        <div className="h-full flex justify-center items-center">
            <div className="w-96 flex flex-col gap-4">
                <Select
                    options={options}
                    label="Lugar"
                    addIcon={
                        <PlusSquare
                            onClick={() => setShowModal(true)}
                            color="#1E40AF"
                            className="!w-10 h-10 cursor-pointer hover:scale-105 transition-all"
                        />
                    }
                    onChange={(event: any) => setSelectedOption(event.value)}
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
    );
};

export default StartScan;
