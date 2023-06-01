import { axios } from "@/config/axios";
import NextAuth, { NextAuthOptions, Session } from "next-auth";
import { JWT } from "next-auth/jwt";
import CredentialsProvider from "next-auth/providers/credentials";

interface User {
    _id: {
        $oid: string;
    };
    email: string;
    password: string;
    token: string;
}

export const authOptions: NextAuthOptions = {
    providers: [
        CredentialsProvider({
            credentials: {
                username: { label: "Username", type: "text", placeholder: "jsmith" },
                password: { label: "Password", type: "password" },
            },

            async authorize(credentials: any, req) {
                try {
                    const { data } = await axios.post("/users/login", {
                        email: credentials.email,
                        password: credentials.password,
                    });
                    return data;
                } catch (err) {
                    return null;
                }
            },
        }),
    ],
    callbacks: {
        jwt({ token, user }) {
            if (user) {
                token.accessToken = user.access_token;
            }

            return token;
        },

        session({ session, token, user }) {
            // @ts-ignore
            session.accessToken = token.accessToken;
            return session;
        },
    },
    secret: process.env.JWT_SECRET,
};

export default NextAuth(authOptions);
