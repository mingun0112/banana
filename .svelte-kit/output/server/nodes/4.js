

export const index = 4;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/main/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/4.59fd0452.js","_app/immutable/chunks/scheduler.54e97ece.js","_app/immutable/chunks/index.bf1713da.js","_app/immutable/chunks/store.29d5135c.js","_app/immutable/chunks/singletons.bc90f49e.js"];
export const stylesheets = ["_app/immutable/assets/4.9b597229.css"];
export const fonts = [];
