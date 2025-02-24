<script>
   let num_runs = 1;
   let domain_select = "none";
</script>

<div id="analyzer-settings">
   <table>
      <tbody>
         <tr>
            <td class="fs-4 col-7">
               Number of runs <i style="font-size:24px">&#63;</i>
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
         </tr>
         <tr>
            <td class="fs-4 col-7">
               Domain <i style="font-size:24px">&#63;</i>
            </td>
            <td class="right-align fs-4 col-5">
               <select
                  class="analyzer-inputs col-11"
                  id="domain-select"
                  bind:value={domain_select}>
                  <option value="social-media">Social media</option>
                  <option value="customer-reviews">Customer reviews</option>
                  <option value="online-forums">Online forums</option>
                  <option value="education">Education</option>
                  <option value="fiction">Fiction</option>
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