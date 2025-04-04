<script>
   import DownloadButton from "./downloadButton.svelte";
   import WordCloud from "wordcloud";
   import { onMount } from "svelte";

   export let wordCloud = [];
   let cloudCanvas;

   // Re-run the word cloud drawing when wordCloud data changes
   $: {
      if(wordCloud && wordCloud.length > 0) {
         WordCloud(cloudCanvas, {
            list: wordCloud.map(w => [w.word, w.count]),
            gridSize: 16,
            weightFactor: 5,
            color: "#000000",
            backgroundColor: "#ffffff"
         });
      }
   }

   // Clear the canvas before drawing a new word cloud
   onMount(() => {
      if (cloudCanvas) {
         cloudCanvas.width = cloudCanvas.width; // Clears the canvas
      }
   })
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