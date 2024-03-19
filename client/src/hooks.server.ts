import { SvelteKitAuth } from '@auth/sveltekit';
import type { Handle} from '@sveltejs/kit';
import { redirect } from '@sveltejs/kit';
import GitHub from '@auth/core/providers/github';
import Google from '@auth/core/providers/google';
import Auth from "@auth/core"
import AzureAd from "@auth/core/providers/azure-ad"
import { GITHUB_ID, GITHUB_SECRET,GOOGLE_CLIENT_ID,GOOGLE_CLIENT_SECRET, AZURE_AD_CLIENT_ID, AZURE_AD_CLIENT_SECRET, AZURE_AD_TENANT_ID} from '$env/static/private';


import { sequence } from '@sveltejs/kit/hooks';
let profiledata
let userdata:{
    role:""
}
export const { handle, signIn, signOut } = SvelteKitAuth({
	providers: [
		
		GitHub({ clientId: GITHUB_ID, clientSecret: GITHUB_SECRET }),
		Google({ clientId: GOOGLE_CLIENT_ID, 
			     clientSecret: GOOGLE_CLIENT_SECRET}),
		AzureAd({ clientId: AZURE_AD_CLIENT_ID, clientSecret: AZURE_AD_CLIENT_SECRET, tenantId: AZURE_AD_TENANT_ID, profile:profiledata}),
	],
	debug:true,
	trustHost:true,
});

function getrole(){
 return "admin"
}