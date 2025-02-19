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
            <td class="fs-2">Precision <i style="font-size:24px">&#63;</i></td>
            <td class="right-align fs-2">0</td>
         </tr>
         <tr>
            <td class="fs-2">Recall <i style="font-size:24px">&#63;</i></td>
            <td class="right-align fs-2">0</td>
         </tr>
         <tr>
            <td class="fs-2">F1 Score <i style="font-size:24px">&#63;</i></td>
            <td class="right-align fs-2">0</td>
         </tr>
      </tbody>
   </table>
   <DownloadButton />
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