<script lang="ts">
	import type { DataHandler } from '@vincjo/datatables';

	export let handler: DataHandler;
	export let orderBy: string;

	export let align: 'left' | 'right' | 'center' = 'left'
	export let identifier = orderBy?.toString()
	export let rowSpan: number = 1

	const sorted = handler.getSort();
</script>

<th on:click={() => handler.sort(orderBy)}     
	class:sortable={orderBy}
    class:active={$sorted.identifier === identifier}
    class={$$props.class ?? 'cursor-pointer select-none'}
    rowspan={rowSpan}
	>
    <div
        class="flex"
        style:justify-content={align === 'left' ? 'flex-start' : align === 'right' ? 'flex-end' : 'center'}
    >
	<div class="flex h-full items-center justify-start gap-x-2">
		<slot />
		{#if $sorted.identifier === orderBy}
			{#if $sorted.direction === 'asc'}
				&darr;
			{:else if $sorted.direction === 'desc'}
				&uarr;
			{/if}
		{:else}
			&updownarrow;
		{/if}
	</div>
</th>