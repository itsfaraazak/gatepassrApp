<script lang="ts">
    import "../app.css"
    
    import { gatepassrAPI} from "$lib/gatepassrAPI";
    import { base } from  "$app/paths";
    import type { LayoutData } from './$types';
    import {signIn, signOut} from "@auth/sveltekit/client"
    import toast , { Toaster } from 'svelte-french-toast';
	  export let data: LayoutData;
    
    let useremail=""

    function toggleHamburgerMenu() {
      var element = document.getElementById("mobile-nav");
      element?.classList.toggle("hidden")
    }


/*     document.getElementsByClassName("sidebar-links a").click()
 */  
</script>


<Toaster />

<header class="absolute inset-x-0 top-0 z-50 safe-top safe-left safe-right">
    <!-- font -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap" rel="stylesheet">

    <!-- front end -->
    <nav class="flex items-center justify-between p-6 lg:px-8" aria-label="Global">
      <div class="flex lg:flex-1">
        <a href="#" class="-m-1.5 p-1.5">
          <span class="sr-only">Your Company</span>
          <img class="h-8 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="">
        </a>
      </div>
      <div class="flex lg:hidden">
        <button type="button" class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700" on:click={toggleHamburgerMenu}>
          <span class="sr-only">Open main menu</span>
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
          </svg>
        </button>
      </div>
      <div class="hidden pb-12  lg:flex lg:gap-x-12">
        <a href="{base}/status-console" data-sveltekit-preload-data class="text-sm font-semibold leading-6 text-gray-900">Home</a>
        <a href="{base}/request-a-gatepass"  data-sveltekit-preload-data class="text-sm font-semibold leading-6 text-gray-900">Request Gatepass</a>
        <a href="{base}/management-console" data-sveltekit-preload-data class="text-sm font-semibold leading-6 text-gray-900">Management Console</a>
        <a href="{base}/security-console" data-sveltekit-preload-data class="text-sm font-semibold leading-6 text-gray-900">Security Console</a>
        <a href="{base}/about-us" class="text-sm font-semibold leading-6 text-gray-900">About us</a>
      </div>
      <div class="hidden  px-1 lg:flex lg:flex-1 lg:justify-end">
          {#if data.session}
          <span>
            
              <strong>{data.session.user?.name ?? "User"}</strong><br/>
              <a href="{base}/profile" class="text-sm font-semibold leading-6 text-gray-900">Profile</a><br/>
              <a href="{base}/auth/signout" class="text-sm font-semibold leading-6 text-gray-900">Sign out</a>
              
             
          </span>
          {:else}
            <a href="{base}/auth/sign-in" class="text-sm font-semibold leading-6 text-gray-900">
              Log in 
              <span aria-hidden="true">&rarr;</span></a>
          {/if}
      </div>
      
    </nav>
    <!-- Mobile menu, show/hide based on menu open state -->
    <div class="hidden" id="mobile-nav" role="dialog" aria-modal="true">
       <!-- Background backdrop, show/hide based on slide-over state. -->
      <div class="fixed inset-0 z-50"></div>
      <div class="fixed inset-y-0 right-0 z-50 safe-top w-full overflow-y-auto bg-white sm:max-w-sm sm:ring-1 sm:ring-gray-900/10">
        <div class="flex items-center justify-between p-6 lg:px-8">
          <a href="{base}/" on:click={toggleHamburgerMenu} class="-m-1.5 p-1.5">
            <span class="sr-only">Your Company</span>
            <img class="h-8 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="">
          </a>
          <button type="button" on:click={toggleHamburgerMenu} class="-m-2.5 rounded-md p-2.5 text-gray-700">
            <span class="sr-only">Close menu</span>
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        <div class="mt-6 mx-4 flow-root">
          <div class="-my-6 divide-y divide-gray-500/10">
            <div class="space-y-2 py-6" id="sidebar-links">
              <a href="{base}/home" on:click={toggleHamburgerMenu} class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Home</a>
              <a href="{base}/request-a-gatepass" on:click={toggleHamburgerMenu} class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Request a Gatepass</a>
              <a href="{base}/management-console" on:click={toggleHamburgerMenu} class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Management Console</a>
              <a href="{base}/security-console" on:click={toggleHamburgerMenu} class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Security Console</a>
               </div>
            <div class="py-6">
              <span>{useremail}</span>
              {#if data.session}
              <div class="">
                  <strong>{data.session.user?.name ?? "User"}</strong>
                  <a href="{base}/profile" on:click={toggleHamburgerMenu} class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">
                    Profile</a>
           
                  <button on:click={() => signOut()} class="button -mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Sign out</button>
              </div>
              {:else}
                <a href="{base}/auth/sign-in" on:click={toggleHamburgerMenu} class="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">
                  Log in 
                <span aria-hidden="true">&rarr;</span></a>
                <a href="{base}/auth/sign-up" on:click={toggleHamburgerMenu} class="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Sign Up</a>

              {/if}
            </div>
          </div>
        </div>
      </div>
    </div>
</header>



<div role="status" class="invisible absolute left-2/4">
  <svg aria-hidden="true" class="w-10 h-10 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
      <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
  </svg>
  <span class="sr-only">Loading...</span>
</div>



<slot />

