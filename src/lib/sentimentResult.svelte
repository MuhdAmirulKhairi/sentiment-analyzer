<script>
   import DownloadButton from "./downloadButton.svelte";

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
                  <th>Sentiment</th>
                  <th>Labels</th>
               </tr>
            </thead>
            <tbody class="table-light">
               <tr>
                  <td>Text</td>
                  <td>Sentiment</td>
                  <td>Labels</td>
               </tr>
               <tr>
                  <td>Text</td>
                  <td>Sentiment</td>
                  <td>Labels</td>
               </tr>
               <tr>
                  <td>Text</td>
                  <td>Sentiment</td>
                  <td>Labels</td>
               </tr>
               <tr>
                  <td>Text</td>
                  <td>Sentiment</td>
                  <td>Labels</td>
               </tr>
               <tr>
                  <td>Text</td>
                  <td>Sentiment</td>
                  <td>Labels</td>
               </tr>
               <tr>
                  <td>Text</td>
                  <td>Sentiment</td>
                  <td>Labels</td>
               </tr>
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