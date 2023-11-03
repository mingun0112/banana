import { writable } from "svelte/store";

export const itemStore = writable<{}>({});
export const fileName =writable('');
// export const uuidStore = writable('');
// export const purchaseStatus = writable(0);
// export const pageIdx = writable(0);
// export const audioValue = writable([0,0]);