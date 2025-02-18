<script>
   import { goto } from '$app/navigation';
</script>

<!-- svelte-ignore a11y_consider_explicit_label -->
<button id="homeButton" type="button">
   <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-house" viewBox="0 0 16 16">
      <path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L2 8.207V13.5A1.5 1.5 0 0 0 3.5 15h9a1.5 1.5 0 0 0 1.5-1.5V8.207l.646.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293zM13 7.207V13.5a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1-.5-.5V7.207l5-5z"/>
    </svg>
</button>

<section id="results-main" class="p-4">
   <div class="panel-heading text-center m-0">RESULTS</div>
   <div id="sentiment-results" class="panel-group row my-3 mx-5">
      <div class="panel panel-default d-block col">
         <label class="panel-texts col-12 text-center" for="csv-file-upload">Upload your dataset...</label>
      </div>
   </div>
   <div class="panel-heading text-center">PERFORMANCE</div>
   <div id="performance-results" class="panel-group row my-3 mx-5">
      <div class="panel panel-default d-block col">
         <label class="panel-texts col-12 text-center" for="csv-file-upload">Upload your dataset...</label>
      </div>
   </div>
   <div class="panel-heading text-center">WORD CLOUD</div>
   <div id="wordcloud-results" class="panel-group row my-3 mx-5">
      <div class="panel panel-default d-block col">
         <label class="panel-texts col-12 text-center" for="csv-file-upload">Upload your dataset...</label>
      </div>
   </div>
</section>

<!-- Footer which shows related info at the bottom -->
<section id="footer-main" class="p-4">
   <footer>
      <p
         style="font-family: Roboto, Helvetica, sans-serif"
         class="d-block text-center m-0">
         2025 | Sentiment Analyzer by Amirul Khairi
      </p>
   </footer>
</section>

<style>
   #header-main, #results-main {
      background-color: #8B5DFF;
   }

   #sentiment-results, #wordcloud-results, #footer-main {
      background-color: #6A42C2;
   }

   #sentiment-results, #wordcloud-results {
      border-radius: 25px;
      padding: 20px;
   }

   .panel-heading {
      color: #FFF7D1;
      -webkit-text-stroke-width: 1px;
      -webkit-text-stroke-color: #000000;
      text-shadow: 1px 2px 4px #000000;
      font-size: 33px;
   }

   #homeButton {
      position: absolute;
      background-color: #8B5DFF;
      float: left;
      padding: 0px;
      margin: 25px;
      border: none;
   }
</style>