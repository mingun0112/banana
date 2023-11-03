import { w as writable } from "./index.js";
const itemStore = writable({});
const fileName = writable("");
const trashList = writable([]);
export {
  fileName as f,
  itemStore as i,
  trashList as t
};
