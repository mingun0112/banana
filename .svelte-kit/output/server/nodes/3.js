

export const index = 3;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/3.e3f661e0.js","_app/immutable/chunks/scheduler.54e97ece.js","_app/immutable/chunks/index.bf1713da.js","_app/immutable/chunks/store.29d5135c.js","_app/immutable/chunks/singletons.bc90f49e.js"];
export const stylesheets = ["_app/immutable/assets/3.c54cf66e.css"];
export const fonts = [];
