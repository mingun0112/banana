<script lang="ts">
	import type { List } from 'postcss/lib/list';
    import { onMount } from 'svelte';

    
    let bboxs: number[][] = [];
    let keypoints: number[][] = [];

    
    // import fs from "fs";

    let modal: HTMLInputElement;
    let imageSrc:string;
    let files: FileList;

    let path:string;
    let fileContent:JSON;

    let images:JSON;
    let annotations: JSON;
    let info:string;

    let currentIndex=0;
    const annotationMap={};
    const bboxMap={};
    const imageMap={};
    const newMap={};
    

    let filepath: String;


    let mainCanvas: HTMLCanvasElement;
	let context

    const onNextClick = async() => {
        const keys = Object.keys(newMap);
        const value=Object.values(newMap)[currentIndex];
        bboxs=value[1];
        keypoints=value[0];
        console.log(value[0])

        if (currentIndex < keys.length - 1) {

            
            filepath=keys[currentIndex];

        const res = await fetch('http://192.168.0.160:9900/post', {
            method: 'POST',
            body: JSON.stringify({filepath}),
        })


        if (res.status === 200) {
            const responseText = await res.json();

            
            imageSrc = `data:image/jpg;base64,${responseText["message"]}`;

        } else {

            console.error('POST 요청 실패');
        }
            currentIndex++; 
        }
    }
    

    const onPrevClick = async() => {

        const keys = Object.keys(newMap);
        const value=Object.values(newMap)[currentIndex];
        bboxs=value[1];
        keypoints=value[0];
        console.log(value[0])

        if (currentIndex < keys.length - 1) {

            
            filepath=keys[currentIndex];

        const res = await fetch('http://192.168.0.160:9900/post', {
            method: 'POST',
            body: JSON.stringify({filepath}),
        })


        if (res.status === 200) {
 
            const responseText = await res.json();

            
            imageSrc = `data:image/jpg;base64,${responseText["message"]}`;

        } else {

            console.error('POST 요청 실패');
        }
        currentIndex--; 
        }
    }

    const onFileSelect=(e)=>{
        let file = e.target.files[0];
        if (file){
            const reader=new FileReader();
            reader.onload = (e) => {

                fileContent = JSON.parse(e.target.result);

                images=fileContent.images;
                annotations=fileContent.annotations;



                images.forEach(image => {
                    imageMap[image.id]=image.file_name;
                });

                annotations.forEach(annotation => {
                    const imageId = annotation.image_id;
                    if (!(imageId in annotationMap)) {
                        annotationMap[imageId] = [];
                        bboxMap[imageId]=[];
                    }
                    annotationMap[imageId].push(annotation.keypoints);
                    bboxMap[imageId].push(annotation.bbox);
                });

                //const newMap={};
                Object.keys(imageMap).forEach((id) => {
                    const imageName = imageMap[id];
                    const annotations = annotationMap[id];
                    const bbox=bboxMap[id];
                    newMap[imageName] = [annotations,bbox];
                });

                // console.log(newMap)                
                info=fileContent.info;
                
            };
            reader.readAsText(file);
        }
    }


    onMount(() => {
        // modal.click();
        if(!files){
            modal.click();
            console.log("not");
        }

        const ctx = mainCanvas.getContext("2d");
        ctx.fillStyle = "orange";
        ctx.lineWidth = 1;
        const mainRender = () => {
            ctx?.clearRect(0, 0, canvas.width, canvas.height);
            if (bboxs){
                bboxs.forEach((bbox)=>{
                    ctx?.strokeRect(bbox[0], bbox[1], bbox[2], bbox[3]);
                    console.log(bbox)
                })
                
            }
        }
        mainRender();
        });
        
    // let rand = -1;

    // function getRand() {
    //   fetch("./rand")
    //     .then(d => d.text())
    //     .then(d => (rand = d));
    // }
</script>

  

<input
	type="checkbox"
	id="errorModal"
	bind:this={modal}
	class="modal-toggle"
/>



<button on:click={onNextClick} class="btn">Forward</button>
<button on:click={onPrevClick} class="btn">Backward</button>
<label>{currentIndex < Object.keys(newMap).length ? Object.keys(newMap)[currentIndex] : 'No data'}</label>
<label>{currentIndex < Object.keys(newMap).length ? Object.values(newMap)[currentIndex] : 'No data'}</label>
<div class='relative'>
    <img src={imageSrc} alt="Image">
    <canvas id='canvas' bind:this={mainCanvas} class="absolute top-0 left-0 w-full h-full"></canvas>
</div>
{#each bboxs as bbox}
    <p>X: {bbox[0]}, Y: {bbox[1]}, Width: {bbox[2]}, Height: {bbox[3]}</p>
{/each}
{#each keypoints as keypoint}
    <p>{keypoint}</p>
{/each}

{#if !files}
<dialog id="my_modal_2" class="modal">
    <div class="modal-box flex flex-col items-center justify-center">
        <h3 class="text-3xl font-bold">Upload your config file!</h3>
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
    <!-- <form method="dialog" class="modal-backdrop">
      <button>close</button>
    </form> -->
</dialog>
{/if}