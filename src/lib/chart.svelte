<script>
   import { onMount } from "svelte";
   import Chart from "chart.js/auto";

   // Declare sentiment counts and canvas element for chart rendering
   export let sentimentCounts;
   let chartCanvas;

   onMount(() => {
      // Initialize a new bar chart after the component mounts
      new Chart(chartCanvas, {
         type: "bar", // Set chart type to 'bar'
         data: {
            labels: ["Positive", "Negative", "Neutral"], // Sentiment labels
            datasets: [{
               label: "Sentiment Counts", // Data label for the chart
               data: [sentimentCounts.positive, sentimentCounts.negative, sentimentCounts.neutral], // Sentiment values
               backgroundColor: ["green", "red", "gray"] // Colors for each sentiment category
            }]
         },
         options: {
            responsive: true, // Ensure chart is responsive
            maintainAspectRatio: false, // Allow aspect ratio to adjust
            scales: {
               x: {
                  grid: { color: "white" }, // White grid lines on the x-axis
                  ticks: { color: "white" } // White tick marks on the x-axis
               },
               y: {
                  grid: { color: "white"}, // White grid lines on the y-axis
                  ticks: { color: "white"} // White tick marks on the y-axis
               }       
            }
         }
      });  
   });
</script>

<div id="chart">
   <!-- Canvas element for rendering the chart -->
   <canvas bind:this={chartCanvas}></canvas>
   <p class="text-center">Right click on the image to save to device.</p>
</div>

<style>
   #chart {
      padding: 20px;
      padding-bottom: 75px;
      width: 100%;
      max-width: 100%;
      height: 500px;
      position: relative;
   }

   canvas {
      display: block;
      margin: auto auto;
      width: 100% !important;
      height: 100% !important;
      padding-bottom: 25px;
   }

   p {
      font-size: 25px;
      font-weight: bold;
   }

   /* Responsive design for smaller screens */
   @media screen and (max-width: 768px) {
      #chart {
         padding: 10px;
         height: 250px;
      }

      canvas {
         padding: 5px;
      }

      p {
         font-size: 13px;
      }
   }
</style>