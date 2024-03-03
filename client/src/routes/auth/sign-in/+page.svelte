<script>
    // @ts-ignore
    let rooturlflask='http://127.0.0.1:5000'
    // @ts-ignore
    //let username = '';
   // let password = '';
    let token = '';
    import { gatepassrAPI } from "$lib/gatepassrAPI";
    // @ts-ignore
    import bcrypt from 'bcryptjs';
    let email = '';
   // let password = '';
   // let token = '';
   //const bcryptjs = require('bcryptjs');

   const numSaltRounds = 8;
   let hashedPassword='';
   

    const login = async () => {
           let password =document.getElementById('password')
           let email = document.getElementById('email')
            await bcrypt.hash(password, numSaltRounds)
                    // @ts-ignore
                    .then(result => {
                        console.log('Result from promise:', result);
                        password = result
                    })
                    // @ts-ignore
                    .catch(error => {
                        console.error('Error:', error);
                        // Handle errors if the promise is rejected
                    });
            //                 // Store hashedPassword in your database
    console.log('Hashed Password:', password);

        console.log(password)
        const response = await fetch(gatepassrAPI + '/auth/signin', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
               // 'Accept': 'application/json',
            },
            body: JSON.stringify({ email, password}),
        });

        const data = await response.json();

        console.log(data)
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
    };
    /*
    const login = async () => {
        const response = await fetch('http://localhost:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        });

        const data = await response.json();

        if (data.token) {
            token = data.token;
            // Store the token in localStorage or a more secure storage mechanism
            console.log('Token:', token);
        } else {
            console.error('Login failed:', data.message);
        }
    };
    */
</script>
<html lang="en-US" class="h-full bg-white">
    <head>
        <meta charset="utf-8"/>
        <title>Sign in to Gatepassr...</title>
    </head>
    <body class="h-full">
        <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
            <div class="sm:mx-auto sm:w-full sm:max-w-sm">
            <img class="mx-auto h-10 w-auto" src="" alt="Your Company">
            <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in to GatepassApp</h2>
            </div>
        
            <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
            <form id=sign-in class="space-y-6" on:submit={login}>
                <div>
                <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
                <div class="mt-2">
                    <input id="email"  name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
                </div>
        
                <div>
                <div class="flex items-center justify-between">
                    <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
                    <div class="text-sm">
                    <a href="/auth/forgotpassword" class="font-semibold text-indigo-600 hover:text-indigo-500">Forgot password?</a>
                    </div>
                </div>
                <div class="mt-2">
                    <input id="password"  name="password" type="password" autocomplete="current-password" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
                </div>
        
                <div>
                <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign in</button>
                </div>
            </form>
        
            <p class="mt-10 text-center text-sm text-gray-500">
                Not a member?
                <a href="/auth/sign-up" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Sign Up</a>
            </p>
            </div>
        </div>

    </body>
</html>