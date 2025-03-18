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
      let id;
      page.subscribe(($page) => {
         id = $page.params.id;
      });

      console.log("Fetching ID: ", id);

      try {
         let response = await fetch(`http://127.0.0.1:8000/api/get_history/${id}`);

         if (response.ok) {
            let data = await response.json();
            console.log("Fetched: ", data);

            sentiments = data.sentiments || [];
            sentimentCounts = data.sentiment_counts || { positive: 0, negative: 0, neutral: 0};
            performance = data.performance || { precision: 0, recall: 0, f1_score: 0};
            word_cloud = data.word_cloud || [];

            console.log("Parsed sentiments: ", sentiments)
         }
         else {
            console.error("Error fetching data: ", response.status)
         }
      }
      catch (error) {
         console.error("Error in fetching data.", error);
      }
      finally {
         loading = false;
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
   <section id="loading-results">
      <p>Loading results...</p>
   </section>
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
   #results-main, #loading-results {
      background-color: #8B5DFF;
   }

   #loading-results {
      width: 100vw;
      height: 100vh;
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

   #loading-results p {
      margin: 0;
      font-size: 25px;
      text-align: center;
      padding: 25px;
      font-weight: bold;
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