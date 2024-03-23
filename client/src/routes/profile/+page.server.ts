import { redirect } from '@sveltejs/kit';
import type { PageServerLoad ,Actions} from './$types';
import { gatepassrAPI } from "$lib/gatepassrAPI";
//import type { Actions } from './$types';
export const load: PageServerLoad = async (event) => {
  const session = await event.locals.auth();
  if (!session?.user) throw redirect(303, '/auth/sign-in');
  return {};
};

export const actions ={
  submitprofile: async ({request, fetch})=>{
    console.log("action triggered")
    const formData = await request.formData()
    console.log(formData)
    let response =  fetch(gatepassrAPI+"/submit/profiledata",{
      method: "POST", // *GET, POST, PUT, DELETE, etc.
      body: JSON.stringify(formData)
    });
    let res = response.then(data=>data.json());
  return {success: true}
}
}
