<script>
  import { goto } from '$app/navigation';
  import { onMount } from 'svelte';
  import Breadcrumb from '$components/breadcrumb.svelte';
  import Table from '$components/table.svelte';
  import { gatepassrAPI } from "$lib/gatepassrAPI";
  import { base } from '$app/paths';
  import { page } from '$app/stores';


  // @ts-ignore
  /**
     * @type {never[]}
     */
  let requests= []
  //let testreq = _get_requests
  /**
     * @type {Response}
     */
  let return_status;
  export let data;
  requests = data.requests;
  console.log(requests);
  console.log("Testing locals");
  console.log(data.user)
  let useremail = $page?.data?.session?.user?.email;
  
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
            <title>Gatepassr Console</title>
        </head>
        <body class="h-full">
          <div class="min-h-full">
        <main>
            
          <div class="mx-4 mt-16 py-6 sm:mx-12">
            <div class="mx-4 my-2 lg:flex lg:items-center lg:justify-between">
            <Breadcrumb currentpage="Status Console"/>
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
              <div class="relative mx-4 mt-4 overflow-hidden text-gray-700 bg-white rounded-none bg-clip-border">

                  <div class="justify-between mb-1 flex-col">
                    <button type="button" on:click={addManualExit} class="inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">
                      Request Gatepass
                    </button>
                    </div>
              </div>
              <div class="px-1 overflow-auto">
                <!-- <Table req={requests} approveReq=""/> -->
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
                          Requested Exit Time
                        </p>
                      </th>
                      <th class="p-4 border-y border-blue-gray-100 bg-blue-gray-50/50">
                        <p class="block font-sans text-sm antialiased font-normal leading-none text-blue-gray-900 opacity-70">
                          Status
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
                            {r[4]}
                          </p>
                        </div>
                      </td>
                      <td class="p-4 border-b border-blue-gray-50">
                        <p class="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900">
                          {r[5]?.substring(0,16)}
                        </p>
                        <p class="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900 opacity-70">
                        {r[5]?.substring(16)}
                      </p>
                      </td>
                      <td class="p-4 border-b border-blue-gray-50">
                        <p class="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900">
                          
                          {#if r[6] !== null}
                          <span>Approved</span>
                          {:else}
                          <span>Pending</span>
                          {/if}

                        </p>
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