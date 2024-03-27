<script lang=ts>
  import { gatepassrAPI } from "$lib/gatepassrAPI"
  import { base } from '$app/paths';
    
</script>


<body class="my-10 mx-4">
        <div>
             <div class="mx-auto max-w-2xl py-32 sm:py-48 lg:py-56">
<!--                 <div class="hidden sm:mb-8 sm:flex sm:justify-center">
                   <div class="card relative px-3 py-1 text-sm leading-6 text-on-primary-600 hover:">
                    Announcing our next round of funding. <a href="#" class="font-semibold text-indigo-600"><span class="absolute inset-0" aria-hidden="true"></span>Read more <span aria-hidden="true">&rarr;</span></a>
                  </div>
                </div> -->
                 <div class="text-center">
                  <h1 class="text-4xl font-bold tracking-tight text-primary sm:text-6xl">
                    <span class="bg-gradient-to-br from-blue-500 to-cyan-300 bg-clip-text text-transparent box-decoration-clone">Gatepassr</span> does gatepasses
                    <span class="bg-gradient-to-br from-red-500 to-yellow-500 bg-clip-text text-transparent box-decoration-clone">better.</span>
                  </h1>
                  <div class="mt-10 flex items-center justify-center gap-x-6">
<!--                     <a href="{base}/auth/sign-in" class="rounded-container-token bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Get started</a>
 -->                    <a href="{base}/login" class="btn variant-filled">Get started</a>

                    <a href="{base}/about-us" class="text-sm font-semibold leading-6 text-on-primary">Learn more <span aria-hidden="true">→</span></a>
                  </div>
                </div>
              </div>
          </div>
<!--           </div>
 -->          
    </body>
