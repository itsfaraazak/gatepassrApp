<script lang=ts>
    import { onMount } from 'svelte';

    /*
    import type { PageData, ActionData } from './$types';

    
	export let data: PageData;
	export let form: ActionData;


    fetch("http://127.0.0.1:5000", {
        method: "GET",
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    });
    */

    /*
    fetch("http://127.0.0.1:5000")
        .then((response) => response.json())
        .then((json) => console.log(json));
    */
    /*
    import { onMount } from 'svelte';
    let request;
    onMount(async () => {
        const response = await fetch(
            'http://127.0.0.1:5000',
            {
                method: 'GET',
                mode: 'no-cors'
            }
        );
        request = await response;
        //request = data;
        console.log(request)
    });
    

    async function getUsers() {
        let response = await fetch("http://127.0.0.1:5000");
        let users = await response.json();
        return users;
    }
    const promise = getUsers();
 

    async function frmsubmit() {

        let response = await fetch('http://127.0.0.1:5000/submitrequest', {
        method: 'POST',
        body: new FormData()
        });

        let result = await response.json();

        alert(result.message);
    };
*/

    
    let student_type: any[] = []
    let student_grade_json: any[] =[]
    let student_grade: any[] = []

    onMount( async () => {
        fetch("http://127.0.0.1:5000/recieve/studenttype")
            .then( response => response.json() )
            .then( data => { student_type = data } )
        fetch("http://127.0.0.1:5000/recieve/grades")
            .then( response => response.json() )
            .then( data => { student_grade = data } )
    });

    console.log(student_grade)    

</script>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Apply for a gatepass</title>
</head>

