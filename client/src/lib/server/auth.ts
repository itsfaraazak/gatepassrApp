import { Lucia } from "lucia";
import { dev } from "$app/environment";
import { AZURE_AD_CLIENT_ID, AZURE_AD_CLIENT_SECRET, AZURE_AD_TENANT_ID, GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET } from "$env/static/private";

import { GitHub } from "arctic";

import { MicrosoftEntraId } from "arctic";

/* import { PostgresJsAdapter } from "@lucia-auth/adapter-postgresql";
import postgres from "postgres";

const sql = postgres();

const adapter = new PostgresJsAdapter(sql, {
	user: "auth_user",
	session: "user_session"
});
 */

import { PrismaAdapter } from "@lucia-auth/adapter-prisma";
import { PrismaClient } from "@prisma/client";

export let prisma = new PrismaClient();

const adapter = new PrismaAdapter(prisma.session, prisma.user);

export const lucia = new Lucia(adapter, {
	sessionCookie: {
		attributes: {
			// set to `true` when using HTTPS
			secure: !dev
		}
	},
    getUserAttributes: (attributes) => {
		return {
			// attributes has the type of DatabaseUserAttributes
			githubId: attributes.github_id,
			username: attributes.username,
			//email: attributes.email,
		};
    }
});

declare module "lucia" {
	interface Register {
		Lucia: typeof lucia;
        DatabaseUserAttributes: DatabaseUserAttributes;
	}
}

interface DatabaseUserAttributes {
	github_id: number;
	username: string;
}


export const github = new GitHub(
	GITHUB_CLIENT_ID,
	GITHUB_CLIENT_SECRET
);

export const entraID = new MicrosoftEntraId(
	AZURE_AD_TENANT_ID,
	AZURE_AD_CLIENT_ID,
	AZURE_AD_CLIENT_SECRET,
	"http://localhost:5173/login/microsoft/callback"
)