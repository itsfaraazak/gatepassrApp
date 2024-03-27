<script>
	//Import local datatable components
	import ThSort from '$lib/components/ThSort.svelte';
	import ThFilter from '$lib/components/ThFilter.svelte';
	import Search from '$lib/components/Search.svelte';
	import RowsPerPage from '$lib/components/RowsPerPage.svelte';
	import RowCount from '$lib/components/RowCount.svelte';
	import Pagination from '$lib/components/Pagination.svelte';

	//Load local data
	import data from '$lib/data/api';

	//Import handler from SSD
	import { DataHandler } from '@vincjo/datatables';

	//Init data handler - CLIENT
	const handler = new DataHandler(data, { rowsPerPage: 5 });
	const rows = handler.getRows();
</script>

<div class=" overflow-x-auto space-y-4">
	<!-- Header -->
	<header class="flex justify-between gap-4">
		<Search {handler} />
		<RowsPerPage {handler} />
	</header>
	<!-- Table -->
	<table class="table table-hover table-compact w-full table-auto">
		<thead>
			<tr>
				<ThSort {handler} orderBy="student_name">Student</ThSort>
				<ThSort {handler} orderBy="student_grade">Grade</ThSort>
				<ThSort {handler} orderBy="approved_by">Status</ThSort>
                <ThSort {handler} orderBy="exit_time">Requested Exit Time</ThSort>
                <ThSort {handler} orderBy="approved_by">Actions</ThSort>

			</tr>
			<tr>
				<ThFilter {handler} filterBy="student_name" />
				<ThFilter {handler} filterBy="student_grade" />
                <ThFilter {handler} filterBy="approved_by" />
				<ThFilter {handler} filterBy="exit_time" />
			</tr>
		</thead>
		<tbody>
			{#each $rows as row}
				<tr>
					<td>{row.student_name}</td>
					<td>{row.student_grade}</td>
					<td>{row.approved_by}</td>
                    <td>{row.exit_time}</td>
                    <td>
                        {#if row.approved_by == null}
                        <button name="btnapprove" type="button" id={row.request_id}>Approve</button>
                        {:else}
                        <button name="btnreject" type="button" id={row.request_id}>Reject</button>
                        {/if}
                    </td>
                    



				</tr>
			{/each}
		</tbody>
	</table>
	<!-- Footer -->
	<footer class="flex justify-between">
		<RowCount {handler} />
		<Pagination {handler} />
	</footer>
</div>