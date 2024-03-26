import { Google, OAuth2RequestError } from "arctic";
import { generateId } from "lucia";
import { github, lucia } from "$lib/server/auth";

import type { RequestEvent } from "@sveltejs/kit";

//import { PrismaClient } from '@prisma/client']

import { prisma } from "$lib/server/auth"


import { GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET } from "$env/static/private";
// const prisma = new PrismaClient()

const google = new Google(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, "http://localhost:5173/login/google/callback");

export async function GET(event: RequestEvent): Promise<Response> {
	const code = event.url.searchParams.get("code");
	const state = event.url.searchParams.get("state");

	const storedState = event.cookies.get("state") ?? null;
    const storedCodeVerifier = event.cookies.get("code_verifier") ?? null;


	if (!code || !storedState || !storedCodeVerifier || state !== storedState) {
		console.log("No code, state, storedState or mismatch. Invalid Request.")
		return new Response(null, {
			status: 400
		});
	}

	try {
        const tokens = await google.validateAuthorizationCode(code, storedCodeVerifier);
       // const githubUser = await google.refreshAccessToken(tokens.accessToken);


        const response = await fetch("https://openidconnect.googleapis.com/v1/userinfo", {
	        headers: {
		        Authorization: `Bearer ${tokens.accessToken}`
	        }
        });

        const googleUser = await response.json();
       console.log(googleUser)
/* 		const githubUserResponse = await fetch("https://api.github.com/user", {
			headers: {
				Authorization: `Bearer ${tokens.accessToken}`
			}
		});
		const githubUser: GitHubUser = await githubUserResponse.json();

		const githubUserResponseEmail = await fetch("https://api.github.com/user/emails", {
			headers: {
				Authorization: `Bearer ${tokens.accessToken}`
			}
		});
		const githubUserEmail: GitHubUser = await githubUserResponseEmail.json();
 */
		// Replace this with your own DB client.
		//const existingUser = await db.table("user").where("github_id", "=", githubUser.id).get();
        console.log("testimg =====");
		console.log(googleUser.sub);

        const existingUser = await prisma.user.findUnique({
            where : {
                provider_id: Number(googleUser.sub),
                //provider_name:"google",il.comelete 
                //email: googleUser.email,
            },
        });

        console.log(existingUser);
		if (existingUser) {
			const session = await lucia.createSession(existingUser.id, {});
			const sessionCookie = lucia.createSessionCookie(session.id);
			event.cookies.set(sessionCookie.name, sessionCookie.value, {
				path: ".",
				...sessionCookie.attributes
			});
		} else {
			const userId = 12345
			//generateId(15);

			// Replace this with your own DB client.
			/* await db.table("user").insert({
				id: userId,
				github_id: githubUser.id,
				username: githubUser.login
			}); */
        
			console.log(userId)

			await prisma.user.create({
				data: {
					id: String(userId),
                    provider_id: Number(googleUser.sub),
					provider_name: "google",
					username: googleUser.name,
					email: googleUser.email,
				}
			});

          /*  await prisma.oauth_account.create({
				data: {
					provider_id: "google",
					//github_id: 1234555,
					provider_user_id: googleUser.sub,
                    user_id: userId
					//username: 'Userrrrr',
					//email: googleUser.email,
				},
			})*/


			const session = await lucia.createSession(userId, {});
			const sessionCookie = lucia.createSessionCookie(session.id);
			event.cookies.set(sessionCookie.name, sessionCookie.value, {
				path: ".",
				...sessionCookie.attributes
			});
		}
		return new Response(null, {
			status: 302,
			headers: {
				Location: "/home"
			}
		});
	} catch (e) {
		// the specific error message depends on the provider
		if (e instanceof OAuth2RequestError) {
			// invalid code
			return new Response(null, {
				status: 400
			});
		}
		return new Response(null, {
			status: 500
		});
	}
}

interface GoogleUser {
	id: number;
	login: string;
    sub: string;
    email:string;
}