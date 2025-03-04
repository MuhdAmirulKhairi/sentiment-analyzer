<script>
   import DownloadButton from "./downloadButton.svelte";
</script>


<div id="word-cloud" class="mx-5">
   <img src="https://randomdeterminism.wordpress.com/wp-content/uploads/2010/08/wordcloud-externalfilter-wordcloud.png" alt="word cloud"/>
   <p class="fs-5 text-center">Right click on the image to save to device.</p>
</div>

<style>
   #word-cloud {
      padding: 25px;
   }

   img {
      display: block;
      margin: auto auto;
      width: 80%;
      padding-bottom: 25px;
   }

   p {
      font-weight: bold;
   }
</style>