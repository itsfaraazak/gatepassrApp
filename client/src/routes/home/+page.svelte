<script>
    import { PushNotifications } from '@capacitor/push-notifications';

    const addListeners = async () => {
    await PushNotifications.addListener('registration', token => {
        console.info('Registration token: ', token.value);
    });

    await PushNotifications.addListener('registrationError', err => {
        console.error('Registration error: ', err.error);
    });

    await PushNotifications.addListener('pushNotificationReceived', notification => {
        console.log('Push notification received: ', notification);
    });

    await PushNotifications.addListener('pushNotificationActionPerformed', notification => {
        console.log('Push notification action performed', notification.actionId, notification.inputValue);
    });
    }

    const registerNotifications = async () => {
    let permStatus = await PushNotifications.checkPermissions();

    if (permStatus.receive === 'prompt') {
        permStatus = await PushNotifications.requestPermissions();
    }

    if (permStatus.receive !== 'granted') {
        throw new Error('User denied permissions!');
    }

    await PushNotifications.register();
    }

    const getDeliveredNotifications = async () => {
    const notificationList = await PushNotifications.getDeliveredNotifications();
    console.log('delivered notifications', notificationList);
    }
</script>

<html lang="en-US" class="h-full bg-gray-100">
        <head>
            <meta charset="utf-8"/>
            <title>Gatepassr Home</title>
        </head>
        <body class="h-full">
          <div class="min-h-full">
        <main>
            
          <div class="mx-4 mt-16 py-6 sm:mx-12">
            <div class="mx-4 my-2 lg:flex lg:items-center lg:justify-between">
              <ol class="flex items-center whitespace-nowrap" aria-label="Breadcrumb">
                <li class="inline-flex items-center">
                  <a class="flex items-center text-sm text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600 dark:focus:text-blue-500" href="#">
                    Home
                  </a>
                  <svg class="flex-shrink-0 mx-2 overflow-visible size-4 text-gray-400 dark:text-neutral-600" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
                </li>
                <li class="inline-flex items-center">
                  <a class="flex items-center text-sm text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600 dark:focus:text-blue-500" href="#">
                    App Center
                    <svg class="flex-shrink-0 mx-2 overflow-visible size-4 text-gray-400 dark:text-neutral-600" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
                  </a>
                </li>
                <li class="inline-flex items-center text-sm font-semibold text-gray-800 truncate dark:text-gray-200" aria-current="page">
                  Application
                </li>
              </ol>
            </div>
            <!-- page header -->
            <div class="mx-4 mt-8 mb-6 lg:flex lg:items-center lg:justify-between">
              
              <div class="min-w-0 flex-1">
                <h2 class="text-3xl font-bold leading-7 text-gray-900 sm:truncate sm:text-3xl sm:tracking-tight">Gatepassr Home</h2>
              </div>
              <div class="mt-5 flex lg:ml-4 lg:mt-0">
                <span class="block">
                </span>

                
                        
              </div> 
            </div>
            </div>

            <div class="mx-8 flex flex-wrap flex-row">
              <div class="basis-auto text-gray-700 bg-white shadow-md bg-clip-border rounded-xl w-96">
                <div
                  class="bg-white relative h-56 mx-4 -mt-6 overflow-hidden text-white shadow-lg bg-clip-border rounded-xl bg-blue-gray-500 shadow-blue-gray-500/40 flex justify-center">
                  <img
                    src="https://pune.indusschool.com/wp-content/uploads/2023/03/logo.png"
                    alt="card" />
                </div>
                <div class="p-6">
                  <h5 class="block mb-2 font-sans text-xl antialiased font-semibold leading-snug tracking-normal text-blue-gray-900">
                    UI/UX Review Check
                  </h5>
                  <p class="block font-sans text-base antialiased font-light leading-relaxed text-inherit">
                    The place is close to Barceloneta Beach and bus stop just 2 min by walk
                    and near to "Naviglio" where you can enjoy the main night life in
                    Barcelona.
                  </p>
                </div>
                <div class="p-6 pt-0">
                  <button
                    class="align-middle select-none font-sans font-bold text-center uppercase transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-3 px-6 rounded-lg bg-gray-900 text-white shadow-md shadow-gray-900/10 hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none"
                    type="button">
                    Read More
                  </button>
                </div>
              </div>  

            </div>

         
        </main>
        </div>
        </body>
</html>
