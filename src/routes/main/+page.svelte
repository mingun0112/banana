<script lang="ts">
	// import type { List } from 'postcss/lib/list';
    import { itemStore,fileName } from '$lib/store';
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';

    
    // let bboxs: number[][] = [];
    // let keypoints: number[][] = [];

    let imageSrc:string;
    let currentIndex=0;
    //const $itemStore={};
    let filepath: String;
    let filevalue: String;
    let mainCanvas: HTMLCanvasElement;

    let keys: string[] = [];
    let value: number[][][] = [];
    let bboxs: number[][] = [];
    let keypoints: number[][] = [];
    let num_keypoints: number;

    let ctx: CanvasRenderingContext2D;

    let pallette=['red','orange','yellow','green','blue','indigo','purple'];
    //let pallette=['#008080','#FFD700','#4169E1','#C0C0C0','#50C878','#2E0854','#FF6EC7']
    let colorpicker:number;
    let filter = false;

    const toggleFilter=async()=>{
        filter = !filter;
        const res = await fetch('http://192.168.0.160:9900/filter', {
            method: 'POST',
            body: JSON.stringify({filter}),
        })
        if (res.status === 200) {
            const responseText = await res.json();
            console.log("success",responseText["filter"])
        }else {

        console.error('POST 요청 실패');
        }
        
        console.log(filter)
    }


    

    const loadItemData = () => {
        keys = Object.keys($itemStore);
        value = Object.values($itemStore);
        console.log("test")

        if (keys.length > 0) {
            num_keypoints=value[currentIndex][0]
            bboxs = value[currentIndex][2];
            keypoints = value[currentIndex][1];
        }
    }

    const postServer = async() => {
        if (keys.length > 0) {
        filepath=keys[currentIndex];
        filevalue=value[currentIndex];

        const res = await fetch('http://192.168.0.160:9900/post', {
            method: 'POST',
            body: JSON.stringify({filepath, filevalue}),
        })

        if (res.status === 200) {
            const responseText = await res.json();
            imageSrc = `data:image/jpg;base64,${responseText["message"]}`;
            console.log("success",{filepath});
            // console.log(imageSrc);

        } else {

            console.error('POST 요청 실패');
        }}
    }

    


    const onNextClick = () => {

        if (currentIndex < keys.length - 1){
            currentIndex++; 
            postServer();
            loadItemData();
            // mainRender();
        }
        else{
            currentIndex=0;
            postServer();
            loadItemData();
            // mainRender();
        }
            

        
    }
    
    const onPrevClick = () => {
        if (currentIndex>0){
            currentIndex--; 
            postServer();
            loadItemData();
            // mainRender();
        }
        else{
            currentIndex=keys.length-1;
            postServer();
            loadItemData();
            // mainRender();
        }

    }

    // const mainRender = () => {

    //         ctx?.clearRect(0, 0, mainCanvas.width, mainCanvas.height);
    //         if (bboxs){
    //             bboxs.forEach((bbox)=>{
    //                 ctx.strokeRect(bbox[0]*0.66, bbox[1]*0.66, bbox[2]*0.66, bbox[3]*0.66);
    //             })
                
    //         }
    //         if (keypoints){
    //             keypoints.forEach((keypoint)=>{
    //                 colorpicker=0;
                    
    //                 for (let i = 0; i < keypoint.length; i += 3) {
                    
    //                 const x = keypoint[i];
    //                 const y = keypoint[i + 1];
    //                 const confidence = keypoint[i + 2];

    //                 if (confidence === 2) {
    //                     ctx.beginPath();
    //                     ctx.arc(x*0.66, y*0.66, 5, 0, 2 * Math.PI);
    //                     ctx.fillStyle=pallette[colorpicker];
    //                     ctx.fill();
    //                 }
    //                 colorpicker++;
    //             }

    //             })
                
    //         }
    //     }

    const goHomeClick=()=>{
        goto('/');
        itemStore.set({});
    }

    function handleRangeChange(event) {
        currentIndex = event.target.value;
        postServer();
        loadItemData();
    }

    onMount(() => {

        loadItemData();
        postServer();

        console.log(filter);
        

        // js rendering option
        // const canvas = mainCanvas.getContext("2d");
        // ctx = canvas;
        // canvas.lineWidth = 5;
        // mainRender();


        

        });

    