<!--
<body>
    <h1>Apply for a gatepass for John @ Indus</h1>


    <form action="/my-handling-form-page" method="post"> 
        <label class="block">
            <ul>
                <li>
                    <label for="student_type">Are you a...</label>
                    <div>
                        {#await promise}
                            <p>Loading...</p>
                        {:then user}
                            {#each user as user}
                                <input type="radio" id={user[0]} name="student_type" value={user[1]} />
                                <label for={user[0]}>{user[1]}</label>
                            {/each}
                        {:catch error}
                            <p style="color: red">{error.message}</p>
                        {/await}
                    </div>
                </li>
                <li>
                <label for="exit_datetime">When do you plan to leave?</label>
                <input type="datetime-local" id="exit_datetime" name="exit_datetime" required/>
                min="2018-06-07T00:00" max="2018-06-14T00:00" should be added to input
                </li>
                <li>
                <label for="reason">What's the reason for which you are issuing this gatepass?</label>
                <textarea id="reason" name="reason"></textarea>
                </li>
                <li class="button">
                    <button class="bg-sky-500 hover:bg-sky-700" type="submit">Send your request</button>
                </li>
            </ul>
          </label>
    </form> 

    <form>
        <label class="block mr-8 ml-8">
            <span class="block text-sm font-medium text-slate-700">You are a...</span>
            <div>
                {#await promise}
                    <p>Loading...</p>
                {:then user}
                    {#each user as user}
                        <input type="radio" id={user[0]} name="student_type" value={user[1]} class="checked:border-blue-500"/>
                        <label for={user[0]}>{user[1]}</label>
                    {/each}
                {:catch error}
                    <p style="color: red">{error.message}</p>
                {/await}
            </div>
            <span class="block text-sm font-medium text-slate-700">Enter the Guardian's Email</span>
            <input type="email" class="peer mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400
            focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
            disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none
            invalid:border-pink-500 invalid:text-pink-600
            focus:invalid:border-pink-500 focus:invalid:ring-pink-500"/>
            <p class="mt-2 invisible peer-invalid:visible text-pink-600 text-sm">
                Please provide a valid email address.
            </p>
        </label>
         
      </form>

</body>


-->


<!--
  This example requires some changes to your config:
  
  ```
  // tailwind.config.js
  module.exports = {
    // ...
    plugins: [
      // ...
      require('@tailwindcss/forms'),
    ],
  }
  ```
-->

<body class="my-4 mx-4">

<form action = "http://127.0.0.1:5000/submit/gatepassrequest" method="POST">
    <div class="space-y-12">
      <div class="border-b border-gray-900/10 pb-12">
        <h1 class="text-base font-semibold leading-7 text-gray-900">Request for a gatepass</h1>
        <p class="mt-1 text-sm leading-6 text-gray-600">This information is required to process your gatepass.</p>
  
        <!-- radios -->

        <div class="col-span-full mt-8">
            <h2 class="text-base font-semibold leading-7 text-gray-900">You are a...</h2>
            <p class="mt-1 text-sm leading-6 text-gray-600">A day scholar student returns home every day, a weekly boarder returns every week and a boarder returns every term.</p>
    
            <div class="mt-3 space-y-6">

                <div class="mt-3 space-y-3">
                  <div class="flex items-center gap-x-3">
                    {#each student_type as user}
                        <input type="radio" id={user[0]} name="student_type" value={user[0]} class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"/>
                        <label class="block text-sm font-medium leading-6 text-gray-900" for={user[0]}>{user[1]}</label>
                    {/each}
                    <!--
                    {#await promise}
                        <p>Loading...</p>
                    {:then user}
                        {#each user as user}
                            <input type="radio" id={user[0]} name="student_type" value={user[1]} class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"/>
                            <label class="block text-sm font-medium leading-6 text-gray-900" for={user[0]}>{user[1]}</label>
                        {/each}
                    {:catch error}
                        <p style="color: red">{error.message}</p>
                    {/await}
                    -->
                  </div>
                  
                </div>
            </div>
        </div>

        <!-- radio end -->

        <!-- grade of student -->

        <div class="col-span-full mt-8">
            <label for="grade_select" class="text-base font-semibold leading-7 text-gray-900">Which grade are you in?</label>
            <select name="grade" id="grade" class="mt-4 block rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                <option value="">Select your grade...</option>
                {#each Object.entries(student_grade) as [numeric_grade, display_grade]}
                    <option value={numeric_grade}>{display_grade}</option>
                <!-- <option value={display_grade}>{display_grade}</option> -->
                {/each}
            </select>

        <!-- grade of student end -->

        <!-- Exit time input -->

        <div class="col-span-full mt-8">
        <label for="exit-time" class="text-base font-semibold leading-7 text-gray-900">When will you be leaving school?</label>
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

        <!-- Exit time input end-->

        <!-- carpool radio box + car number -->



        <!-- Guardian info -->

        <div class="border-b border-gray-900/10 pb-12">
            <h2 class="text-base font-semibold leading-7 text-gray-900 mt-8">Who will pick you up?</h2>
            <p class="mt-1 text-sm leading-6 text-gray-600">Enter information correctly to ensure no hassles at pick-up.</p>
      
            <div class="mt-4 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
              <div class="sm:col-span-3">
                <label for="name-guardian" class="block text-sm font-medium leading-6 text-gray-900">Guardian's name</label>
                <div class="mt-2">
                  <input type="text" name="name-guardian" id="name-guardian" autocomplete="given-name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
              </div>
      
              <div class="sm:col-span-3">
                <label for="guardian-relation" class="block text-sm font-medium leading-6 text-gray-900">How is your guardian related to you?</label>
                <div class="mt-2">
                  <input type="text" name="guardian-relation" id="guardian-relation" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
              </div>
      
              <div class="sm:col-span-4">
                <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Guardian's Email address</label>
                <div class="mt-2">
                  <input id="email" name="email" type="email" autocomplete="email" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
              </div>

        <!-- Guardian info end-->
        <!-- reason for gatepass -->
            <div class="col-span-full">
                <h2 class="text-base font-semibold leading-7 text-gray-900 pt-4 pb-1">Why are you issuing this gatepass?</h2>
                <label for="about" class="block text-sm font-medium leading-6 text-gray-600">Briefly describe why you are applying for this gatepass</label>
                <div class="mt-2">
                <textarea id="about" name="about" rows="3" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"></textarea>
                </div>
            </div>

            <!-- reason for gatepass end-->  
    <div class="mt-6 flex items-center justify-end gap-x-6">
      <button type="button" class="text-sm font-semibold leading-6 text-gray-900">Cancel</button>
      <button type="submit" class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Send request!</button>
    </div>
  </form>
  

</body>

<!--
<div>
    {#each request as i}
        <p>i</p>
    {/each}
</div>
-->