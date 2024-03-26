<script lang="ts">
    import { onMount } from 'svelte';
    import { gatepassrAPI } from "$lib/gatepassrAPI";
    //import Gprequest from  '$components/gprequest.svelte';
    import Breadcrumb from '$components/breadcrumb.svelte';
    import {grades} from '../../config'
    import { page } from '$app/stores';
    import type { PageData } from '../$types';

    import { superForm } from 'sveltekit-superforms/client';
    import { z } from "zod"
    import SuperDebug from "sveltekit-superforms/client/SuperDebug.svelte"

    export let data;
   
const fetchProfile = data.profile;

//     const requestGatepassSchema = z.object({
//         student_type: z.string().trim().nonempty({ message: "Student type is required" }),
//         exit_time: z.date({
//         required_error: "Date is required",
//         invalid_type_error: "Format invalid",
//   }),

//     })
    //const { form,errors, message, enhance , constraints} = superForm(data,{
        //taintedMessage:"Are you sure you want to leave?.",
      //  validators: requestGatepassSchema,
    //});

    let student_type: any[] = []
    let student_grade_json: any[] =[]
    let student_grade: any[] = []
    let studentlist: any[] =[]
    let getprofiledata:any;
    let profile =""
    let selection: any[] = [];
    $: selectionCount = selection.length;
    //let useremail = $page?.data?.session?.user?.email ?? 'itsyasmeenkhan@gmail.com';
    let useremail =data.user_email
    console.log(useremail);
    let  profiledata={
        guardian_id: 0,
        primary_guardian_email: "",
        secondary_guardian_email:"",
        primary_contact_number:"",
        secondary_contact_number:"",
        student_list: studentlist,
        created_by:useremail
        }
    
    var date = new Date();
    let minimum_date= ( date.getFullYear() + "-"+("0" + (date.getMonth() + 1)).slice(-2) + "-"+ ("0" + date.getDate()).slice(-2) + "T" + ("0" + date.getHours() ).slice(-2) + ":"+ ("0" + date.getMinutes()).slice(-2) );
   
    
      //getprofiledata = await getProfile();
      getprofiledata = fetchProfile;
      let profiledataobj =  getprofiledata[0]
      //console.log(profiledataobj)
      profiledata.guardian_id = profiledataobj.guardian_id;
      profiledata.primary_guardian_email = profiledataobj.primary_guardian_email;
      profiledata.secondary_guardian_email=profiledataobj.secondary_guardian_email;
      profiledata.student_list = profiledataobj.student_list;
      profiledata.primary_contact_number=profiledataobj.primary_contactnumber;
      profiledata.secondary_contact_number=profiledataobj.seconday_contactnumber;
</script>



