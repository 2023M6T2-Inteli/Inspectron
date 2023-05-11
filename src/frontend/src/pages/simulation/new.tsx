import Button, { ButtonTypes } from "@/components/button";
import SimpleInfo from "@/components/simpleInfo";
import Wrapper from "@/components/wrapper";
import React from "react";
import { toast } from "react-toastify";
import { PlusSquare } from "lucide-react";
import Modal from "@/components/modal";
import StartScan from "@/components/startScan";
import LiveScan from "@/components/liveScan";
import LocationModal from "@/locationModal";

const NewSimulation: React.FC = (props) => {
    const [stage, setStage] = React.useState(0);
    const [showModal, setShowModal] = React.useState(false);

    const startScan = () => {
        toast.success("Varredura iniciada com sucesso!");
        setStage(1);
    };

    const emergencyStop = () => {
        toast.info("Varredura finalizada com sucesso!");
        setStage(0);
    };

    let content = null;
    switch (stage) {
        case 0:
            content = (
                <StartScan
                    buttonHandler={startScan}
                    setShowModal={setShowModal}
                />
            );
            break;
        case 1:
            content = <LiveScan buttonHandler={emergencyStop} />;
            break;
    }

    return (
        <Wrapper title={"Nova varredura"}>
            <div className="bg-white rounded-xl shadow-2xl p-8 grow">
                {content}
            </div>
            {showModal && <LocationModal setShowModal={setShowModal} />}
        </Wrapper>
    );
};

export default NewSimulation;
