import { redirect } from '@sveltejs/kit';
import type { PageServerLoad ,Actions} from './$types';
import { gatepassrAPI } from "$lib/gatepassrAPI";

export const load: PageServerLoad = async (event) => {

  const useremail = await event.locals.user_email ;
  const role_id = await event.locals.roleid;
  return {
    user_email: useremail,
    role_id:event.locals.roleid,
  };
}

// export const actions ={
//   submitprofile: async ({request, fetch})=>{
//     console.log("action triggered")
//     const formData = await request.formData()
//     console.log(formData)
//     let response =  fetch(gatepassrAPI+"/submit/profiledata",{
//       method: "POST", // *GET, POST, PUT, DELETE, etc.
//       body: JSON.stringify(formData)
//     });
//     let res = response.then(data=>data.json());
//   return {success: true}
// }
// }
