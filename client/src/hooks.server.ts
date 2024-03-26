import { lucia } from "$lib/server/auth";
import type { Handle } from "@sveltejs/kit";

export const handle: Handle = async ({ event, resolve }) => {
	event.locals.user_email = "itsyasmeenkhan@gmail.com";
	event.locals.roleid ="1";
	return resolve(event);
};
