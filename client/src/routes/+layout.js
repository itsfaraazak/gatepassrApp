export const prerender = true;
import { json } from '@sveltejs/kit';
export let _result = undefined
function _get_requests(){
    const result = fetch("http://127.0.0.1:5000/recieve/todaysrequests")
        .then( response => response.json() )
        .then( data => { _result = data } )
    return result
}