import { authOptions } from "@/pages/api/auth/[...nextauth]";
import axiosPackage, { AxiosInstance } from "axios";
import { GetServerSidePropsContext, PreviewData } from "next";
import { getSession } from "next-auth/react";
import { getServerSession } from "next-auth";
import { ParsedUrlQuery } from "querystring";

interface Axios extends AxiosInstance {
    CancelToken?: any;
    isCancel?: any;
}

const axios: Axios = axiosPackage.create({
    // withCredentials: true,
    baseURL: process.env.NEXT_PUBLIC_APP_URL,
    headers: {
        common: {
            Accept: "application/json",
        },
    },
});

axios.interceptors.request.use(async (config) => {
    const session = await getSession();
    config.headers.Authorization = `Bearer ${session?.accessToken}`;
    return config;
});

// axios.CancelToken = axiosPackage.CancelToken;
// axios.isCancel = axiosPackage.isCancel;

const createServerSideAxiosInstance = async (ctx: GetServerSidePropsContext<ParsedUrlQuery, PreviewData>) => {
    const instance = axiosPackage.create();
    instance.defaults.baseURL = process.env.NEXT_PUBLIC_APP_URL;
    const session = await getServerSession(ctx.req, ctx.res, authOptions);

    if (session) {
        instance.defaults.headers.common.Authorization = `Bearer ${session.accessToken}`;
    }

    return instance;
};

export { axios, createServerSideAxiosInstance };
