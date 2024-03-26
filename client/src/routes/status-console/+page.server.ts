import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { gatepassrAPI } from "$lib/gatepassrAPI";

export const load: PageServerLoad = async (event) => {

  const useremail = await event.locals.user_email ;
  const role_id = await event.locals.roleid;
 
  const fetchUserRequests = async()=> {
    const responseProfile = await fetch(gatepassrAPI +"/submit/userrequests", {
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
    requests: await fetchUserRequests(),
  };
}