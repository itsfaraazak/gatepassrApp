<script>
    // @ts-nocheck
    
    export let gatepassrAPIurl
    export let grades
    export let min_date
    export let  profiledata
    </script>
    
    <form action = "{gatepassrAPIurl}/submit/gatepassrequest" method="POST" class="mx-4 mt-4 mb-4 lg:flex lg:items-center lg:justify-between">
        <div class="space-y-4">
        <div class="border-b border-gray-900/10 pb-5">
            <h1 class="text-3xl font-bold leading-7 text-gray-900 sm:truncate sm:text-3xl sm:tracking-tight">Request for a gatepass</h1>
            
            {#if profiledata}
            <div class="mt-10 grid grid-cols-1 gap-x-2 gap-y-2 sm:grid-cols-7">
            <div class="sm:col-span-3">
              <label for="username" class="text-base font-semibold leading-7 text-gray-900">Student Name</label>
              <div class="mt-2">
                <select  class="rounded-md border-0 py-1 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    {#each profiledata.student_list as student, index}
                        <option value={student.student_email}>
                            {student.student_name}-Grade {student.grade}
                        </option>
                    {/each}
                </select>
              </div>
            </div>
            
            <div class="sm:col-span-4">
            <h2 class="text-base font-semibold leading-7 text-gray-900">Student is a...</h2>
                <div class="mt-2 flex items-center gap-x-3">
                    <input type="radio" id="1" name="student_type" value="1" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"/>
                        <label class="block text-sm font-medium leading-6 text-gray-900" for="1">Day Scholar</label>
                    <input type="radio" id="2" name="student_type" value="2" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"/>
                        <label class="block text-sm font-medium leading-6 text-gray-900" for="2">Weekly Boarder</label>
                    <input type="radio" id="3" name="student_type" value="3" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"/>
                        <label class="block text-sm font-medium leading-6 text-gray-900" for="3">Boarder</label>

                    <!-- {#each student_type as user}
                        <input type="radio" id={user[0]} name="student_type" value={user[0]} class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"/>
                        <label class="block text-sm font-medium leading-6 text-gray-900" for={user[0]}>{user[1]}</label>
                    {/each} -->
                </div>
            </div>
           </div>
            {/if}
            <!-- <div class="mt-5">
                <h2 class="text-base font-semibold leading-7 text-gray-900">You are a...</h2>
                <div class="mt-3 space-y-6">
    
                    <div class="mt-3 space-y-3">
                    <div class="flex items-center gap-x-3">
                        <input type="radio" id="1" name="student_type" value="1" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"/>
                            <label class="block text-sm font-medium leading-6 text-gray-900" for="1">Day Scholar</label>
                        <input type="radio" id="2" name="student_type" value="2" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"/>
                            <label class="block text-sm font-medium leading-6 text-gray-900" for="2">Weekly Boarder</label>
                        <input type="radio" id="3" name="student_type" value="3" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"/>
                            <label class="block text-sm font-medium leading-6 text-gray-900" for="3">Boarder</label>
    
                    
                    </div>
                </div>
            </div> -->
            <div class="mt-5">
                <!-- <label for="grade_select" class="text-base font-semibold leading-7 text-gray-900">Which grade student is in?</label>
                <select name="grade" id="grade" class="mt-4 mx-2 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    <option value="">Select grade</option>
                    {#each grades as grade}
                        <option value={grade.id}>
                            {grade.text}
                        </option>
                    {/each}
                </select> -->
    
            <div class="mt-5 col-span-full">
            <label for="exit-time" class="text-base font-semibold leading-7 text-gray-900">When will you be leaving school?</label>
            <input class="mt-4 mx-2 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            type="datetime-local"
            id="exit-time"
            name="exit-time" min={min_date} value="{min_date}"/>
            </div>
            <!-- carpool radio box + car number -->
            
                <h2 class="text-base font-semibold leading-7 text-gray-900 mt-5">Who will pick you up?</h2>
            
        
                <div class="my-4">
                    <label for="name-guardian" class="block text-sm font-medium leading-6 text-gray-900">Guardian's name</label>
                    <div class="mt-2">
                    <input type="text" name="name-guardian" id="name-guardian" autocomplete="given-name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    </div>
                </div>
        
                <div class="my-4">
                    <label for="guardian-relation" class="block text-sm font-medium leading-6 text-gray-900">How is your guardian related to you?</label>
                    <div class="mt-2">
                    <input type="text" name="guardian-relation" id="guardian-relation" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    </div>
                </div>
        
                <div class="my-4">
                    <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Guardian's Email address</label>
                    <div class="mt-2">
                    <input id="email" name="email" type="email" autocomplete="email" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    </div>
                </div>
    
                <div class="my-4">
                    <h2 class="text-base font-semibold leading-7 text-gray-900 pt-4 pb-1">Reason for gatepass</h2>
                    <!-- <label for="about" class="block text-sm font-medium leading-6 text-gray-600">Briefly describe why you are applying for this gatepass</label> -->
                    <div class="mt-2">
                    <textarea id="about" name="about" rows="3" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"></textarea>
                </div>
    
        <div class="mt-5 flex items-center justify-end gap-x-6">
        <button type="button" class="text-sm font-semibold leading-6 text-gray-900">Cancel</button>
        <button type="submit" class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Send request!</button>
        </div>
    </form>