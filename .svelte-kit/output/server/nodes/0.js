import * as universal from '../entries/pages/_layout.ts.js';

export const index = 0;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/_layout.svelte.js')).default;
export { universal };
export const universal_id = "src/routes/+layout.ts";
export const imports = ["_app/immutable/nodes/0.1a96d52a.js","_app/immutable/chunks/scheduler.54e97ece.js","_app/immutable/chunks/index.bf1713da.js"];
export const stylesheets = ["_app/immutable/assets/app.4c6be7a4.css"];
export const fonts = [];
