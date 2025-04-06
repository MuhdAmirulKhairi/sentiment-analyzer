<script>
   import DownloadButton from "./downloadButton.svelte"; // Import download button
   import { onMount } from "svelte";
   import { draw } from "svelte/transition";

   export let wordCloud = []; // Holds word frequency data
   let cloudCanvas; // HTML canvas
   let WordCloud; // Placeholder for word cloud

   // Function to draw word cloud
   async function drawWordCloud() {
      if (cloudCanvas && wordCloud && wordCloud.length > 0) {
         cloudCanvas.width = cloudCanvas.width; // Clear canvas

         // Improving resolution
         const dpr = window.devicePixelRatio || 1;
         const rect = cloudCanvas.getBoundingClientRect();
         cloudCanvas.width = rect.width * dpr;
         cloudCanvas.height = rect.height * dpr;

         const ctx = cloudCanvas.getContext("2d");
         ctx.scale(dpr, dpr);

         // Render word cloud
         WordCloud(cloudCanvas, {
            list: wordCloud.map(w => [w.word, w.count]),
            gridSize: Math.round(16 * (rect.width / 1024)),
            weightFactor: (count) => Math.log2(count + 2) * 10,
            fontFamily: "Roboto, Helvetica, san-serif",
            color: function (word, weight) {
               // Add gradient
               const hue = Math.round(240 - weight * 2);
               return `hsl(${hue}, 80%, 50%)`;
            },
            backgroundColor: "#d9d9d9",
            rotateRatio: 0.1,
            rotationSteps: 2,
            drawOutOfBound: false,
            shrinkToFit: true
         });
      }
   }

   // Load word cloud library
   onMount(async () => {
      const module = await import("wordcloud"); // Dynamically import word cloud library
      WordCloud = module.default || module;
      drawWordCloud();
   })

   // Redraw if word cloud changes
   $: if (cloudCanvas && wordCloud && wordCloud.length > 0) {
      drawWordCloud();
   }

   // Download word cloud as png
   function downloadWordCloud() {
      const link = document.createElement('a');
      link.download = 'wordcloud.png';
      link.href = cloudCanvas.toDataURL("image/png");
      link.click();
   }
</script>

<!-- Word cloud section -->
<div id="word-cloud">
   <canvas bind:this={cloudCanvas}></canvas> <!-- Canvas where word cloud is-->
   {#if wordCloud.length === 0}
      <p class="text-center">No words available.</p> <!-- Fallback message -->
   {/if}
   <DownloadButton download_link={downloadWordCloud} /> <!-- Download button -->
</div>

<style>
   #word-cloud {
      padding: 25px;
      border-radius: 20px;
   }

   canvas {
      display: block;
      margin: auto auto;
      width: 100%;
      max-width: 800px;
      height: 500px;
      border: 1px solid #ddd;
      border-radius: 10px;
      background-color: #d9d9d9;
      margin-bottom: 20px;
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