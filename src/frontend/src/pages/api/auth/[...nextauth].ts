import { axios } from "@/config/axios";
import NextAuth, { Session } from "next-auth";
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

export default NextAuth({
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
                    return data;
                } catch (err) {
                    return null;
                }
            },
        }),
    ],
    callbacks: {
        jwt({ token, account, user, session }) {
            if (user) {
                token.accessToken = user.access_token;
            }

            return token;
        },

        session({ session, token, user }) {
            session.accessToken = token.accessToken;
            return session;
        },
    },
    secret: process.env.JWT_SECRET,
});
