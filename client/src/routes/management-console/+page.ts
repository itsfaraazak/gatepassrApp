import {redirect } from '@sveltejs/kit';
import type { PageServerLoad, Actions } from './$types';
import { gatepassrAPI } from "$lib/gatepassrAPI";
/** @type {import('./$types').Actions} */

export const load = async ({fetch}) => {
  // const session = await event.locals.auth();
  // if (!session?.user) throw redirect(303, '/auth/sign-in');

  const fetchRequests = async()=> {
    const requestsRes = await fetch(gatepassrAPI +"/recieve/pendingrequests")
    const requestsdata =  await requestsRes.json();
    return requestsdata;
  }
  
  return {
    requests: await fetchRequests()
  };
};

// export const actions = {
//   approveRequest: async({request }) => {
//         const formData = await request.formData();
//         const id = formData.get('id');
//         console.log(id)
      
//   return { success: true };
//   }
// } satisfies Actions;

