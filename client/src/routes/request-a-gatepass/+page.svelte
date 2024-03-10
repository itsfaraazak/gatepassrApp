<script lang=ts>
    import { onMount } from 'svelte';
    import { gatepassrAPI } from "$lib/gatepassrAPI";

    import Gprequest from  '$components/gprequest.svelte';
    import Breadcrumb from '$components/breadcrumb.svelte';
    import {grades} from '../../config'
   

    let student_type: any[] = []
    let student_grade_json: any[] =[]
    let student_grade: any[] = []
    let useremail =""
    var date = new Date();

    let minimum_date= ( date.getFullYear() + "-"+("0" + (date.getMonth() + 1)).slice(-2) + "-"+ ("0" + date.getDate()).slice(-2) + "T" + ("0" + date.getHours() ).slice(-2) + ":"+ ("0" + date.getMinutes()).slice(-2) );
    console.log(minimum_date)   
 
 // Converting the number value to string
   // let a = d.toString()
    //a = d.toString("YYYY-MM-DD HH:mm:ss")
    onMount( async () => {
        // fetch(gatepassrAPI + "/recieve/studenttype")
        //     .then( response => response.json() )
        //     .then( data => { student_type = data } )
        fetch(gatepassrAPI + "/recieve/grades")
            .then( response => response.json() )
            .then( data => { student_grade = data } )
            let bearer =(localStorage.getItem("jwtToken"))
       
   });

</script>



<div class="mx-4 mt-8 py-6 sm:mx-12">
    <Breadcrumb currentpage="Request for a Gatepass"/>
    <Gprequest gatepassrAPIurl={gatepassrAPI} grades={grades} min_date={minimum_date}/>
</div>
