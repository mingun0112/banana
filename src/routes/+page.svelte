<script lang="ts">
	import type { List } from 'postcss/lib/list';
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    import { itemStore, fileName } from '$lib/store';
    import { Wave } from 'svelte-loading-spinners';
	import { navigating } from '$app/stores'
    
    let bboxs: number[][] = [];
    let keypoints: number[][] = [];
    let num_keypoints: number;

    
    // import fs from "fs";

    let modal: HTMLInputElement;
    let imageSrc:string;
    let files: FileList;

    let path:string;
    let fileContent:JSON;

    let images:JSON;
    let annotations: JSON;
    let info:string;

    const annotationMap={};
    const keypointNumMap={};
    const bboxMap={};
    const imageMap={};
    const newMap={};
    

    let filepath: String;

    let characters = ['🍌', '🐒', '🙉','🙈','🐵','🍌'];

    let confetti = new Array(100).fill()
        .map((_, i) => {
            return {
                character: characters[i % characters.length],
                x: Math.random() * 100,
                y: -20 - Math.random() * 100,
                r: 0.1 + Math.random() * 1
            };
        })
        .sort((a, b) => a.r - b.r);

    onMount(()=>{
        let frame;

		function loop() {
			frame = requestAnimationFrame(loop);

			confetti = confetti.map(emoji => {
				emoji.y += 0.7 * emoji.r;
				if (emoji.y > 120) emoji.y = -20;
				return emoji;
			});
		}

		loop();

       
		return () => cancelAnimationFrame(frame);
    })


    const onFileSelect=(e)=>{
        let file = e.target.files[0];
        if (file){
            const reader=new FileReader();
            reader.onload = (e) => {

                fileContent = JSON.parse(e.target.result);
                fileName.set(file["name"])
                images=fileContent.images;
                annotations=fileContent.annotations;



                images.forEach(image => {
                    imageMap[image.id]=image.file_name;
                });

                annotations.forEach(annotation => {
                    const imageId = annotation.image_id;
                    // const keypointNum= annotation.num_keypoints;
                    if (!(imageId in annotationMap)) {
                        annotationMap[imageId] = [];
                        bboxMap[imageId]=[];
                        keypointNumMap[imageId]=[];
                    }
                    annotationMap[imageId].push(annotation.keypoints);
                    bboxMap[imageId].push(annotation.bbox);
                    keypointNumMap[imageId].push(annotation.num_keypoints)
                });

                //const newMap={};
                Object.keys(imageMap).forEach((id) => {
                    const imageName = imageMap[id];
                    const annotations = annotationMap[id];
                    const bbox=bboxMap[id];
                    const keypointNum=keypointNumMap[id];
                    newMap[imageName] = [keypointNum,annotations,bbox];
                });

                // console.log(newMap)                
                info=fileContent.info;
                
            };
            itemStore.set(newMap);
            
            console.log($itemStore);
            reader.readAsText(file);
            setTimeout(() => {
                goto('/main');
            }, 1500);
            
            
        }
    }


</script>

{#if (files)}
{#each confetti as c}
	<span class="cong_span" style="left: {c.x}%; top: {c.y}%; transform: scale({c.r})">{c.character}</span>
{/each}
{/if}

<div class="w-screen h-screen flex flex-col items-center justify-center">
    <div class="flex-none">
        <img src="banana.png" alt="logo" class="w-32 ml-5">
    </div>
    <div class="flex-none">
        <a class="btn btn-ghost text-stroke normal-case text-5xl text-yellow-300">Hi, I am 바나나!</a>
    </div>
    {#if (!files)}
        <div class="modal-box flex flex-col items-center justify-center mt-10">
                <h3 class="text-3xl font-bold">Your 파일을 올려주세요</h3>
                <!-- <h3 class="text-3xl font-bold">Upload your config file!</h3> -->
                <label for="dropzone-file" class="flex flex-col items-center justify-center w-full mt-12 h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
                <div class="flex flex-col items-center justify-center pt-5 pb-6">
                    <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
                    </svg>
                    <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to upload</span> or drag and drop</p>
                    <p class="text-xs text-gray-500 dark:text-gray-400">JSON (Only coco format)</p>
                </div>
                <input id="dropzone-file" on:change={(e)=>onFileSelect(e)} bind:files type="file" accept=".json" class="hidden" />
        </div>
    {:else}
        <div class="modal-box flex flex-col items-center justify-center mt-10">
            <Wave size="150" color="#f59e0b" unit="px" duration="1s" />
        </div>
    {/if}
    
</div>



<style>
    .text-stroke {
  -webkit-text-stroke: 2px #713f12;
  font-family: 'GangwonEduPowerExtraBoldA';
}

:global(body) {
		overflow: hidden;
	}

	.cong_span {
		position: absolute;
		font-size: 5vw;
		user-select: none;
	}


</style>