<script>
// @ts-nocheck

    /**
     * @type {never[]}
     */
     export let req = []
     export let approveReq
</script>

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
      -->{#if approveReq}
        <th class="p-4 border-y border-blue-gray-100 bg-blue-gray-50/50">
          <p class="block font-sans text-sm antialiased font-normal leading-none text-blue-gray-900 opacity-70">
            Actions
          </p>
        </th>
        {/if}
      </tr>
    </thead>
    <tbody>
      <!-- row -->

      {#each req as r}
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
      {#if approveReq}
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
      {/if}
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

          {#if r[6] == null}
          <form method="POST" action="?/approverequest">
            <input type="hidden" id="{r[7]}">
            <button name="btnapprove"
              class="relative h-10 w-full select-none rounded-lg text-center align-middle font-sans text-xs font-medium uppercase text-gray-900 transition-all hover:bg-gray-900/10 active:bg-gray-900/20 disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
              type="button" on:click|once ={approveReq(r[7])} id={r[7]}>
              <span>Approve</span>
          </button>
         </form>
          {:else}
            <button
              class="relative h-10 w-full select-none rounded-lg text-center align-middle font-sans text-xs font-medium uppercase text-gray-900 transition-all hover:bg-gray-900/10 active:bg-gray-900/20 disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
              type="button">
              
              <p>Reject</p>
            </button>
          {/if}

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
          
        </td>
      </tr>
      {/each}
      <!-- row end -->

  </table>