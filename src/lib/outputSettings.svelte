<script>
   // Store sorting and word cloud settings
   export let sort_by; // Controls the sorting order of sentiment results
   export let word_cloud; // Controls how many words to appear on word cloud
</script>

<!-- Output settings -->
<div id="output-settings">
   <table>
      <tbody>
         <!-- Sort by -->
         <tr>
            <td class="fs-4 col-9">
               Sort by
               <!-- Tooltip -->
               <p style="font-size:24px;
                         display: inline;"
                  title="Sort the sentiment outputs in different order">&#63;</p>
            </td>
            <td class="right-align fs-4 col-3">
               <select
                  class="analyzer-inputs col-12"
                  id="sort-by"
                  bind:value={sort_by}>
                  <option value="Positive">Positive</option>
                  <option value="Negative">Negative</option>
                  <option value="Neutral">Neutral</option>
               </select>
            </td>
         </tr>

         <!-- Number of words in cloud -->
         <tr>
            <td class="fs-4 col-9">
               Number of words
               <!-- Tooltip -->
               <p style="font-size:24px;
                         display: inline;"
                  title="Displays the top most common sentiment in the word cloud">
                  &#63;</p>
            </td>
            <td class="right-align fs-4 col-3">
               <input
                  class="analyzer-inputs col-12"
                  type="number"
                  id="num-words"
                  min="20"
                  max="45"
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