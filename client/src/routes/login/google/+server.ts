import { Google } from "arctic";
import { generateCodeVerifier, generateState } from "arctic";

import { GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET } from '$env/static/private'
import { redirect, type RequestEvent } from "@sveltejs/kit";

const google = new Google(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, "http://localhost:5173/login/google/callback");

export async function GET(event: RequestEvent): Promise<Response> {
	const state = generateState();
    const codeVerifier = generateCodeVerifier();
	const url = await google.createAuthorizationURL(state, codeVerifier, {
        scopes: ["profile", "email"]
    });
    
    event.cookies.set("state", state, {
	    secure: true, // set to false in localhost
	    path: "/",
	    httpOnly: true,
	    maxAge: 60 * 10 // 10 min
    });

    // store code verifier as cookie
    event.cookies.set("code_verifier", codeVerifier, {
	    secure: true, // set to false in localhost
	    path: "/",
	    httpOnly: true,
	    maxAge: 60 * 10 // 10 min
    });

	redirect(302, url.toString());
}
