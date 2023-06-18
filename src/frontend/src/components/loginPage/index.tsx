import { useRouter } from "next/router";
import { signIn, getCsrfToken } from "next-auth/react";
import { toast } from "react-toastify";
import Head from "next/head";
import LoginForm from "../loginForm";
import Image from "next/image";
import HomeImage from "../../assets/home.png";

interface LoginPageProps {
  csrfToken: string;
}

const LoginPage: React.FC<LoginPageProps> = ({ csrfToken }) => {
  const router = useRouter();

  const onSubmit = async (data: any) => {
    try {
      const res = await signIn("credentials", {
        redirect: false,
        email: data.email,
        password: data.password,
        callbackUrl: `${window.location.origin}`,
      });

      if (res?.ok) {
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
            <h1 className="text-4xl mb-2 text-[#0D0958]">Olá, bem-vindo de volta!</h1>
            <h3 className="text-xl text-[#7A7C95] mb-4">É um prazer ter você aqui.</h3>
            <LoginForm csrfToken={csrfToken} onSubmit={onSubmit} />
          </div>
        </div>
        <div className="w-[50vw]">
          <div className="p-8 w-full h-full bg-login-texture bg-no-repeat bg-cover overflow-hidden rounded-3xl relative">
            <div className="absolute top-36 left-[50%] w-[60%] translate-x-[-50%] rounded-tl-4xl">
              <h1 className="text-white font-bold  text-4xl">
                Avaliações preliminares de espaços confiados em um só lugar
              </h1>
              <h5 className="text-white mt-4 text-xl">Coloque as suas credenciais para ter acesso ao sistema.</h5>
            </div>
            <div className="w-[70%] h-[30%] absolute top-[40%] left-[50%] translate-x-[-50%]">
              <Image src={HomeImage} alt="Home" />
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default LoginPage;