<script>
   import DownloadButton from "./downloadButton.svelte";
   import WordCloud from "wordcloud";
   import { onMount } from "svelte";
    import { draw } from "svelte/transition";

   export let wordCloud = [];
   let cloudCanvas;

   // Function to draw word cloud
   function drawWordCloud() {
      if (cloudCanvas && wordCloud && wordCloud.length > 0) {
         cloudCanvas.width = cloudCanvas.width; // Clear canvas
         WordCloud(cloudCanvas, {
            list: wordCloud.map(w => [w.word, w.count]),
            gridSize: 16,
            weightFactor: 5,
            color: "#000000",
            backgroundColor: "#ffffff",
            weightFactor: (size) => size * 0.5
         });
      }
   }

   // Run the function
   onMount(() => {
      drawWordCloud();
   })

   // Redraw if word cloud changes
   $: if (cloudCanvas && wordCloud && wordCloud.length > 0) {
      drawWordCloud();
   }
</script>


<div id="word-cloud">
   <canvas bind:this={cloudCanvas}></canvas>
   {#if wordCloud.length === 0}
      <p class="text-center">No words available.</p>
   {/if}
   <p class="text-center">Right click on the image to save to device.</p>
</div>

<style>
   #word-cloud {
      padding: 25px;
   }

   canvas {
      display: block;
      margin: auto auto;
      width: 80%;
      padding-bottom: 25px;
   }

   p {
      font-size: 25px;
      font-weight: bold;
   }

   @media screen and (max-width: 768px) {
      #word-cloud {
         padding: 10px;
      }

      canvas {
         padding: 5px;
      }

      p {
         font-size: 13px;
      }
   }
</style>