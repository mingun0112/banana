

export const index = 1;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/fallbacks/error.svelte.js')).default;
export const imports = ["_app/immutable/nodes/1.1149a021.js","_app/immutable/chunks/scheduler.54e97ece.js","_app/immutable/chunks/index.bf1713da.js","_app/immutable/chunks/singletons.bc90f49e.js"];
export const stylesheets = [];
export const fonts = [];