</script>


<div class="navbar bg-base-100">
    <div class="flex-none">
        <div class="dropdown dropdown-end ">
            <label tabindex="0" class="btn btn-ghost btn-circle avatar">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-5 h-5 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
            </label>
            <ul tabindex="0" class="menu dropdown-content bg-base-200 rounded-box absolute">
                <li>
                    <a on:click={goHomeClick}>
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" /></svg>
                        
                    </a>
                </li>
                <li>
                    <a>
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                    </a>
                </li>
                <li>
                    <a>
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg>
                    </a>
                </li>
            </ul>
        </div>
    </div>
    <div class="flex-none">
        <img src="banana.png" alt="logo" class="w-9 ml-5">
    </div>
    <div class="flex-1">
      <a class="btn btn-ghost text-stroke normal-case text-3xl text-yellow-300">Banana</a>
    </div>
    <div class="flex-none dropdown dropdown-end">
        <button tabindex="0" class="btn btn-square btn-ghost">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-5 h-5 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z"></path></svg>
        </button>
        <ul tabindex="0" class="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52">
          <li>
            <a class="justify-between">
              Profile
              <span class="badge">New</span>
            </a>
          </li>
          <li><a>Settings</a></li>
          <li><a>Logout</a></li>
        </ul>
      </div>

  </div>

<div>

</div>
<div class="flex flex-col ">
    <div class="flex justify-center">
        <p>{$fileName}</p>
    </div>
    <div class="flex justify-center">
        <div class="form-control">
            <label class="label cursor-pointer">
            <span class="label-text">Filtering</span> 
            <input type="checkbox" class="toggle ml-5"  on:change={toggleFilter}/>
            </label>
        </div>
    </div>
</div>
<div class="flex justify-center">
    <div class="justify-center">
        <div class="join grid grid-cols-3">
            <button on:click={onPrevClick} class="join-item btn btn-outline">Previous page</button>
            <div class=" dropdown dropdown-end">
                <button  tabindex="0" class="join-item  btn w-full">Page {currentIndex}</button>
                <ul tabindex="0" class="z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-full">
                    <li>
                        <input type="range" min="0" max={keys.length-1} value={currentIndex} class="range w-full" on:input={handleRangeChange}/>
                    </li>
                </ul>
            </div>
            
            
            <button  on:click={onNextClick} class="join-item btn btn-outline">Next</button>
        </div>

        <!-- <label>{currentIndex}</label>
        <label>{keys.length}</label> -->
        <!--{#each bboxs as bbox}
            <p>X: {bbox[0]}, Y: {bbox[1]}, Width: {bbox[2]}, Height: {bbox[3]}</p>
        {/each}
        {#each keypoints as keypoint}
            <p>{keypoint}</p>
        {/each} -->

        <!-- <label>{currentIndex < Object.keys($itemStore).length ? Object.keys($itemStore)[currentIndex] : 'No data'}</label>
        <label>{currentIndex < Object.keys($itemStore).length ? Object.values($itemStore)[currentIndex] : 'No data'}</label> -->
        <div class='relative w-full h-full mt-12'>
            <img src={imageSrc} alt="map" width="1280" height="720" >
            <!-- js rendering option -->
            <!-- <canvas id='mainCanvas' bind:this={mainCanvas} class="absolute top-0 left-0"  width="1280" height="720" ></canvas> -->
            <div class="absolute top-0 left-0 grid grid-cols-2 top-0 left-0 w-full h-full" >
                <button on:click={onPrevClick} ></button>
                <button on:click={onNextClick}></button>
            </div>
        </div>
        

    </div>

</div>

<style>
    .text-stroke {
  -webkit-text-stroke: 1px #713f12;
}


</style>