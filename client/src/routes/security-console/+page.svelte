<script>
  import { goto } from '$app/navigation';
  import { onMount } from 'svelte';
  /**
   * @type {any[]}
   */
  let requests = []
  /**
     * @type {Response}
     */
  let return_status;
  onMount( async () => {
      fetch("http://127.0.0.1:5000/recieve/todaysrequests")
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
    goto('/security-console/add-manual-exit')
  }

    
      
      function approveRequest(request_id) {
          console.log(request_id);
          /*
          const bodydata = {
              request_id: request_id,
              name: request_id,
              email: "abc@awesome.com"
            };
          request_id = 1
          console.log(JSON.stringify(bodydata));
          const updateData = async () => {
            const response = await fetch('localhost:5000/submit/approverequest', {
                method: 'GET',
                headers: {
                  'Content-Type': "text/html"
                },
                body: request_id  // the variable dataToSend can be a 'string' or an {object} that comes from somewhere else in our application
            });
          if (response.ok) {
              const data = await response.json();
              console.log(data)
              return data;
          } 
          else 
          {
              console.log('error: ', response.status, response.statusText);
              /* Handle the error returned by the HTTP request */
             // return {error: {status: response.status, statusText: response.statusText}};
         // };
       // };
        
          let response =  fetch("http://127.0.0.1:5000/submit/approverequest",{
            method: "POST", // *GET, POST, PUT, DELETE, etc.
            mode: "no-cors", // no-cors, *cors, same-origin
            //cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
            //credentials: "same-origin", // include, *same-origin, omit
            headers: {
              "Content-Type": "text/plain",
              // 'Content-Type': 'application/x-www-form-urlencoded',
            },
            Accept: "text/plain",
            //redirect: "follow", // manual, *follow, error
            //referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
            //body: '{"request": "'+ request_id +'"}'
            body: request_id
          });
    
          response.then(data =>return_status=data)
              //return_status = (json)
          console.log(return_status)
          if (response.ok) {
              //const data =  response.json();
              console.log(response.data)
              //return data;
          } 
          else 
          {
              console.log('error: ', response.status, response.statusText);
              /* Handle the error returned by the HTTP request */
             // return {error: {status: response.status, statusText: response.statusText}};
          };
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
              <ol class="flex items-center whitespace-nowrap" aria-label="Breadcrumb">
                <li class="inline-flex items-center">
                  <a class="flex items-center text-sm text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600 dark:focus:text-blue-500" href="#">
                    Exit Registry
                  </a>
                  <svg class="flex-shrink-0 mx-2 overflow-visible size-4 text-gray-400 dark:text-neutral-600" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
                </li>
                <li class="inline-flex items-center">
                  <a class="flex items-center text-sm text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600 dark:focus:text-blue-500" href="#">
                    App Center
                    <svg class="flex-shrink-0 mx-2 overflow-visible size-4 text-gray-400 dark:text-neutral-600" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
                  </a>
                </li>
                <li class="inline-flex items-center text-sm font-semibold text-gray-800 truncate dark:text-gray-200" aria-current="page">
                  Application
                </li>
              </ol>
            </div>
            <!-- page header -->
            <div class="mx-4 mt-8 mb-6 lg:flex lg:items-center lg:justify-between">
              
              <div class="min-w-0 flex-1">
                <h2 class="text-3xl font-bold leading-7 text-gray-900 sm:truncate sm:text-3xl sm:tracking-tight">Today's Exit Register</h2>
              </div>
              <div class="mt-5 flex lg:ml-4 lg:mt-0">
                <span class="block">
                </span>
                        
                <!-- Dropdown 
                <div class="relative ml-3 sm:hidden">
                  <button type="button" class="inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:ring-gray-400" id="mobile-menu-button" aria-expanded="false" aria-haspopup="true">
                    More
                    <svg class="-mr-1 ml-1.5 h-5 w-5 text-gray-400" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                      <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd" />
                    </svg>
                  </button>
            
                  
                    Dropdown menu, show/hide based on menu state.
            
                    Entering: "transition ease-out duration-200"
                      From: "transform opacity-0 scale-95"
                      To: "transform opacity-100 scale-100"
                    Leaving: "transition ease-in duration-75"
                      From: "transform opacity-100 scale-100"
                      To: "transform opacity-0 scale-95"
                  
                  <div class="absolute right-0 z-10 -mr-1 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none" role="menu" aria-orientation="vertical" aria-labelledby="mobile-menu-button" tabindex="-1">
                     Active: "bg-gray-100", Not Active: ""
                    <a href="#" class="block px-4 py-2 text-sm text-gray-700" role="menuitem" tabindex="-1" id="mobile-menu-item-0">Edit</a>
                    <a href="#" class="block px-4 py-2 text-sm text-gray-700" role="menuitem" tabindex="-1" id="mobile-menu-item-1">View</a>
                  </div>
                </div> -->
              </div> 
            </div>
          
            <!-- page header end -->
            <!-- table -->
            <div class="mx-4 mt-4 mb-2 relative flex flex-col h-full text-gray-700 bg-white shadow-md rounded-xl ">
              <div class="relative mx-4 mt-4 overflow-hidden text-gray-700 bg-white rounded-none bg-clip-border">

                  <div class="justify-between mb-1 flex-col">
                    <button type="button" on:click={addManualExit} class="inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">
                      Add record...
                    </button>
                    </div>
                
                <div class="flex flex-col items-center justify-between md:flex-row">
                  <!-- <div class="block w-full overflow-hidden md:w-max">
                    <nav>
                      <ul role="tablist" class="relative flex flex-row p-1 rounded-lg bg-blue-gray-50 bg-opacity-60">
                        <li role="tab"
                          class="relative flex items-center justify-center w-full h-full px-2 py-1 font-sans text-base antialiased font-normal leading-relaxed text-center bg-transparent cursor-pointer select-none text-blue-gray-900"
                          data-value="all">
                          <div class="z-20 text-inherit">
                            &nbsp;&nbsp;All&nbsp;&nbsp;
                          </div>
                          <div class="absolute inset-0 z-10 h-full bg-white rounded-md shadow"></div>
                        </li>
                        <li role="tab"
                          class="relative flex items-center justify-center w-full h-full px-2 py-1 font-sans text-base antialiased font-normal leading-relaxed text-center bg-transparent cursor-pointer select-none text-blue-gray-900"
                          data-value="monitored">
                          <div class="z-20 text-inherit">
                            &nbsp;&nbsp;Monitored&nbsp;&nbsp;
                          </div>
                        </li>
                        <li role="tab"
                          class="relative flex items-center justify-center w-full h-full px-2 py-1 font-sans text-base antialiased font-normal leading-relaxed text-center bg-transparent cursor-pointer select-none text-blue-gray-900"
                          data-value="unmonitored">
                          <div class="z-20 text-inherit">
                            &nbsp;&nbsp;Unmonitored&nbsp;&nbsp;
                          </div>
                        </li>
                      </ul>
                    </nav>
                  </div> -->
                  <!-- <div class="w-full md:w-72">
                     <div class="relative h-10 w-full min-w-[200px]">
                      <div class="absolute grid w-5 h-5 top-2/4 right-3 -translate-y-2/4 place-items-center text-blue-gray-500">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                          stroke="currentColor" aria-hidden="true" class="w-5 h-5">
                          <path stroke-linecap="round" stroke-linejoin="round"
                            d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"></path>
                        </svg>
                      </div>
                      <input
                        name="search"
                        class="peer h-full w-full border border-blue-gray-200 border-t-transparent bg-transparent !pr-9     inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
                        placeholder="Search for a student..." />
                      <label
                        for="search"
                        class="before:content[' '] after:content[' '] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none !overflow-visible truncate text-[11px] font-normal leading-tight text-gray-500 transition-all before:pointer-events-none before:mt-[6.5px] before:mr-1 before:box-border before:block before:h-1.5 before:w-2.5 before:rounded-tl-md before:border-t before:border-l before:border-blue-gray-200 before:transition-all after:pointer-events-none after:mt-[6.5px] after:ml-1 after:box-border after:block after:h-1.5 after:w-2.5 after:flex-grow after:rounded-tr-md after:border-t after:border-r after:border-blue-gray-200 after:transition-all peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[3.75] peer-placeholder-shown:text-blue-gray-500 peer-placeholder-shown:before:border-transparent peer-placeholder-shown:after:border-transparent peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-gray-900 peer-focus:before:border-t-2 peer-focus:before:border-l-2 peer-focus:before:!border-gray-900 peer-focus:after:border-t-2 peer-focus:after:border-r-2 peer-focus:after:!border-gray-900 peer-disabled:text-transparent peer-disabled:before:border-transparent peer-disabled:after:border-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500">
                        Search
                      </label>
                    </div>
                  </div> -->
                </div>
              </div>
              <div class="px-1 overflow-auto">
                <table class="w-full mt-4 text-left table-auto min-w-max">
                  <thead>
                    <tr>
                      <th class="p-4 border-y border-blue-gray-100 bg-blue-gray-50/50">
                        <p class="block font-sans text-sm antialiased font-normal leading-none text-blue-gray-900 opacity-70">
                          Student
                        </p>
                      </th>
                      <!-- <th class="p-4 border-y border-blue-gray-100 bg-blue-gray-50/50">
                        <p class="block font-sans text-sm antialiased font-normal leading-none text-blue-gray-900 opacity-70">
                          Grade
                        </p>
                      </th> -->
                      
                      <th class="p-4 border-y border-blue-gray-100 bg-blue-gray-50/50">
                        <p class="block font-sans text-sm antialiased font-normal leading-none text-blue-gray-900 opacity-70">
                          Status
                        </p>
                      </th>
                    
                      <th class="p-4 border-y border-blue-gray-100 bg-blue-gray-50/50">
                        <p class="block font-sans text-sm antialiased font-normal leading-none text-blue-gray-900 opacity-70">
                            Exit Time
                        </p>
                      </th>
                      <!--
                      <th class="p-4 border-y border-blue-gray-100 bg-blue-gray-50/50">
                        <p class="block font-sans text-sm antialiased font-normal leading-none text-blue-gray-900 opacity-70">
                          Type
                        </p>
                      </th>
                                        -->
                    </tr>
                  </thead>
                  <tbody>
                    <!-- row -->
    
                    {#each requests as r}
                    <tr>
                      <td class="p-4 border-b border-blue-gray-50">
                        <div class="flex items-center gap-3">
                          <div class="flex flex-col">
                            <p class="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900">
                              {r[0]}
                            </p>
                            <p
                            class="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900 opacity-70">
                            Grade {r[1]}
                            </p>
                          </div>
                        </div>
                      <!-- </td>
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
                      </td> -->
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
                    <!-- status -->
                      <td class="p-4 border-b border-blue-gray-50">
                        <div class="w-max">
                          {#if r[2] == null}
                            <div
                            class="relative grid items-center px-2 py-1 font-sans text-xs font-bold text-red-900 uppercase rounded-md select-none whitespace-nowrap bg-red-500/20">
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
                          {r[3].substring(0,16)}
                        </p>
                        <p class="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900 opacity-70">
                        {r[3].substring(16)}
                      </p>
                      </td>
                      <!--
                      <td class="p-4 border-b border-blue-gray-50">
                        <p class="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900">
                          {r[5]}
                        </p>
                      </td>
                    -->
    
                          <!--
                          <span class="absolute transform -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"
                              class="w-4 h-4">
                              <path
                                d="M21.731 2.269a2.625 2.625 0 00-3.712 0l-1.157 1.157 3.712 3.712 1.157-1.157a2.625 2.625 0 000-3.712zM19.513 8.199l-3.712-3.712-12.15 12.15a5.25 5.25 0 00-1.32 2.214l-.8 2.685a.75.75 0 00.933.933l2.685-.8a5.25 5.25 0 002.214-1.32L19.513 8.2z">
                              </path>
                            </svg>
                          </span>
                        -->
                        
                      
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