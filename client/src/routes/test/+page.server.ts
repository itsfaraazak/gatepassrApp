export const load = async (event) => {
    const user = await event.locals.user;
     //createSession()
     return {
         user: user
     };
 };