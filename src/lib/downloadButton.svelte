<script>
   export let download_link = ""; // Recieves download function from the parent component
</script>

<!-- Download button -->
<div class="text-center p-2">
   <button
      class="px-4 py-1 download-button"
      id="download-results"
      type="submit"
      on:click={download_link}
      >
      Download
   </button>
</div>

<style>
   .download-button {
      color: #F5F5F5;
      background-color: #2C2C2C;
      border-radius: 11px;
   }
</style>