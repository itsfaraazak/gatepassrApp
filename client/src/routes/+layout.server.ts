export const prerender = true;
import type { LayoutServerLoad } from "./$types"

export const load = async (event) => {
	const session = await event.locals.getSession();

	return {
		session
	};
};
