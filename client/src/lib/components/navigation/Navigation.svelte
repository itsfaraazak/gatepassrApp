<script lang=ts>
    import { LightSwitch, getDrawerStore } from "@skeletonlabs/skeleton";

    const drawerStore = getDrawerStore();

    function drawerClose(): void {
        drawerStore.close();
    }

    export let layout;

</script>

<!-- TODO: different nav based on user role, to be done after roles are implemented -->

{#if layout == "vertical"}

<nav class="list-nav p-4">
	<ul>
        <li><a href="/home" on:click={drawerClose}>Home</a></li>
        <li><a href="/" on:click={drawerClose}>About</a></li>
        <li><a href="/blog" on:click={drawerClose}>Blog</a></li>
        <li><a href="/about-us" on:click={drawerClose}>About</a></li>
	</ul>
    <LightSwitch class="absolute bottom-0 my-8 mx-2"/>
</nav>

{:else}
    <a href="/home" class="text-sm font-semibold leading-6 text-primary">Home</a>
    <a href="#" class="text-sm font-semibold leading-6 text-primary">Features</a>
    <a href="/blog" class="text-sm font-semibold leading-6 text-primary">Blog</a>
    <a href="/about-us" class="text-sm font-semibold leading-6 text-primary">About</a>

{/if}

<!-- 
<nav class="list-nav p-4">
	<ul>
        <li><a href="/" on:click={drawerClose}>Homepage</a></li>
        <li><a href="/about" on:click={drawerClose}>About</a></li>
        <li><a href="/blog" on:click={drawerClose}>Blog</a></li>
        <li><a href="/contact" on:click={drawerClose}>Contact</a></li>
	</ul>
</nav> -->