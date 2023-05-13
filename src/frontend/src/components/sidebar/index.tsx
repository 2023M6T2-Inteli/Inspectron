import Image from "next/image";
import React from "react";
import Logo from "@/assets/logo.png";
import { LayoutDashboard, Plus } from "lucide-react";
import Link from "next/link";
import { useRouter } from "next/router";
import Avatar from "@/assets/avatar.png"

interface Props {}

const Sidebar: React.FC<Props> = (props) => {
  const router = useRouter();
    const items = [
        {
            icon: LayoutDashboard,
            label: "Varreduras/Locais",
            link: "/",
        },
        {
            icon: Plus,
            label: "Nova varredura",
            link: "/simulation/new",
        },
    ];

    return (
        <div className="w-[20vw] min-h-[100vh] flex flex-col py-8 border-r-2 border-[#E4E4E4] fixed">
            <Image alt="Logo" src={Logo} className="mx-auto mb-6" />

            <div className="flex flex-col gap-2">
                {items.map((item, index) => (
                    <Link
                        className={`flex pl-6 py-5 mr-10 rounded-r-2xl gap-4 text-xl items-center text-[#A3A3A5] ${router.pathname == item.link && "bg-slate-900 !text-white"}`}
                        key={item.link}
                        href={item.link}
                    >
                        <item.icon /> <p>{item.label}</p>{" "}
                    </Link>
                ))}
            </div>

            <div className="mt-auto flex gap-4 justify-center items-center text-lg">
              <Image alt="Avatar" src={Avatar} className="" />
              <p>Alfredo Soares Azevedo</p>
            </div>
        </div>
    );
};

export default Sidebar;
