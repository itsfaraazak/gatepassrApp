<script>
export let currentpage= undefined
</script>
<div class="mx-4 my-2 lg:flex lg:items-center lg:justify-between">
    <ol class="flex items-center whitespace-nowrap" aria-label="Breadcrumb">
      <li class="inline-flex items-center">
        <a class="flex items-center text-sm text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600 dark:focus:text-blue-500" href="/home">
          Home
        </a>
        {#if currentpage}
        <svg class="flex-shrink-0 mx-2 overflow-visible size-4 text-gray-400 dark:text-neutral-600" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
        {/if}
    </li>
      {#if currentpage}
      <li class="inline-flex items-center text-sm font-semibold text-gray-800 truncate dark:text-gray-500" aria-current="page">
        <span class="flex items-center text-sm text-gray-500 focus:outline-none" href="#">
            {currentpage}
        </span>
      </li>
      {/if}
    </ol>
</div>