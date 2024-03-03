<!-- Login.svelte -->
<script>
    import { gatepassrAPI } from "$lib/gatepassrAPI";

    let email = '';
    let password = '';
    let token = '';

    const login = async () => {
        const response = await fetch(gatepassrAPI + '/auth/signin', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
               // 'Accept': 'application/json',
            },
            body: JSON.stringify({ email, password }),
        });

        const data = await response.json();

        console.log(data)
        //access_token
        if (data.access_token) {
            token = data.access_token;
            // Store the token in localStorage or a more secure storage mechanism
            console.log('access_token:', token);
            // After successful login
            localStorage.setItem('jwtToken', token);
            // @ts-ignore
            console.log("===" +(localStorage.getItem("jwtToken")))
            window.location.href = '/auth/sign-in/protected'; // Redirect to protected route

        } else {
            console.error('Login failed:', data.message);
        } 
        
        /* if (response.ok) {
            // Login successful
            window.location.href = '/auth/sign-in/protected'; // Redirect to protected route
        } else {
            // Login failed
            const data = await response.json();
            console.error('Login failed:', data.message);
        } */
    };
</script>

<style>
    /* Add your styles here */
</style>

<div>
    <br>
    <br>    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>

    <h2>Login</h2>
    <form on:submit={login}>
        <label for="username">Username:</label>
        <input bind:value={email} type="text" id="username">

        <label for="password">Password:</label>
        <input bind:value={password} type="password" id="password">

        <button type="submit">Login</button>
    </form>
</div>
