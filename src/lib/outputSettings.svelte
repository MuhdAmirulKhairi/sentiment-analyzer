<script>
   let sort_by = "none";
   let word_cloud = 20;
</script>

<div id="output-settings">
   <table>
      <tbody>
         <tr>
            <td class="fs-4 col-9">
               Sort by <i style="font-size:24px">&#63;</i>
            </td>
            <td class="right-align fs-4 col-3">
               <select
                  class="analyzer-inputs col-12"
                  id="sort-by"
                  bind:value={sort_by}>
                  <option value="positive">Positive</option>
                  <option value="negative">Negative</option>
                  <option value="neutral">Neutral</option>
               </select>
            </td>
         </tr>
         <tr>
            <td class="fs-4 col-9">
               Number of words <i style="font-size:24px">&#63;</i>
            </td>
            <td class="right-align fs-4 col-3">
               <input
                  class="analyzer-inputs col-12"
                  type="number"
                  id="num-words"
                  min="20"
                  max="60"
                  bind:value={word_cloud}/>
            </td>
         </tr>
      </tbody>
   </table>
</div>

<style>
   #output-settings {
      font-family: Roboto, Helvetica, sans-serif;
      margin-left: 55px;
      margin-right: 55px;
   }

   td {
      color: #D9D9D9;
      font-size: 20px;
      -webkit-text-stroke-width: 0.25px;
      -webkit-text-stroke-color: #000000;
      text-shadow: 1px 2px 4px #000000;
      padding-bottom: 10px;
   }

   .right-align {
      text-align: right;
   }

   tr {
      padding: 5px;
   }

   input, select {
      border-radius: 50px;
   }
</style>