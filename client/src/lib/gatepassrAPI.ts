import { env } from '$env/dynamic/public'
console.log(env.PUBLIC_GATEPASSAPI_URL)
export const gatepassrAPI = env.PUBLIC_GATEPASSAPI_URL ?? "http://127.0.0.1:5000"

//"https://gatepassrapi.azurewebsites.net"
//"http://127.0.0.1:5000";