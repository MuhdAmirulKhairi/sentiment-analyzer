<script>
   // Declare variables for number of runs and domain selection
   export let domain_select;
   export let process;
</script>

<div id="analyzer-settings">
   <table>
      <tbody>
         <!-- Choose process -->
         <tr>
            <td class="fs-4 col-7">
               Choose a process
               <p style="font-size:24px;
                         display: inline;"
                  title="Select a process whether to perform training or testing">&#63;</p>
            </td>
            <td class="right-align fs-4 col-5">
               <select
                  class="analyzer-inputs col-11"
                  id="domain-select"
                  bind:value={process}>
                  <option value="Training and Testing">Training and Testing</option>
                  <option value="Testing only">Testing only</option>
               </select>
            </td>
         </tr>
         <!-- Dropdown for selecting the domain -->
         {#if process === "Testing only"}
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
                     <option value="Reviews">Reviews</option>
                     <option value="Education/News">Education/News</option>
                     <option value="Fiction">Fiction</option>
                  </select>
               </td>
            </tr>
         {:else if process === "Training and Testing"}
            <tr>
               <td class="fs-4 col-7">
                  Placeholder
                  <p style="font-size:24px;
                           display: inline;"
                     title="Select which domain is suitable for this dataset">&#63;</p>
               </td>
               <td class="right-align fs-4 col-5">
                  <select
                     class="analyzer-inputs col-11"
                     id="domain-select"
                     bind:value={domain_select}>
                     <option value="Social media">Placeholder</option>
                  </select>
               </td>
            </tr>
         {/if}
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

   select {
      border-radius: 50px;
   }
</style>