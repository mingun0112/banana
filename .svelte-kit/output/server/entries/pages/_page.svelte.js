import { c as create_ssr_component, a as subscribe } from "../../chunks/ssr.js";
import { i as itemStore } from "../../chunks/store.js";
const Circle_svelte_svelte_type_style_lang = "";
const Circle2_svelte_svelte_type_style_lang = "";
const Circle3_svelte_svelte_type_style_lang = "";
const DoubleBounce_svelte_svelte_type_style_lang = "";
const GoogleSpin_svelte_svelte_type_style_lang = "";
const ScaleOut_svelte_svelte_type_style_lang = "";
const SpinLine_svelte_svelte_type_style_lang = "";
const Stretch_svelte_svelte_type_style_lang = "";
const BarLoader_svelte_svelte_type_style_lang = "";
const Jumper_svelte_svelte_type_style_lang = "";
const RingLoader_svelte_svelte_type_style_lang = "";
const SyncLoader_svelte_svelte_type_style_lang = "";
const Rainbow_svelte_svelte_type_style_lang = "";
const Firework_svelte_svelte_type_style_lang = "";
const Pulse_svelte_svelte_type_style_lang = "";
const Jellyfish_svelte_svelte_type_style_lang = "";
const Chasing_svelte_svelte_type_style_lang = "";
const Square_svelte_svelte_type_style_lang = "";
const Shadow_svelte_svelte_type_style_lang = "";
const Moon_svelte_svelte_type_style_lang = "";
const Plane_svelte_svelte_type_style_lang = "";
const Diamonds_svelte_svelte_type_style_lang = "";
const Clock_svelte_svelte_type_style_lang = "";
const Wave_svelte_svelte_type_style_lang = "";
const Puff_svelte_svelte_type_style_lang = "";
const ArrowDown_svelte_svelte_type_style_lang = "";
const ArrowUp_svelte_svelte_type_style_lang = "";
const _page_svelte_svelte_type_style_lang = "";
const css = {
  code: ".text-stroke.svelte-za6cn6{-webkit-text-stroke:2px #713f12;font-family:'GangwonEduPowerExtraBoldA'}body{overflow:hidden}.cong_span.svelte-za6cn6{position:absolute;font-size:5vw;user-select:none}",
  map: null
};
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $$unsubscribe_itemStore;
  $$unsubscribe_itemStore = subscribe(itemStore, (value) => value);
  let characters = ["🍌", "🐒", "🙉", "🙈", "🐵", "🍌"];
  new Array(100).fill().map((_, i) => {
    return {
      character: characters[i % characters.length],
      x: Math.random() * 100,
      y: -20 - Math.random() * 100,
      r: 0.1 + Math.random() * 1
    };
  }).sort((a, b) => a.r - b.r);
  $$result.css.add(css);
  $$unsubscribe_itemStore();
  return `${``} <div class="w-screen h-screen flex flex-col items-center justify-center"><div class="flex-none" data-svelte-h="svelte-1lwiol3"><img src="banana.png" alt="logo" class="w-32 ml-5"></div> <div class="flex-none mt-8" data-svelte-h="svelte-1o8uabm"><a class="btn btn-ghost text-stroke normal-case text-5xl text-yellow-300 svelte-za6cn6">Hi, I am 바나나 입니다!</a></div> ${`<div class="modal-box flex flex-col items-center justify-center mt-10"><h3 class="text-3xl font-bold" data-svelte-h="svelte-17jm9q4">Your 파일을 올려주세요</h3>  <label for="dropzone-file" class="flex flex-col items-center justify-center w-full mt-12 h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600"><div class="flex flex-col items-center justify-center pt-5 pb-6" data-svelte-h="svelte-nq8n38"><svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"></path></svg> <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to upload</span> or drag and drop</p> <p class="text-xs text-gray-500 dark:text-gray-400">JSON (Only coco format)</p></div> <input id="dropzone-file" type="file" accept=".json" class="hidden"></label></div>`} </div>`;
});
export {
  Page as default
};
