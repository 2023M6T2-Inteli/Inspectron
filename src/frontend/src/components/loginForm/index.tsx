import { Lock, AtSign } from "lucide-react";
import Input from "@/components/input";
import Button, { ButtonTypes } from "@/components/button";
import { useForm } from "react-hook-form";
import * as yup from "yup";
import { yupResolver } from "@hookform/resolvers/yup";

const schema = yup.object({
  email: yup.string().required("Esse campo é obrigatório."),
  password: yup.string().required("Esse campo é obrigatório."),
});

interface LoginFormProps {
  csrfToken: string;
  onSubmit: (data: any) => void;
}

const LoginForm: React.FC<LoginFormProps> = ({ csrfToken, onSubmit }) => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: yupResolver(schema),
  });

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col gap-6">
      <input {...register("csrfToken")} type="hidden" defaultValue={csrfToken} />

      <Input
        register={register("email")}
        label="Email"
        Icon={AtSign}
        error={errors.email?.message as string}
        placeholder="john@gmail.com"
      />
      <Input
        register={register("password")}
        label="Senha"
        Icon={Lock}
        error={errors.password?.message as string}
        placeholder="8+ caracteres obrigatórios"
        type="password"
      />
      <Button buttonType={ButtonTypes.primary}>LOGIN</Button>
    </form>
  );
};

export default LoginForm;