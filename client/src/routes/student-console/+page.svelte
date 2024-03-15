<script>
// @ts-nocheck

  import { goto } from '$app/navigation';
  import { onMount } from 'svelte';
  import Breadcrumb from '$components/breadcrumb.svelte';
  import Table from '$components/table.svelte';
  import { gatepassrAPI } from "$lib/gatepassrAPI";
  import { base } from '$app/paths';

 // import { _get_requests } from '../+layout';
  /**
   * @type {any[]}
   */
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

  function addManualExit() {
    goto(base +'/request-a-gatepass')
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
              <Breadcrumb currentpage="Security Console"/>
            </div>
            <!-- page header -->
            <div class="mx-4 mt-8 mb-6 lg:flex lg:items-center lg:justify-between">
              
              <div class="min-w-0 flex-1">
                <h2 class="text-3xl font-bold leading-7 text-gray-900 sm:truncate sm:text-3xl sm:tracking-tight">My Gatepasses</h2>
              </div>
              <div class="mt-5 flex lg:ml-4 lg:mt-0">
                <span class="block">
                </span>
                        
              </div> 
            </div>
          
            <!-- page header end -->
            <!-- table -->
            <div class="mx-4 mt-4 mb-2 relative flex flex-col h-full text-gray-700 bg-white shadow-md rounded-xl ">

              <div class="px-1 overflow-auto">
                <Table requests={requests} ></Table>
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