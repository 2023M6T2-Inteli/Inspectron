import { GetServerSideProps, GetServerSidePropsContext, NextPageContext, PreviewData } from "next";
import { getSession } from "next-auth/react";
import { ParsedUrlQuery } from "querystring";

const returnConst = {
    redirect: {
        destination: "/",
        permanent: false,
    },
};

export const withAuth = async (
    ctx: GetServerSidePropsContext<ParsedUrlQuery, PreviewData>,
    getServerSidePropsFunc?: GetServerSideProps
) => {
    const session = await getSession(ctx);

    if (!session) {
        return returnConst;
    }

    // Se a sessão existir, então chame a função getServerSideProps da página.
    if (getServerSidePropsFunc) {
        try {
            const wrappedProps: any = await getServerSidePropsFunc(ctx);
            
            // Retorne os props recebidos da função getServerSideProps da página.
            return {
                props: {
                    ...wrappedProps.props,
                    session,
                },
            };
        } catch (err) {
            console.log(err);
            return returnConst;
        }
    }

    // Se não existir uma função getServerSideProps para a página, apenas retorne a sessão.
    return {
        props: {
            session,
        },
    };
};
