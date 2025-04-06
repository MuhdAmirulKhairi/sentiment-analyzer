<script>
   import DownloadButton from "./downloadButton.svelte"; // Imports download button

   export let sentiments = []; // Holds sentiment array of text and sentiments
   export let sortBy = "all"; // Determines which sentiment to show first

   // Reactive component to sort the array
   $: sortedSentiments = [...sentiments]

   // Sort based on the settings
   $: if (sortBy === "Positive") {
      sortedSentiments.sort((a, b) => {
         return a.sentiment === "positive" ? -1 : b.sentiment === "positive" ? 1 : 0;
      });
   }
   else if (sortBy === "Negative") {
      sortedSentiments.sort((a, b) => {
         return a.sentiment === "negative" ? -1 : b.sentiment === "negative" ? 1 : 0;
      });
   }
   else if (sortBy === "Neutral") {
      sortedSentiments.sort((a, b) => {
         return a.sentiment === "neutral" ? -1 : b.sentiment === "neutral" ? 1 : 0;
      });
   }

   // Convert table into a CSV file
   function downloadCSV() {
      let table = document.getElementById("sentiment-results-table");
      let rows = Array.from(table.querySelectorAll("tr"));

      // Converts table into CSV dataset
      let csv_content = "data:text/csv;charset=utf-8,";
      csv_content = csv_content + rows.map(row => {
         let cells = Array.from(row.querySelectorAll("th, td"));
         return cells.map(cell => `"${cell.innerText}"`).join(",");
      }).join("\n");

      // Creates link and trigger download
      let encoded = encodeURI(csv_content);
      let link = document.createElement("a");

      link.setAttribute("href", encoded);
      link.setAttribute("download", "sentiment_results.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
   }
</script>

<!-- Display table of sentiment results -->
<div id="sentiment-results-table">
   <div class="table-responsive">
      <div class="scrollable-table">
         <table class="table table-striped table-bordered">
            <thead class="table-dark">
               <tr>
                  <th class="col-8">Text</th>
                  <th>Labels</th>
               </tr>
            </thead>
            <tbody class="table-light">
               {#each sortedSentiments as s}
                  <tr>
                     <td>{s.text}</td>
                     <td>{s.sentiment}</td>
                  </tr>
               {/each}
            </tbody>
         </table>
      </div>
   </div>
   <DownloadButton download_link={downloadCSV}/> <!-- Attached download button -->
</div>

<style>
   #sentiment-results-table {
      padding: 25px;
   }

   .scrollable-table {
      max-height: 300px;
      overflow-y: auto;
      margin-bottom: 20px;
   }

   th {
      position: sticky;
      color: #f4f4f4;
      text-align: center;
      font-family: Roboto, Helvetica, sans-serif;
   }

   td {
      padding: 8px;
      text-align: center;
      font-family: Roboto, Helvetica, sans-serif;
   }
</style>