<script>
   import DownloadButton from "./downloadButton.svelte";
   import WordCloud from "wordcloud";

   export let wordCloud;
   let cloudCanvas;

   $: wordCloud.length > 0 && WordCloud(cloudCanvas, {
      list: wordCloud.map(w => [w.word, w.count]),
      gridSize: 16,
      weightFactor: 5
   });
</script>


<div id="word-cloud">
   <canvas bind:this={cloudCanvas}></canvas>
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