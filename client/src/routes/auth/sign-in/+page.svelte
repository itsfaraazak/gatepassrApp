<script>
    import { gatepassrAPI } from "$lib/gatepassrAPI";
    // @ts-ignore
    let rooturlflask='http://127.0.0.1:5000'
    // @ts-ignore
    let username = '';
    let password = '';
    let token = '';
    let message ='';
    
    const login = async () => {
        const response = await fetch(gatepassrAPI + '/auth/signin', {
            method: 'POST',
            //mode:'no-cors',
            headers: {
                'Content-Type': 'application/json',
                //'Accept': 'application/json',
            },
            body: JSON.stringify({ username, password }),
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
            //window.location.href = '/auth/sign-in/protected'; // Redirect to protected route
            window.location.href = '/request-a-gatepass'; // Redirect to protected route

        } else {
            message = data.msg;
            console.error('Login failed:', data.msg);
        } 
    };
    
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
                    <input id="email"  bind:value={username} type="email" autocomplete="email" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
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
                    <input id="password"  bind:value={password} type="password" autocomplete="current-password" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
                </div>
        
                <div>
                <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign in</button>
                </div>
            </form>
             <span>{message}</span>
            <p class="mt-10 text-center text-sm text-gray-500">gatepassrAPIgatepassrAPI
                Not a member?
                <a href="/auth/sign-up" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Sign Up</a>
            </p>
            </div>
        </div>

    </body>
</html>