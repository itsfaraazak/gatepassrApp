import { gatepassrAPI } from "$lib/gatepassrAPI"

import type { State } from '@vincjo/datatables/remote';

let data = [];

export const reload = async (state: State) => {
	const response = await fetch(gatepassrAPI +`/recieve/fancy?${getParams(state)}`);
	return response.json();
};

const getParams = (state: State) => {
	const { pageNumber, rowsPerPage, sort, filters, search } = state;

	let params = `_page=${pageNumber}`;

	if (rowsPerPage) {
		params += `&_limit=${rowsPerPage}`;
	}
	if (sort) {
		params += `&_sort=${sort.orderBy}&_order=${sort.direction}`;
	}
	if (filters) {
		params += filters.map(({ filterBy, value }) => `&${filterBy}=${value}`).join();
	}
	if (search) {
		params += `&q=${search}`;
	}
	return params;
};

/* const fetchRequests = async()=> {
    const requestsRes = await fetch(gatepassrAPI +"/recieve/fancy")
    const requestsdata =  await requestsRes.json();
    return requestsdata;
    }
      
export default data = await fetchRequests()
 */