<script>
   import { onMount } from 'svelte';
   import { page } from "$app/stores";
   
   import SentimentResult from '$lib/sentimentResult.svelte';
   import Chart from "$lib/chart.svelte";
   import Performance from '$lib/performance.svelte';
   import WordCloud from '$lib/wordCloud.svelte';

   let sentiments = [];
   let sentimentCounts = { positive: 0, negative: 0, neutral: 0};
   let performance = { precision: 0, recall: 0, f1_score: 0};
   let word_cloud = [];
   let loading = true;

   async function fetchResults() {
      loading = true;
      const id = $page.params.id; // Check if there is an ID in the URL

      let response;
      if (id) {
         // Fetch results
         response = await fetch(`http://localhost:8000/api/get_history/${id}`);
      }
      else {
         // Fetch fresh analysis
         response = await fetch("http://localhost:8000/analyze_sentiment", {
            method: "POST",
            headers: { "Content-Type": "application/json"},
            body: JSON.stringify({ texts: ["example text 1", "example text 2"] }) // Will replace with actual texts
         });
      }

      if (response.ok) {
         const data = await response.json();
         sentiments = data.sentiments;
         sentimentsCounts = data.sentiment_counts;
         performance = data.performance;
         wordCloud = data.word_cloud;
      }
   }

   onMount(fetchResults);
</script>

<a href="/">
   <button id="homeButton" type="button">
      <img src="/home.png" alt="home">
   </button>
</a>

{#if loading}
   <p>Loading results...</p>
{:else}
   <section id="results-main" class="p-4">
      <div class="panel-heading text-center m-0">RESULTS</div>
      <div id="sentiment-results" class="panel-group row my-3 mx-5">
         <div class="panel panel-default d-block col">
            <SentimentResult {sentiments}/>
         </div>
      </div>
      <div class="panel-heading text-center m-0">CHART</div>
      <div id="chart-results" class="panel-group row my-3 mx-5">
         <div class="panel panel-default d-block col">
            <Chart {sentimentCounts}/>
         </div>
      </div>
      <div class="panel-heading text-center">PERFORMANCE</div>
      <div id="performance-results" class="panel-group row my-3 mx-5">
         <div class="panel panel-default d-block col">
            <Performance {performance}/>
         </div>
      </div>
      <div class="panel-heading text-center">WORD CLOUD</div>
      <div id="wordcloud-results" class="panel-group row my-3 mx-5">
         <div class="panel panel-default d-block col">
            <WordCloud {word_cloud}/>
         </div>
      </div>
   </section>
{/if}

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

   #sentiment-results, #chart-results, #wordcloud-results, #footer-main {
      background-color: #6A42C2;
   }

   #sentiment-results, #chart-results, #wordcloud-results {
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

   @media screen and (max-width: 768px) {
      #sentiment-results, #chart-results, #performance-results, #wordcloud-results {
         padding-right: 0;
         padding-left: 0;
         padding-top: 2px;
         padding-bottom: 2px;
      }
   }
</style>