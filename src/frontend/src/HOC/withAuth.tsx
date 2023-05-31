import { GetServerSideProps, NextPageContext } from "next";
import { getSession } from "next-auth/react";

const withAuth = (WrappedComponent: any) => {
    const Wrapper = ({ session, ...props }: any) => {
        if (!session) {
            return null; // or handle the unauthorized state however you prefer
        }

        return <WrappedComponent session={session} {...props} />;
    };

    return Wrapper;
};

export const getServerSideProps = async (context: NextPageContext) => {
    const session = await getSession(context);
    if (!session) {
        return {
            redirect: {
                destination: "/",
                permanent: false,
            },
        };
    }

    return {
        props: { session },
    };
};

export default withAuth;
