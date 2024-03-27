<script>
    import Datatable from '$lib/components/Datatable.svelte';
</script>


<div class="mx-4 mt-16 py-6 sm:mx-12">
    <div class="mx-4 my-2 lg:flex lg:items-center lg:justify-between">
    </div>
    <!-- page header -->
    <div class="mx-4 mt-8 mb-6 lg:flex lg:items-center lg:justify-between">
      
      <div class="min-w-0 flex-1">
        <h2 class="text-3xl font-bold leading-7 text-primary sm:truncate sm:text-3xl sm:tracking-tight">Pending Requests</h2>
      </div>
      <div class="mt-5 flex lg:ml-4 lg:mt-0">
        <span class="block">
        </span>
                
      </div> 
    </div>
        <Datatable />

</div>
