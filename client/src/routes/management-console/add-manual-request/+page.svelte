<script lang=ts>

    import { gatepassrAPI } from "$lib/gatepassrAPI";
    import { onMount } from "svelte";
    let student_type: any[] = []
    let student_grade_json: any[] =[]
    let student_grade: any[] = []

    onMount( async () => {
        fetch(gatepassrAPI + "/recieve/studenttype")
            .then( response => response.json() )
            .then( data => { student_type = data } )
        fetch(gatepassrAPI + "/recieve/grades")
            .then( response => response.json() )
            .then( data => { student_grade = data } )
    });

</script>
<html lang="en-US" class="h-full bg-gray-100">
        <head>
            <meta charset="utf-8"/>
            <title>Add a Request Manually | Gatepassr Management Console</title>
        </head>
        <body class="h-full">
          <div class="min-h-full">
        <main>
            
          <div class="mx-4 mt-16 py-6 sm:mx-12">
            <div class="mx-4 my-2 lg:flex lg:items-center lg:justify-between">
              <ol class="flex items-center whitespace-nowrap" aria-label="Breadcrumb">
                <li class="inline-flex items-center">
                  <a class="flex items-center text-sm text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600 dark:focus:text-blue-500" href="/management-console">
                    Management Console
                  </a>
                  <svg class="flex-shrink-0 mx-2 overflow-visible size-4 text-gray-400 dark:text-neutral-600" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
                </li>
                
                <li class="inline-flex items-center text-sm font-semibold text-gray-800 truncate dark:text-gray-200" aria-current="page">
                    Manual Request Entry
                </li>
              </ol>
            </div>
            <!-- page header -->
            <div class="mx-4 mt-8 mb-6 lg:items-center lg:justify-between">
              
              <div class="min-w-0 flex-1">
                <h2 class="text-3xl font-bold leading-7 text-gray-900 sm:truncate sm:text-3xl sm:tracking-tight">Manual Request Entry</h2>
              </div>
              <div class="mt-5 flex lg:mt-0">
                <span class="block">
                </span>
                <!-- form start -->
                <form action = "{gatepassrAPI}/submit/gatepassrequest" method="POST" class="lg:flex lg:items-center lg:justify-between">
                    <div class="border-b border-gray-900/10 pb-12">
                        <div class="col-span-full mt-5">
                            <h2 class="text-base font-semibold leading-7 text-gray-900">Student Type</h2>
                            
                    
                            <div class="mt-3 space-y-6">
    
                                <div class="mt-3 space-y-3">
                                <div class="flex items-center gap-x-3">
                                    {#each student_type as user}
                                        <input type="radio" id={user[0]} name="student_type" value={user[0]} class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"/>
                                        <label class="block text-sm font-medium leading-6 text-gray-900" for={user[0]}>{user[1]}</label>
                                    {/each}
                                </div>
                                
                                </div>
                            </div>
                        </div>
                        <div class="col-span-full mt-8">
                            <label for="grade_select" class="text-base font-semibold leading-7 text-gray-900">Grade</label>
                            <select name="grade" id="grade" class="mt-4 block rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                                <option value="">Select Student's Grade...</option>
                                {#each Object.entries(student_grade) as [numeric_grade, display_grade]}
                                    <option value={numeric_grade}>{display_grade}</option>
                                {/each}
                            </select>
    
                        <div class="col-span-full mt-8">
                        <label for="exit-time" class="text-base font-semibold leading-7 text-gray-900">Requested Exit Time</label>
                        <input class="mt-4 block rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                        type="datetime-local"
                        id="exit-time"
                        name="exit-time"/>
                        <!-- TODO: add current date and time as
                        value="2022-06-12T19:30"
                        min="2018-06-07T00:00"
                        max="2018-06-14T00:00"
                        for input-->
                        
                        </div>
    
                        <!-- carpool radio box + car number -->
    
    
    
                        <div class="border-b border-gray-900/10 pb-12">
                            <h2 class="text-base font-semibold leading-7 text-gray-900 mt-8">Guardian Details</h2>
                        
                    
                            <div class="my-4">
                                <label for="name-guardian" class="block text-sm font-medium leading-6 text-gray-900">Guardian's Name</label>
                                <div class="mt-2">
                                <input type="text" name="name-guardian" id="name-guardian" autocomplete="given-name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                                </div>
                            </div>
                    
                            <div class="my-4">
                                <label for="guardian-relation" class="block text-sm font-medium leading-6 text-gray-900">Guardian's Relation With Student</label>
                                <div class="mt-2">
                                <input type="text" name="guardian-relation" id="guardian-relation" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                                </div>
                            </div>
                    
                            <div class="my-4">
                                <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Guardian's Email Address</label>
                                <div class="mt-2">
                                <input id="email" name="email" type="email" autocomplete="email" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                                </div>
                            </div>
    
                            <div class="my-4">
                                <h2 class="text-base font-semibold leading-7 text-gray-900 pt-4 pb-1">Reason for Gatepass</h2>
                                <div class="mt-2">
                                <textarea id="about" name="about" rows="3" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"></textarea>
                            </div>

                            <div class="my-4">
                                <h2 class="text-base font-semibold leading-7 text-gray-900 pt-4 pb-1">Reason for Manual Entry</h2>
                                <label for="about" class="block text-sm font-medium leading-6 text-gray-600">Describe why the manual request was created (eg. error at X screen, emergency...)</label>
                                <div class="mt-2">
                                <textarea id="about" name="about" rows="3" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"></textarea>
                            </div>
    
                    <div class="mt-6 flex items-center justify-end gap-x-6">
                    <button type="button" class="text-sm font-semibold leading-6 text-gray-900">Cancel</button>
                    <button type="submit" class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Add request!</button>
                    </div>
                </form>

                <!-- form end -->
                        
              </div> 
            </div>
            </div>
            
        </main>
    </div>
    </body>
</html>
