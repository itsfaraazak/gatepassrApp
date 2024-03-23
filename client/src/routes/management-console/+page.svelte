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
export let data;
const {requests} = data;
console.log(requests)
//let requests = []
/**
 * @type {Response}
 */
let return_status;
let isauthorized= false;

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
// let admindata;
// async function getRole(){
//   await fetch(gatepassrAPI +"/submit/isauthorized", {
//      method: "POST",
//     //  mode: "no-cors",
//      body: JSON.stringify({
//          user_email: user_email,
//      })
//  })
//  .then(response => response.json())
//  .then(data => {admindata = data});

//   console.log(admindata[0]);
// }

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
               <!-- <Table req={requests} approveReq={approveRequest}></Table> -->
               <table class="w-full mt-4 text-left table-auto min-w-max">
                <thead>
                  <tr>
                    <th class="p-4 border-y border-blue-gray-100 bg-blue-gray-50/50">
                      <p class="block font-sans text-sm antialiased font-normal leading-none text-blue-gray-900 opacity-70">
                        Student
                      </p>
                    </th>
                    <th class="p-4 border-y border-blue-gray-100 bg-blue-gray-50/50">
                      <p class="block font-sans text-sm antialiased font-normal leading-none text-blue-gray-900 opacity-70">
                        Grade
                      </p>
                    </th>
                    <th class="p-4 border-y border-blue-gray-100 bg-blue-gray-50/50">
                      <p class="block font-sans text-sm antialiased font-normal leading-none text-blue-gray-900 opacity-70">
                        Status
                      </p>
                    </th>
                    <th class="p-4 border-y border-blue-gray-100 bg-blue-gray-50/50">
                      <p class="block font-sans text-sm antialiased font-normal leading-none text-blue-gray-900 opacity-70">
                        Requested Exit Time
                      </p>
                    </th>
                    <!--
                    <th class="p-4 border-y border-blue-gray-100 bg-blue-gray-50/50">
                      <p class="block font-sans text-sm antialiased font-normal leading-none text-blue-gray-900 opacity-70">
                        Type
                      </p>
                    </th>
                  -->
                    <th class="p-4 border-y border-blue-gray-100 bg-blue-gray-50/50">
                      <p class="block font-sans text-sm antialiased font-normal leading-none text-blue-gray-900 opacity-70">
                        Actions
                      </p>
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <!-- row -->
            
                  {#each requests as r}
                  <tr>
                    <td class="p-4 border-b border-blue-gray-50">
                      <div class="flex items-center gap-3">
                        <img src="https://demos.creative-tim.com/test/corporate-ui-dashboard/assets/img/team-3.jpg"
                          alt={r[0]} class="relative inline-block h-9 w-9 !rounded-full object-cover object-center" />
                        <div class="flex flex-col">
                          <p class="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900">
                            {r[0]}
                          </p>
                          <p
                            class="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900 opacity-70">
                            {r[1]}
                          </p>
                        </div>
                      </div>
                    </td>
                    <td class="p-4 border-b border-blue-gray-50">
                      <div class="flex flex-col">
                        <p class="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900">
                          {r[2]}
                        </p>
                        <p
                          class="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900 opacity-70">
                          {r[5]}
                        </p>
                      </div>
                    </td>
                    <!--
                    <td class="p-4 border-b border-blue-gray-50">
                      <div class="w-max">
                        <div
                          class="relative grid items-center px-2 py-1 font-sans text-xs font-bold text-green-900 uppercase rounded-md select-none whitespace-nowrap bg-green-500/20">
                          <span class="">Approved</span>
                        </div>
                      </div>
                    </td>
                  -->
                  
                    <td class="p-4 border-b border-blue-gray-50">
                      <div class="w-max">
                        {#if r[6] == null}
                          <div 
                          class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 relative grid items-center px-2 py-1 font-sans text-xs font-bold uppercase rounded-md select-none whitespace-nowrap bg-blue-gray-500/20 text-blue-gray-900">
                          <span class="status">Pending</span>
                        </div>
                        {:else}
                          <div
                          class="relative grid items-center px-2 py-1 font-sans text-xs font-bold text-green-900 uppercase rounded-md select-none whitespace-nowrap bg-green-500/20">
                          <span class="status">Approved</span>
                         </div>
                        {/if}
                      </div>
                    </td>
                  
                    <td class="p-4 border-b border-blue-gray-50">
                      <p class="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900">
                        {r[4].substring(0,16)}
                      </p>
                      <p class="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900 opacity-70">
                      {r[4].substring(16)}
                    </p>
                    </td>
                    <!--
                    <td class="p-4 border-b border-blue-gray-50">
                      <p class="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900">
                        {r[5]}
                      </p>
                    </td>
                  -->
                    
                    <td class="p-4 border-b border-blue-gray-50">
                     <form method="POST">
                      <input type="hidden" name="" id ={r[7]}/>
                      {#if r[6] == null}
                        <button name="btnapprove"
                          class="relative h-10 w-full select-none rounded-lg text-center align-middle font-sans text-xs font-medium uppercase text-gray-900 transition-all hover:bg-gray-900/10 active:bg-gray-900/20 disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
                          type="button"  id={r[7]}>
                          <span>Approve</span>
                      </button>
                      {:else}
                        <button
                          class="relative h-10 w-full select-none rounded-lg text-center align-middle font-sans text-xs font-medium uppercase text-gray-900 transition-all hover:bg-gray-900/10 active:bg-gray-900/20 disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
                          type="button">
                          
                          <p>Reject</p>
                        </button>
                      {/if}
                    </form>
                    </td>
                  </tr>
                  {/each}
                  <!-- row end -->
            
            </table>
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