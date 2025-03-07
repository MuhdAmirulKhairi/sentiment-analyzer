<script>
   import DownloadButton from "./downloadButton.svelte";
</script>


<div id="word-cloud">
   <img src="https://randomdeterminism.wordpress.com/wp-content/uploads/2010/08/wordcloud-externalfilter-wordcloud.png" alt="word cloud"/>
   <p class="text-center">Right click on the image to save to device.</p>
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
      font-size: 25px;
      font-weight: bold;
   }

   @media screen and (max-width: 768px) {
      #word-cloud {
         padding: 10px;
      }

      img {
         padding: 5px;
      }

      p {
         font-size: 13px;
      }
   }
</style>