<script lang="ts">
    import "../app.css"
    
    import { gatepassrAPI} from "$lib/gatepassrAPI";
    import { base } from  "$app/paths";
    import type { LayoutData } from './$types';
    import {signIn, signOut} from "@auth/sveltekit/client"
	
	  export let data: LayoutData;
    console.log(data)

    let useremail=""

    function toggleHamburgerMenu() {
      var element = document.getElementById("mobile-nav");
      element?.classList.toggle("hidden")
    }


/*     document.getElementsByClassName("sidebar-links a").click()
 */  
</script>




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
<!--           {#if data?.username}
          <span>
            
              <strong>{data?.username ?? "User"}</strong><br/>
              <a href="{base}/profile" class="text-sm font-semibold leading-6 text-gray-900">Profile</a><br/>
              <a href="{base}/auth/signout" class="text-sm font-semibold leading-6 text-gray-900">Sign out</a>
              
             
          </span>
 -->     
            <a href="{base}/login" class="text-sm font-semibold leading-6 text-gray-900">
              Log in 
              <span aria-hidden="true">&rarr;</span></a>
              <a href="{base}/protected" class="text-sm font-semibold leading-6 text-gray-900">
                Sign out
                <span aria-hidden="true">&rarr;</span></a>
  
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
             
              <!-- <div class="">
                  <strong>{data?.username ?? "User"}</strong>
                  <a href="{base}/profile" on:click={toggleHamburgerMenu} class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">
                    Profile</a>
           
                  <button on:click={() => signOut()} class="button -mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Sign out</button>
              </div> -->
                <a href="{base}/login" on:click={toggleHamburgerMenu} class="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">
                  Log in 
                <span aria-hidden="true">&rarr;</span></a>
                <a href="{base}/protected" on:click={toggleHamburgerMenu} class="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Sign out</a>

            </div>
          </div>
        </div>
      </div>
    </div>
</header>



<slot />

