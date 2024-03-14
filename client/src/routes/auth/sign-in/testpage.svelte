

<div class="signin">
    <div class="card">
        <div class="provider">
            <form action="http://localhost:5173/auth/signin/github" method="POST">
                <input type="hidden" name="csrfToken" value="8962b54fbf0a6f441e1a8b906085ee286997b6f51a13ebb6b9e38e2685f772ff">
                <input type="hidden" name="callbackUrl" value="http://localhost:5173/auth/sign-in">
                <button type="submit" class="button" style="--provider-bg: #24292f; --provider-dark-bg: #24292f; --provider-color: #fff; --provider-dark-color: #fff; --provider-bg-hover: rgba(36, 41, 47, 0.8); --provider-dark-bg-hover: rgba(36, 41, 47, 0.8);" tabindex="0">
                    <img loading="lazy" height="24" width="24" id="provider-logo" src="https://authjs.dev/img/providers/github.svg">
                    <img loading="lazy" height="24" width="24" id="provider-logo-dark" src="https://authjs.dev/img/providers/github.svg">
                    <span>Sign in with GitHub</span></button></form></div><div class="provider">
            <form action="http://localhost:5173/auth/signin/google" method="POST">
                <input type="hidden" name="csrfToken" value="8962b54fbf0a6f441e1a8b906085ee286997b6f51a13ebb6b9e38e2685f772ff">
                <input type="hidden" name="callbackUrl" value="http://localhost:5173/auth/sign-in">
                <button type="submit" class="button" style="--provider-bg: #fff; --provider-dark-bg: #fff; --provider-color: #000; --provider-dark-color: #000; --provider-bg-hover: rgba(255, 255, 255, 0.8); --provider-dark-bg-hover: rgba(255, 255, 255, 0.8);" tabindex="0"><img loading="lazy" height="24" width="24" id="provider-logo" src="https://authjs.dev/img/providers/google.svg"><img loading="lazy" height="24" width="24" id="provider-logo-dark" src="https://authjs.dev/img/providers/google.svg"><span>Sign in with Google</span></button></form></div><div class="provider"><form action="http://localhost:5173/auth/signin/azure-ad" method="POST"><input type="hidden" name="csrfToken" value="8962b54fbf0a6f441e1a8b906085ee286997b6f51a13ebb6b9e38e2685f772ff"><input type="hidden" name="callbackUrl" value="http://localhost:5173/auth/sign-in"><button type="submit" class="button" style="--provider-bg: #0072c6; --provider-dark-bg: #0072c6; --provider-color: #fff; --provider-dark-color: #fff; --provider-bg-hover: rgba(0, 114, 198, 0.8); --provider-dark-bg-hover: rgba(0, 114, 198, 0.8);" tabindex="0"><img loading="lazy" height="24" width="24" id="provider-logo" src="https://authjs.dev/img/providers/azure.svg"><img loading="lazy" height="24" width="24" id="provider-logo-dark" src="https://authjs.dev/img/providers/azure.svg"><span>Sign in with Azure Active Directory</span></button></form></div></div></div>