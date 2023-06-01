import NextAuth from "next-auth";

declare module "next-auth" {
    /**
     * Returned by `useSession`, `getSession` and received as a prop on the `SessionProvider` React Context
     */
    interface Session {
        accessToken?: string;
    }

    interface User {
        access_token?: string;
    }

    interface JWT {
      access_token?: string;
    }
}
