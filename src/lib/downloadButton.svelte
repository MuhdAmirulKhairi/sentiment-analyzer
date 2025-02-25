<script>
   export let download_link = "";
</script>

<div class="text-center p-2">
   <a href={download_link} download>
      <button
         class="px-4 py-1 download-button"
         id="download-results"
         type="submit"
         >
         Download
      </button>
   </a>
</div>

<style>
   .download-button {
      color: #F5F5F5;
      background-color: #2C2C2C;
      border-radius: 11px;
   }
</style>