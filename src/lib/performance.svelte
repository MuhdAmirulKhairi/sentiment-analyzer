<script>
   import DownloadButton from "./downloadButton.svelte"; // Import download button

   export let performance; // Stores precision, recall, f1 score

   // Function to download as a CSV file
   function downloadCSV() {
      let table = document.getElementById("performance-table");
      let rows = Array.from(table.querySelectorAll("tr"));

      // Converts each row and cell into CSV format
      let csv_content = "data:text/csv;charset=utf-8,";
      csv_content = csv_content + rows.map(row => {
         let cells = Array.from(row.querySelectorAll("th, td"));
         return cells.map(cell => `"${cell.innerText}"`).join(",");
      }).join("\n");

      let encoded = encodeURI(csv_content);
      let link = document.createElement("a");

      // Trigger download
      link.setAttribute("href", encoded);
      link.setAttribute("download", "performance_results.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
   }
</script>

<!-- Performance section -->
<div id="performance-table">
   <table>
      <thead>
         <tr>
            <th class="col-12 fs-1">Metrics</th>
            <th class="right-align fs-1">Value</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td class="fs-2">Precision
               <!-- Tooltip --> 
               <p style="font-size:26px; display: inline;"
                  title="Measures how many predicted positives are correct">&#63;</p>
            </td>
            <td class="right-align fs-2">{performance?.precision?.toFixed(2) || 'N/A'}</td>
         </tr>
         <tr>
            <td class="fs-2">Recall 
               <!-- Tooltip --> 
               <p style="font-size:26px; display: inline;"
                  title="Measures how many actual positives are correctly identified">&#63;</p>
            </td>
            <td class="right-align fs-2">{performance?.recall?.toFixed(2) || 'N/A'}</td>
         </tr>
         <tr>
            <td class="fs-2">F1 Score 
               <!-- Tooltip --> 
               <p style="font-size:26px; display: inline;"
                  title="Evaluates system correctness and completeness in prediction">&#63;</p>
            </td>
            <td class="right-align fs-2">{performance?.f1_score?.toFixed(2) || 'N/A'}</td>
         </tr>
      </tbody>
   </table>
   <DownloadButton download_link={downloadCSV}/> <!-- Download button that triggers CSV export -->
</div>

<style>
   #performance-table {
      padding: 25px;
      font-family: Roboto, Helvetica, sans-serif;
   }

   .right-align {
      text-align: right;
   }
</style>