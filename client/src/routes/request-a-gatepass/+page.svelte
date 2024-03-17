<script lang=ts>
    import { onMount } from 'svelte';
    import { gatepassrAPI } from "$lib/gatepassrAPI";

    import Gprequest from  '$components/gprequest.svelte';
    import Breadcrumb from '$components/breadcrumb.svelte';
    import {grades} from '../../config'
    import { page } from '$app/stores';

    let student_type: any[] = []
    let student_grade_json: any[] =[]
    let student_grade: any[] = []
    let studentlist: any[] =[]
    let getprofiledata:any;
    let profile =""
    let useremail = $page?.data?.session?.user?.email;
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
 
    onMount( async () => {
        // fetch(gatepassrAPI + "/recieve/studenttype")
        //     .then( response => response.json() )
        //     .then( data => { student_type = data } )
        fetch(gatepassrAPI + "/recieve/grades")
            .then( response => response.json() )
            .then( data => { student_grade = data } )
           // let bearer =(localStorage.getItem("jwtToken"))
        
           await fetch(gatepassrAPI + "/recieve/profile")
      .then( response => response.json() )
      .then( data => { getprofiledata = data} )

      let profiledataobj =  getprofiledata[0]
      console.log(profiledataobj)
      profiledata.guardian_id = profiledataobj.guardian_id;
      profiledata.primary_guardian_email = profiledataobj.primary_guardian_email;
      profiledata.secondary_guardian_email=profiledataobj.secondary_guardian_email;

      profiledata.student_list = profiledataobj.student_list;
      profiledata.primary_contact_number=profiledataobj.primary_contactnumber;
      profiledata.secondary_contact_number=profiledataobj.seconday_contactnumber;
   });

</script>



<div class="mx-4 mt-8 py-6 sm:mx-12">
    <Breadcrumb currentpage="Request for a Gatepass"/>
    <Gprequest gatepassrAPIurl={gatepassrAPI} grades={grades} min_date={minimum_date} profiledata={profiledata}/>
</div>
