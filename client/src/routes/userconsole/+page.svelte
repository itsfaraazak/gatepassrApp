<script>
// @ts-nocheck
  import { gatepassrAPI } from "$lib/gatepassrAPI";
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  import { base } from '$app/paths';

  import Breadcrumb from '$components/breadcrumb.svelte';
  import Table from '$components/table.svelte';
  let requests = []
  
  //let testreq = _get_requests
  /**
     * @type {Response}
     */
  let return_status;
  onMount( async () => {
      fetch(gatepassrAPI +"/recieve/todaysrequests")
          .then( response => response.json() )
          .then( data => { requests = data } )
  });
  function addManualRequest() {
    // goto('/management-console/add-manual-request')
    goto(base +'/request-a-gatepass')
}
</script>
<html lang="en-US" class="h-full bg-gray-100">
        <head>
            <meta charset="utf-8"/>
            <title>Gatepassr user Console</title>
        </head>
        <body class="h-full">
          <div class="min-h-full">
        
            
            <div class="mx-4 mt-16 py-6 sm:mx-12">
              <div class="mx-4 my-2 lg:flex lg:items-center lg:justify-between">
                <Breadcrumb currentpage="User Console"/>
              </div>
            </div>
          
            <!-- page header end -->
            <!-- table -->
            <div class="mx-4 mt-4 mb-2 relative flex flex-col h-full text-gray-700 bg-white shadow-md rounded-xl ">
              <div class="relative mx-4 mt-4 overflow-hidden text-gray-700 bg-white rounded-none bg-clip-border">

                  <div class="justify-between mb-1 flex-col">
                    <button type="button" on:click={addManualRequest} class="inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">
                      Request Gatepass
                    </button>
                    </div>
                
                <div class="flex flex-col items-center justify-between md:flex-row">
                </div>
              </div>
              <div class="px-1 overflow-auto">
               <Table req={requests} ></Table>
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
       
     
    </body>
  </html>