
import { fail, redirect } from "@sveltejs/kit";
import { lucia } from "$lib/server/auth";

import type { Actions, PageServerLoad } from "./$types";


export const load: PageServerLoad = async (event) => {
/* 	console.log(event.locals.user)
	console.log(event.locals.session)
	console.log(event.locals.session)

 */
	if (!event.locals.user) redirect(302, "/login");

	return {
		username: event.locals.user.username
	};
};

export const actions: Actions = {
	default: async (event) => {
		if (!event.locals.session) {
			return fail(401);
		}
		await lucia.invalidateSession(event.locals.session.id);
		const sessionCookie = lucia.createBlankSessionCookie();
		event.cookies.set(sessionCookie.name, sessionCookie.value, {
			path: ".",
			...sessionCookie.attributes
		});
		redirect(302, "/login");
	}
};