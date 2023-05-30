import { axios } from "@/config/axios";
import NextAuth from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";

const options = {
    providers: [
        CredentialsProvider({
            credentials: {
                username: { label: "Username", type: "text", placeholder: "jsmith" },
                password: { label: "Password", type: "password" },
            },

            // Set your own credentials provider options here
            // For example, you can use an API endpoint to validate credentials
            async authorize(credentials: any, req) {
                try {
                    const { data } = await axios.post("/users/login", {
                        email: credentials.email,
                        password: credentials.password,
                    });
                    console.log(data)
                    return data;
                } catch (err) {
                    return null;
                }
            },
        }),
    ],
    secret: process.env.JWT_SECRET,
    pages: {
        signIn: "/login",
    },
};

export default NextAuth(options);
