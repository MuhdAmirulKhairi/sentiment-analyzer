<title>Results</title>

<script>
   import { onMount } from 'svelte';
   import { page } from "$app/stores";
   
   // Import components to render each result
   import SentimentResult from '$lib/sentimentResult.svelte';
   import Chart from "$lib/chart.svelte";
   import WordCloud from '$lib/wordCloud.svelte';
    import { json } from '@sveltejs/kit';

   // Default values
   let sentiments = []; // List of sentiment results
   let sentimentCounts = { positive: 0, negative: 0, neutral: 0}; // Chart counts
   let performance = { precision: 0, recall: 0, f1_score: 0}; // Performance metrics
   let show_only = "All"; // Sort by setting
   let word_cloud = []; // Word cloud data
   let display_WC = [];
   let num_words = 45; // Number of words in word cloud
   let loading = true; // Flag to show loading state

   // Update displayed word cloud whenever num_words changes
   $: if (word_cloud && word_cloud.length > 0 && num_words) {
         const clamp = Math.max(20, Math.min(num_words, word_cloud.length))
         display_WC = word_cloud.slice(0, clamp);
      }

   $: max = word_cloud.length || 45;

   // Fetch results using ID
   async function fetchResults() {
      loading = true;
      let id;
      page.subscribe(($page) => {
         id = $page.params.id;
      });

      console.log("Fetching ID: ", id);

      try {
         // Backend call
         let user_ID = localStorage.getItem("user_id");
         let response = await fetch(`http://127.0.0.1:8000/api/get_history/${id}?user_id=${user_ID}`);

         if (response.ok) {
            let data = await response.json();
            console.log("Fetched: ", data);

            // Assign attached values
            sentiments = data.sentiments || [];
            sentimentCounts = data.sentiment_counts || { positive: 0, negative: 0, neutral: 0};
            show_only = data.show_only || "None";
            word_cloud = data.word_cloud || [];
            console.log("Fetched word cloud:", word_cloud);
            console.log("Word cloud length:", word_cloud.length);

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

   // Trigger fetch on page mount
   onMount(fetchResults);
</script>

<!-- Home button -->
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
   <!-- Main results page -->
   <section id="results-main" class="p-4">
      <div class="panel-heading text-center m-0 py-2">RESULTS</div>
      <div id="sentiment-results" class="panel-group row my-3 mx-5"> <!-- Sentiment Results -->
         <div class="panel panel-default d-block col">
            <div class="text-center my-2">
               <label for="sort-dropdown" class="me-2 fs-5">Show only:</label>
               <select id="sort-dropdown" bind:value={show_only} class="fs-5 w-auto d-inline-block">
                  <option value="All" selected>All</option>
                  <option value="Positive">Positive</option>
                  <option value="Negative">Negative</option>
                  <option value="Neutral">Neutral</option>
               </select>
            </div>
            <SentimentResult {sentiments} showOnly={show_only}/>
         </div>
      </div>
      <div class="panel-heading text-center m-0 py-2">CHART</div> <!-- Chart -->
      <div id="chart-results" class="panel-group row my-3 mx-5">
         <div class="panel panel-default d-block col">
            <Chart {sentimentCounts}/>
         </div>
      </div>
      <div class="panel-heading text-center py-2">WORD CLOUD</div> <!-- Word cloud -->
      <div id="wordcloud-results" class="panel-group row my-3 mx-5">
         <div class="panel panel-default d-block col">
            <div class="text-center my-2">
               <label for="num-words" class="me-2 fs-5">Number of words:</label>
               <input
                  class="fs-5 w-auto d-inline-block"
                  type="number"
                  id="num-words"
                  min="20"
                  {max}
                  bind:value={num_words}/>
            </div>
            <WordCloud wordCloud={display_WC}/>
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
      min-height: calc(100vh - 160px);
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

   label {
      color: #D9D9D9;
      font-size: 20px;
      -webkit-text-stroke-width: 0.25px;
      -webkit-text-stroke-color: #000000;
      text-shadow: 1px 2px 4px #000000;
      padding-bottom: 10px;
   }

   input, select {
      border-radius: 10px;
   }

   @media screen and (max-width: 768px) {
      #sentiment-results, #chart-results, #wordcloud-results {
         padding-right: 0;
         padding-left: 0;
         padding-top: 2px;
         padding-bottom: 2px;
      }
   }
</style>