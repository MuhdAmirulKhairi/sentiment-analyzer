<script>
   import { goto } from '$app/navigation';
   import SentimentResult from '$lib/sentimentResult.svelte';
   import Performance from '$lib/performance.svelte';
</script>

<a href="/">
   <button id="homeButton" type="button">
      <img src="/home.png" alt="home">
   </button>
</a>

<section id="results-main" class="p-4">
   <div class="panel-heading text-center m-0">RESULTS</div>
   <div id="sentiment-results" class="panel-group row my-3 mx-5">
      <div class="panel panel-default d-block col">
         <SentimentResult />
      </div>
   </div>
   <div class="panel-heading text-center m-0">CHART</div>
   <div id="sentiment-results" class="panel-group row my-3 mx-5">
      <div class="panel panel-default d-block col">
      </div>
   </div>
   <div class="panel-heading text-center">PERFORMANCE</div>
   <div id="performance-results" class="panel-group row my-3 mx-5">
      <div class="panel panel-default d-block col">
         <Performance />
      </div>
   </div>
   <div class="panel-heading text-center">WORD CLOUD</div>
   <div id="wordcloud-results" class="panel-group row my-3 mx-5">
      <div class="panel panel-default d-block col">
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
   #results-main {
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
      background: none;
      float: left;
      padding: 0px;
      margin: 15px;
      border: none;
   }
</style>