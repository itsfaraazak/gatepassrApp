<script>
    import { gatepassrAPI } from '$lib/gatepassrAPI';
    import { onMount } from 'svelte';

    let message = '';
   
    onMount(async () => {
        // @ts-ignore
        let bearer =(localStorage.getItem("jwtToken"))
       
        const response = await fetch(gatepassrAPI + '/auth/protected', {
            method: 'GET',
            // @ts-ignore
           // mode: '*',
            credentials: 'include',
            headers: {
                'Authorization': "Bearer " + bearer,
                "content-type": "application/json",
            },
            // @ts-ignore
            xhrFields: { withCredentials: true},
        });

        if (response.ok) {
            const data = await response.json();
            message = data.logged_in_as;
        } else {
            const data = await response.json();
            console.error('Access denied:', data.message);
            message = 'Access denied';
        }
    });
</script>

<style>
    /* Add your styles here */
</style>

<div>
    <h2>Protected Route</h2>
    <p>Welcome {message}</p>
</div>