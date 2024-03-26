import { redirect } from "@sveltejs/kit";
import { generateCodeVerifier, generateState } from "arctic";
import { entraID } from "$lib/server/auth";

import type { RequestEvent } from "@sveltejs/kit";

export async function GET(event: RequestEvent): Promise<Response> {
	const state = generateState();
    const codeVerifier = generateCodeVerifier();

	const url = await entraID.createAuthorizationURL(state, codeVerifier, {
        scopes: ["profile", "email"]
    });

	event.cookies.set("entraid_oauth_state", state, {
		path: "/",
		secure: import.meta.env.PROD,
		httpOnly: true,
		maxAge: 60 * 10,
		sameSite: "lax"
	});

    // store code verifier as cookie
    event.cookies.set("entraid_oauth_code_verifier", codeVerifier, {
        path: "/",
	    secure: import.meta.env.PROD,
	    httpOnly: true,
	    maxAge: 60 * 10, // 10 min
        sameSite: "lax"
    });

	redirect(302, url.toString());
}