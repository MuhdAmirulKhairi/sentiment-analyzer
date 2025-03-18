<script>
   import Papa from "papaparse";
   import { CSVdata } from "$lib/stores";

   let selectedColumns = ["text", "sentiment"] // Specified the columns to be displayed

   function handleFileUploads(event) {
      const uploadedFile = event.target.files[0];

      if (uploadedFile) {
         const reader = new FileReader();
         
         reader.onload = (x) => {
            const CSVtexts = x.target.result;

            Papa.parse(CSVtexts, {
               header: true,
               skipEmptyLines: true,
               complete: function(result) {
                  // Filter unwanted columns
                  CSVdata.set(result.data
                                    .filter(row => row.text && row.sentiment)
                                    .map(row => ({
                                       text: row.text,
                                       sentiment: row.sentiment || "Unknown"
                                    }))
                  );
               },
            });
         };

         reader.readAsText(uploadedFile);
      }
   }
</script>

<input
   type="file" 
   id="csv-file-upload"
   class="form-control col"
   accept=".csv"
   required
   on:change={handleFileUploads}
/>
<div id="CSVTable">
   {#if $CSVdata.length > 0}
   <div class="table-responsive">
      <div class="scrollable-table">
         <table class="table table-striped table-bordered">
            <thead class="table-dark">
               <tr>
                  <th>Text</th>
                  <th>Sentiment</th>
               </tr>
            </thead>
            <tbody class="table-light">
               {#each $CSVdata as row}
                  <tr>
                     <td>{row.text}</td>
                     <td>{row.sentiment}</td>
                  </tr>
               {/each}
            </tbody>
         </table>
      </div>
   </div>
   {/if}
</div>

<style>
   .scrollable-table {
      max-height: 200px;
      overflow-y: auto;
   }
   
   table {
      table-layout: fixed;
      width: 100%;
      border-collapse: collapse;
   }

   th {
      position: sticky;
      color: #D9D9D9;
      border-color: #f4f4f4;
      text-align: center;
      font-family: Roboto, Helvetica, sans-serif;
      word-wrap: break-word;
      overflow-wrap: break-word;
      white-space: normal;
   }
   
   td {
      border-color: #f4f4f4;
      padding: 8px;
      text-align: center;
      font-family: Roboto, Helvetica, sans-serif;
      word-wrap: break-word;
      overflow-wrap: break-word;
      white-space: normal;
   }
</style>