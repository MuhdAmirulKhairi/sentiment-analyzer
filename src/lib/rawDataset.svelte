<script>
   import Papa from "papaparse"; // For CSV handling
   import { CSVdata2, datasetName } from "$lib/stores"; // To hold parsed CSV data and dataset name

   let selectedColumns = ["text"] // Specified the columns to be displayed

   // Handle file input when user uploads dataset
   function handleFileUploads(event) {
      const uploadedFile = event.target.files[0];

      if (uploadedFile) {
         datasetName.set(uploadedFile.name); // Stores file name

         const reader = new FileReader(); // Create new file reader
         
         reader.onload = (x) => {
            const CSVtexts = x.target.result;
            
            // Parse CSV file
            Papa.parse(CSVtexts, {
               header: true, // Treat the first rows as headers
               skipEmptyLines: true, // Ignore empty rows
               complete: function(result) {
                  // Filter unwanted columns
                  CSVdata2.set(result.data
                                 .filter(row => row.text)
                                 .map(row => ({
                                    text: row.text
                                 }))
                  );
               },
            });
         };

         reader.readAsText(uploadedFile); // Read dataset as text
      }
   }
</script>

<!-- Input to upload dataset -->
<input
   type="file" 
   id="csv-file-upload"
   class="form-control col"
   accept=".csv"
   required
   on:change={handleFileUploads}
/>
<div id="CSVTable"> <!-- Table to display dataset -->
   {#if $CSVdata2.length > 0}
   <div class="table-responsive">
      <div class="scrollable-table">
         <table class="table table-striped table-bordered">
            <thead class="table-dark">
               <tr>
                  <th>Text</th>
               </tr>
            </thead>
            <tbody class="table-light">
               {#each $CSVdata2 as row}
                  <tr>
                     <td>{row.text}</td>
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