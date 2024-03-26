export const prerender = true;
import type { LayoutServerLoad } from "./$types"
import type { Cookies } from '@sveltejs/kit';

export const load = async (event) => {
	const session = await event.locals.getSession();
    //createSession()
	return {
		user: user
	};
};
 */
// function createSession(cookies: Cookies) {

// 	const sessionID = crypto.randomUUID();

// 	cookies.set('session', JSON.stringify({ sessionID }), {

// 		path: '/',

// 		expires: new Date(Temporal.Now.plainDateTimeISO().add({ hours: 2 }).toString()),

// 		sameSite: 'lax',

// 		httpOnly: true

// 	});

// }

