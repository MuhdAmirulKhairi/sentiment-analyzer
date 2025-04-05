<script>
   // Declare variables for number of runs and domain selection
   //export let num_runs;
   export let domain_select;
</script>

<div id="analyzer-settings">
   <table>
      <tbody>
         <!-- Input field for specifying the number of runs -->
         <!-- <tr>
            <td class="fs-4 col-7">
               Number of runs 
               <p style="font-size:24px;
                         display: inline;"
                  title="Runs the data through the system at a number of times to increase accuracy (can take longer if used a higher number)">&#63;</p>
            </td>
            <td class="right-align fs-4 col-5">
               <input 
                  class="analyzer-inputs col-11"
                  type="number"
                  id="num-runs"
                  min="1"
                  max="20"
                  bind:value={num_runs}/>
            </td>
         </tr> -->
         <!-- Dropdown for selecting the domain -->
         <tr>
            <td class="fs-4 col-7">
               Domain
               <p style="font-size:24px;
                         display: inline;"
                  title="Select which domain is suitable for this dataset">&#63;</p>
            </td>
            <td class="right-align fs-4 col-5">
               <select
                  class="analyzer-inputs col-11"
                  id="domain-select"
                  bind:value={domain_select}>
                  <option value="Social media">Social media</option>
                  <option value="Customer reviews">Customer reviews</option>
                  <option value="Education">Education</option>
                  <option value="Fiction">Fiction</option>
               </select>
            </td>
         </tr>
      </tbody>
   </table>
</div>

<style>
   #analyzer-settings {
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