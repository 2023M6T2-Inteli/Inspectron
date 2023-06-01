import Button, { ButtonTypes } from "@/components/button";
import Input from "@/components/input";
import { AtSign, Lock } from "lucide-react";
import Image from "next/image";
import HomeImage from "../assets/home.png";
import Head from "next/head";
import { useForm } from "react-hook-form";
import * as yup from "yup";
import { yupResolver } from "@hookform/resolvers/yup";
import { toast } from "react-toastify";
import { signIn, getCsrfToken } from "next-auth/react";
import { GetServerSideProps } from "next";
import { useRouter } from "next/router";

const schema = yup
    .object({
        email: yup.string().required("Esse campo é obrigatório."),
        password: yup.string().required("Esse campo é obrigatório."),
    })
    .required();

interface Props {
    csrfToken: string;
}

export default function Login({ csrfToken }: Props) {
    const router = useRouter();
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
            const res = await signIn("credentials", {
                redirect: false,

                email: data.email,
                password: data.password,
                callbackUrl: `${window.location.origin}`,
            });
          
            if (res!.ok) {
                toast.success("Login realizado com sucesso.");
                router.replace("/dashboard");
            } else {
                toast.error("Erro ao fazer login.");
            }
        } catch {
            toast.error("Erro ao fazer login.");
        }
    };

    return (
        <>
            <Head>
                <title>Login</title>
            </Head>
            <div className="min-h-[100vh] flex p-10">
                <div className="grow w-[50vw] flex items-center">
                    <div className="my-auto px-28 rounded-lg w-full">
                        <h1 className="text-4xl mb-2 text-[#0D0958]">Olá, bem vindo de volta!</h1>
                        <h3 className="text-xl text-[#7A7C95] mb-4">É um prazer ter você aqui.</h3>
                        <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col gap-6">
                            <input {...register("csrfToken")} type="hidden" defaultValue={csrfToken} />

                            <Input
                                register={{ ...register("email") }}
                                label="Email"
                                Icon={AtSign}
                                error={errors.email?.message as string}
                                placeholder="john@gmail.com"
                            />
                            <Input
                                register={{ ...register("password") }}
                                label="Senha"
                                Icon={Lock}
                                error={errors.password?.message as string}
                                placeholder="8+ caracteres obrigatórios"
                                type="password"
                            />
                            <Button buttonType={ButtonTypes.primary}>LOGIN</Button>
                        </form>
                    </div>
                </div>
                <div className="w-[50vw]">
                    <div className="p-8 w-full h-full bg-login-texture bg-no-repeat bg-cover overflow-hidden rounded-3xl relative">
                        <div className="absolute top-36 left-[50%] w-[60%] translate-x-[-50%] rounded-tl-4xl">
                            <h1 className="text-white font-bold  text-4xl">
                                Avaliações preliminares de espaços confiados em um só lugar
                            </h1>
                            <h5 className="text-white mt-4 text-xl">
                                Coloque as suas credenciais para ter acesso ao sistema.
                            </h5>
                        </div>
                        <div className="w-[70%] h-[30%] absolute top-[40%] left-[50%] translate-x-[-50%]">
                            <Image src={HomeImage} alt="Home" />
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}

// This is the recommended way for Next.js 9.3 or newer
export const getServerSideProps: GetServerSideProps = async (context) => {
    return {
        props: {
            csrfToken: await getCsrfToken(context),
        },
    };
};
