import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { gatepassrAPI } from "$lib/gatepassrAPI";
//export const prerender = false;
export const load: PageServerLoad = async (event) => {

  const useremail = await event.locals.user_email ;
  const role_id = await event.locals.roleid;
 
  const fetchProfile = async()=> {
    const responseProfile = await fetch(gatepassrAPI +"/submit/profile", {
        method: "POST",
        body: JSON.stringify({
            user_email: event.locals.user_email
        }),
    })
    const requestsdataProfile =  await responseProfile.json()
    return requestsdataProfile;
    }

  return {
    user_email: useremail,
    role_id:event.locals.roleid,
    profile: await fetchProfile(),
  };
}