<div class="mx-4 mt-8 py-6 sm:mx-12">
    <!-- <SuperDebug data={form} /> -->
    <Breadcrumb currentpage="Request for a Gatepass"/>
    <!-- <Gprequest gatepassrAPIurl={gatepassrAPI} grades={grades} min_date={minimum_date} profiledata={profiledata}/> -->
    <form action = "{gatepassrAPI}/submit/gatepassrequest" name="gprequestform"  id="gprequestform"
    method="POST" 
    class="mx-4 mt-4 mb-4 lg:flex lg:items-center lg:justify-between">
        <div class="space-y-4">
        <div class="border-b border-gray-900/10 pb-5">
            <h1 class="text-3xl font-bold leading-7 text-gray-900 sm:truncate sm:text-3xl sm:tracking-tight">Request for a gatepass</h1>
            
            
            <div class="mt-10 grid grid-cols-1 gap-x-2 gap-y-2 sm:grid-cols-7">
            <div class="sm:col-span-3">
              <label for="username" class="text-base font-semibold leading-7 text-gray-900">Student Name *</label>
              <div class="mt-2">
                <!-- <select multiple name="student_list" class="min-w-16 rounded-md border-0 py-1 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    {#each profiledata.student_list as student, index}
                        <option value={student.student_name},{student.student_email},{student.grade}>
                            {student.student_name}  (Grade-{student.grade})
                        </option>
                    {/each}
                </select> -->
                {#each profiledata.student_list as student, index}
                <div class="flex items-center mb-4" >
                    <input id="default-checkbox" bind:group={selection} type="checkbox" name="student_list"
                    value={student.student_name},{student.student_email},{student.grade} class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 ">
                    <label for="default-checkbox" class="ms-2 text-sm font-medium">
                        {student.student_name}  (Grade-{student.grade})
                    </label>
                </div>
                {/each}
                <input type="hidden" bind:value={selection} name="student_array" id="student_array"/>
                <input type="hidden" bind:value={selectionCount} name="student_count" id="student_count"/>
                <!-- <checkbox name="student_list_1" class="min-w-16 rounded-md border-0 py-1 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    {#each profiledata.student_list as student, index}
                        <option value={student.student_name},{student.student_email},{student.grade}>
                            {student.student_name}  (Grade-{student.grade})
                        </option>
                    {/each}
                </checkbox> -->
                <!-- <input type="text" id="grade" name="grade" />-->
                <input id="name" class="hidden" name="student_email"/> 
                     
                
              </div>
            </div>
            
            <div class="sm:col-span-4">
            <h2 class="text-base font-semibold leading-7 text-gray-900">Student is ...*</h2>
                <div class="mt-2 flex items-center gap-x-3">
                    <input type="radio"required bind:group={student_type} id="1" name="student_type" value="1" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"/>
                        <label class="block text-sm font-medium leading-6 text-gray-900" for="1">Day Scholar</label>
                    <input type="radio"  required bind:group={student_type} id="2" name="student_type" value="2" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"/>
                        <label class="block text-sm font-medium leading-6 text-gray-900" for="2">Weekly Boarder</label>
                    <input type="radio"  required bind:group={student_type} id="3" name="student_type" value="3" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"/>
                        <label class="block text-sm font-medium leading-6 text-gray-900" for="3">Boarder</label>

                </div>
            </div>
           </div>
            
            <div class="mt-5">
               
            <div class="mt-5 col-span-full">
            <label for="exit-time" class="text-base font-semibold leading-7 text-gray-900">When will you be leaving school? *</label>
            <input required class="mt-4 mx-2 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            type="datetime-local"
            id="exit-time"
            name="exit-time" min="{minimum_date}"/>
            </div>
            
            
                <h2 class="text-base font-semibold leading-7 text-gray-900 mt-5">Who will pick you up? *</h2>
            
        
                <div class="my-4">
                    <label for="name-guardian" class="block text-sm font-medium leading-6 text-gray-900">Guardian's name *</label>
                    <div class="mt-2">
                    <input type="text" required name="name-guardian" value={data.user_email} readonly class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    </div>
                </div>
        
                <div class="my-4">
                    <label for="guardian-relation" class="block text-sm font-medium leading-6 text-gray-900">How is your guardian related to you? *</label>
                    <div class="mt-2">
                    <input type="text" required name="guardian-relation" id="guardian-relation" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    </div>
                </div>
        
                <div class="my-4">
                    <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Guardian's Email address *</label>
                    <div class="mt-2">
                    <input id="email" name="email" required type="email" autocomplete="email" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    </div>
                </div>
    
                <div class="my-4">
                    <h2 class="text-base font-semibold leading-7 text-gray-900 pt-4 pb-1">Reason for gatepass *</h2>
                    <!-- <label for="about" class="block text-sm font-medium leading-6 text-gray-600">Briefly describe why you are applying for this gatepass</label> -->
                    <div class="mt-2">
                    <textarea id="about" required name="about" rows="3" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"></textarea>
                </div>
    
        <div class="mt-5 flex items-center justify-end gap-x-6">
        <button type="button" 
        class="text-sm font-semibold leading-6 text-gray-900">Cancel</button>
        <button type="submit" 
        class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
        Send request!</button>
        </div>
    </form>
</div>
