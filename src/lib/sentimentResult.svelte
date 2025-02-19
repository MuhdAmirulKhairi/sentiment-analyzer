<script>
   import DownloadButton from "./downloadButton.svelte";
</script>

<div id="sentiment-results-table" class="mx-5">
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
            </tbody>
         </table>
      </div>
   </div>
   <DownloadButton />
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