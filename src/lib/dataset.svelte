<script>
   import Papa from "papaparse";

   let CSVdata = [];

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
                  CSVdata = [...result.data];
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
   {#if CSVdata.length > 0}
   <div class="table-responsive">
      <div class="scrollable-table">
         <table class="table table-striped table-bordered">
            <thead class="table-dark">
               <tr>
                  {#each Object.keys(CSVdata[0]) as head}
                     <th>{head}</th>
                  {/each}
               </tr>
            </thead>
            <tbody class="table-light">
               {#each CSVdata as row}
                  <tr>
                     {#each Object.values(row) as cell}
                        <td>{cell}</td>
                     {/each}
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
      max-width: 560px;
      overflow-y: auto;
   }
   
   table {
      width: 100%;
      border-collapse: collapse;
   }

   th {
      position: sticky;
      color: #D9D9D9;
      border-color: #f4f4f4;
      text-align: center;
      font-family: Roboto, Helvetica, sans-serif;
   }
   
   td {
      border-color: #f4f4f4;
      padding: 8px;
      text-align: center;
      font-family: Roboto, Helvetica, sans-serif;
   }
</style>