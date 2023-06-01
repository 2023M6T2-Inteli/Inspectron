import axiosPackage, { AxiosInstance } from "axios";
import { getSession } from "next-auth/react";

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

axios.CancelToken = axiosPackage.CancelToken;
axios.isCancel = axiosPackage.isCancel;

export { axios };
