<script>
// @ts-nocheck

import { redirect } from '@sveltejs/kit';
import { onMount } from 'svelte';
import { goto } from '$app/navigation';
import Table from '$components/table.svelte';
import Breadcrumb from '$components/breadcrumb.svelte';

import { gatepassrAPI } from "$lib/gatepassrAPI";
import { base } from '$app/paths';
import { page } from '$app/stores';

let user_email = $page?.data?.session?.user?.email
/**
 * @type {any[]}
 */
let requests = []
/**
 * @type {Response}
 */
let return_status;
let isauthorized= false;
function get_Requests()
{
  fetch(gatepassrAPI +"/recieve/pendingrequests")
        .then( response => response.json() )
        .then( data => { requests = data } )
}

onMount( async () => {
  get_Requests();
  await getRole();
});

function toggleHamburgerMenu() {
    var mobile_menu = document.getElementById("mobile-menu");
    mobile_menu?.classList.toggle("hidden");
    var btn_close_mobile_menu = document.getElementById("btn-svg-close-mobile-menu");
    btn_close_mobile_menu?.classList.toggle("hidden");
    btn_close_mobile_menu?.classList.toggle("block");
    var btn_close_mobile_menu = document.getElementById("btn-svg-open-mobile-menu");
    btn_close_mobile_menu?.classList.toggle("block");
    btn_close_mobile_menu?.classList.toggle("hidden");
}

function addManualRequest() {
    goto('/management-console/add-manual-request')
    //goto(base +'/request-a-gatepass')
}
function reloadPage() {
        const thisPage = window.location.pathname;
        console.log('goto ' + thisPage);
        goto('/').then(
            () => goto(thisPage)
        );
}
  // @ts-ignore
function approveRequest(request_id) {
  console.log(request_id);
  let response =  fetch(gatepassrAPI+"/submit/approverequest",{
    method: "POST", // *GET, POST, PUT, DELETE, etc.
    mode: "no-cors", // no-cors, *cors, same-origin
    headers: {
      "Content-Type": "text/plain"
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    // @ts-ignore
    Accept: "text/plain",
    body: request_id
  });

  response.then(data =>return_status=data)
  //return_status = (json)
  console.log(return_status)
  if (response.ok) {
      //const data =  response.json();
      console.log(response.data)
      
  } 
  else 
  {
      console.log('error: ', response.status, response.statusText);
      /* Handle the error returned by the HTTP request */
      // return {error: {status: response.status, statusText: response.statusText}};
  };
  reloadPage();
}
let admindata;
async function getRole(){
  await fetch(gatepassrAPI +"/submit/isauthorized", {
     method: "POST",
    //  mode: "no-cors",
     body: JSON.stringify({
         user_email: user_email,
     })
 })
 .then(response => response.json())
 .then(data => {admindata = data});

  console.log(admindata[0]);
}

</script>

<html lang="en-US" class="h-full bg-gray-100">
        <head>
            <meta charset="utf-8"/>
            <title>Gatepassr Management Console</title>
        </head>
        <body class="h-full">
          <div class="min-h-full">
        <main>
            
          <div class="mx-4 mt-16 py-6 sm:mx-12">
            <div class="mx-4 my-2 lg:flex lg:items-center lg:justify-between">
              <Breadcrumb currentpage="Management Console"/>
            </div>
            <!-- page header -->
            <div class="mx-4 mt-8 mb-6 lg:flex lg:items-center lg:justify-between">
              
              <div class="min-w-0 flex-1">
                <h2 class="text-3xl font-bold leading-7 text-gray-900 sm:truncate sm:text-3xl sm:tracking-tight">Pending Requests</h2>
              </div>
              <div class="mt-5 flex lg:ml-4 lg:mt-0">
                <span class="block">
                </span>
                        
              </div> 
            </div>
          
            <!-- page header end -->
            <!-- table -->
            <div class="mx-4 mt-4 mb-2 relative flex flex-col h-full text-gray-700 bg-white shadow-md rounded-xl ">
              <div class="relative mx-4 mt-4 overflow-hidden text-gray-700 bg-white rounded-none bg-clip-border">

                  <div class="justify-between mb-1 flex-col">
                    <button type="button" on:click={addManualRequest} class="inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">
                      Add record...
                    </button>
                    </div>
                
                <div class="flex flex-col items-center justify-between md:flex-row">
                </div>
              </div>
              <div class="px-1 overflow-auto">
               <Table req={requests} approveReq={approveRequest}></Table>
              </div>
              <div class="flex items-center justify-between p-4 border-t border-blue-gray-50">
                <p class="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900">
                  Page 1 of 10
                </p>
                <div class="flex gap-2">
                  <button
                    class="inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
                    type="button">
                    Previous
                  </button>
                  <button
                    class="inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
                    type="button">
                    Next
                  </button>
                </div>
              </div>
            </div>
            <!-- table -->
          </div>
        </main>
      </div>
        </body>
    </html>