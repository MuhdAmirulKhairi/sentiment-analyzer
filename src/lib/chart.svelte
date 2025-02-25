<script>
   import DownloadButton from "./downloadButton.svelte";
</script>

<div id="chart" class="mx-5">
   <img src="https://www.myqbook.com/userfiles/The%20bar%20graph%20below%20shows%20the%20colors%20of%20toy%20trains%20bought%20from%20a%20store%20last%20year.gif" alt="chart"/>
   <DownloadButton download_link=""/>
</div>

<style>
   #chart {
      padding: 25px;
   }

   img {
      display: block;
      margin: auto auto;
      width: 80%;
      padding-bottom: 25px;
   }
</style>