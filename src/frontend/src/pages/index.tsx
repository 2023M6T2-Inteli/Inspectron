import { GetServerSideProps } from "next";
import { getCsrfToken } from "next-auth/react";
import LoginPage from "../components/loginPage";

interface LoginProps {
  csrfToken: string;
}

const Login: React.FC<LoginProps> = ({ csrfToken }) => {
  return <LoginPage csrfToken={csrfToken} />;
};

export const getServerSideProps: GetServerSideProps = async (context) => {
  return {
    props: {
      csrfToken: await getCsrfToken(context),
    },
  };
};

export default Login;