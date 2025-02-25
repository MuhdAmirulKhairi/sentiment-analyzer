<script>
   import DownloadButton from "./downloadButton.svelte";
</script>

<div id="performance" class="mx-5">
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
               <p style="font-size:26px; display: inline;"
                  title="Measures how many predicted positives are correct">&#63;</p>
            </td>
            <td class="right-align fs-2">0</td>
         </tr>
         <tr>
            <td class="fs-2">Recall 
               <p style="font-size:26px; display: inline;"
                  title="Measures how many actual positives are correctly identified">&#63;</p>
            </td>
            <td class="right-align fs-2">0</td>
         </tr>
         <tr>
            <td class="fs-2">F1 Score 
               <p style="font-size:26px; display: inline;"
                  title="Evaluates system correctness and completeness in prediction">&#63;</p>
            </td>
            <td class="right-align fs-2">0</td>
         </tr>
      </tbody>
   </table>
   <DownloadButton download_link=""/>
</div>

<style>
   #performance {
      padding: 25px;
      font-family: Roboto, Helvetica, sans-serif;
   }

   .right-align {
      text-align: right;
   }
</style>