<script>
   import { onMount } from "svelte";
   import Chart from "chart.js/auto";

   export let sentimentCounts;
   let chartCanvas;

   onMount(() => {
      new Chart(chartCanvas, {
         type: "bar",
         data: {
            labels: ["Positive", "Negative", "Neutral"],
            datasets: [{
               label: "Sentiment Counts",
               data: [sentimentCounts.positive, sentimentCounts.negative, sentimentCounts.neutral],
               backgroundColor: ["green", "red", "gray"]
            }]
         },
         options: {
            scales: {
               x: {
                  grid: { color: "white" },
                  ticks: { color: "white" }
               },
               y: {
                  grid: { color: "white"},
                  ticks: { color: "white"}
               }       
            }
         }
      });  
   });
</script>

<div id="chart">
   <canvas bind:this={chartCanvas}></canvas>
   <p class="text-center">Right click on the image to save to device.</p>
</div>

<style>
   #chart {
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
      #chart {
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