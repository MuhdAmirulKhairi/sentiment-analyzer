<script>
   import DownloadButton from "./downloadButton.svelte";

   export let sentiments = [];
   export let sortBy = "all";

   // Sort based on sorting settings
   $: sortedSentiments = [...sentiments]

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

   function downloadCSV() {
      let table = document.getElementById("sentiment-results-table");
      let rows = Array.from(table.querySelectorAll("tr"));

      let csv_content = "data:text/csv;charset=utf-8,";
      csv_content = csv_content + rows.map(row => {
         let cells = Array.from(row.querySelectorAll("th, td"));
         return cells.map(cell => `"${cell.innerText}"`).join(",");
      }).join("\n");

      let encoded = encodeURI(csv_content);
      let link = document.createElement("a");

      link.setAttribute("href", encoded);
      link.setAttribute("download", "sentiment_results.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
   }
</script>

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
   <DownloadButton download_link={downloadCSV}/>
</div>

<style>
   #sentiment-results-table {
      padding: 25px;
   }

   .scrollable-table {
      max-height: 300px;
      overflow-y: auto;
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