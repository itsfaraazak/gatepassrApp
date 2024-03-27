import { gatepassrAPI } from "$lib/gatepassrAPI"

let data = [];

const fetchRequests = async()=> {
    const requestsRes = await fetch(gatepassrAPI +"/recieve/fancy")
    const requestsdata =  await requestsRes.json();
    return requestsdata;
    }
      
export default data = await fetchRequests()
