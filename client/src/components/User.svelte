import {page} from "$app/stores";

{#if $page.data.session}
<span>
    <small>Signed in as</small><br/>
    <strong>{$page.data.session.user?.name ?? "User"}</strong>
</span>
{/if}