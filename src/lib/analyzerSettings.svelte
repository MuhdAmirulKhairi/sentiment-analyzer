<script>
   // Declare variables for different settings
   export let process;

   export let domain_select;
   
   export let min_df;
   export let max_df;
   export let scaling;
   export let pattern_method;
   export let sensi;
</script>

<div id="analyzer-settings">
   <table>
      <tbody>
         <!-- Choose process -->
         <tr>
            <td class="fs-4 col-8">
               Choose a model
               <p style="font-size:24px;
                         display: inline;"
                  title="Select a model (SVM for train/test, BERT for test)">&#63;</p>
            </td>
            <td class="right-align fs-4 col-4">
               <select
                  class="analyzer-inputs col-12"
                  id="process"
                  bind:value={process}>
                  <option selected disabled hidden></option>
                  <option value="SVM">SVM</option>
                  <option value="BERT">BERT</option>
               </select>
            </td>
         </tr>
         <!-- Dropdown for selecting the domain -->
         {#if process === "BERT"}
            <tr>
               <td class="fs-4 col-8">
                  Domain
                  <p style="font-size:24px;
                           display: inline;"
                     title="Select which domain is suitable for this dataset">&#63;</p>
               </td>
               <td class="right-align fs-4 col-4">
                  <select
                     class="analyzer-inputs col-12"
                     id="domain-select"
                     bind:value={domain_select}>
                     <option value="Social media">Social media</option>
                     <option value="Reviews">Reviews</option>
                     <option value="Education/News">Education/News</option>
                     <option value="Fiction">Fiction</option>
                  </select>
               </td>
            </tr>
         {:else if process === "SVM"}
            <tr>
               <td class="fs-4 col-8">
                  Min document count
                  <p style="font-size:24px;
                           display: inline;"
                     title="Ignores rare words in text that are fewer than the specified value.">&#63;</p>
               </td>
               <td class="right-align fs-4 col-4">
                  <input
                     type="number"
                     class="analyzer-inputs col-12"
                     id="min-df"
                     bind:value={min_df}
                     min="1"
                     max="10"/>
               </td>
            </tr>
            <tr>
               <td class="fs-4 col-8">
                  Max document count
                  <p style="font-size:24px;
                           display: inline;"
                     title="Ignores words in text that appear more than the specified percentage.">&#63;</p>
               </td>
               <td class="right-align fs-4 col-4">
                  <input
                     type="number"
                     class="analyzer-inputs col-12"
                     id="min-df"
                     step="0.1"
                     bind:value={max_df}
                     min="0.5"
                     max="1.0"/>
               </td>
            </tr>
            <tr>
               <td class="fs-4 col-8">
                  Allow scaling
                  <p style="font-size:24px;
                           display: inline;"
                     title="Allows softening of common text impact.">&#63;</p>
               </td>
               <td class="right-align fs-4 col-4">
                  <select
                     class="analyzer-inputs col-12"
                     id="domain-select"
                     bind:value={scaling}>
                     <option selected disabled hidden></option>
                     <option value="True">Yes</option>
                     <option value="False">No</option>
                  </select>
               </td>
            </tr>
            <tr>
               <td class="fs-4 col-8">
                  Recognition method
                  <p style="font-size:24px;
                           display: inline;"
                     title="Changes how SVM 'interprets' the data.">&#63;</p>
               </td>
               <td class="right-align fs-4 col-4">
                  <select
                     class="analyzer-inputs col-12"
                     id="domain-select"
                     bind:value={pattern_method}>
                     <option selected disabled hidden></option>
                     <option value="rbf">Natural</option>
                     <option value="linear">Basic</option>
                     <option value="poly">Complex</option>
                     <option value="sigmoid">Soft</option>
                  </select>
               </td>
            </tr>
            <tr>
               <td class="fs-4 col-8">
                  Sensitivity
                  <p style="font-size:24px;
                           display: inline;"
                     title="Changes how each piece of data affects the overall model.">&#63;</p>
               </td>
               <td class="right-align fs-4 col-4">
                  <input
                     type="number"
                     class="analyzer-inputs col-12"
                     id="min-df"
                     step="0.1"
                     bind:value={sensi}
                     min="0.1"
                     max="1.0"/>
               </td>
            </tr>
         {/if}
      </tbody>
   </table>
</div>

<style>
   #analyzer-settings {
      font-family: Roboto, Helvetica, sans-serif;
      margin-left: 50px;
      margin-right: 50px;
   }

   table {
      width: 100%;
      table-layout: fixed;
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
      border-radius: 10px;
   }

   input {
      border-radius: 15px;
   }
</style>