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
   <div class="table-container">
      <table>
         <thead>
            <tr>
               {#each Object.keys(CSVdata[0]) as head}
                  <th>{head}</th>
               {/each}
            </tr>
         </thead>
         <tbody>
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
   {/if}
</div>

<style>
   .table-container {
      max-height: 200px;
      max-width: 567px;
      overflow-y: auto;
      display: block;
      position: relative;
   }
   
   table {
      width: 100%;
      border-collapse: collapse;
   }
   
   th, td {
      border: 1px solid #2C2C2C;
      background-color: #f4f4f4;
      padding: 8px;
      text-align: center;
      font-family: Roboto, Helvetica, sans-serif;
   }
</style>