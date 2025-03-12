<script>
   import { onMount } from "svelte";

   let history = [];

   async function fetchHistory() {
      try {
         const response = await fetch("/api/get_history");
         if (response.ok) {
            const data = await response.json();
            history = data.history;
         }
         else {
            console.error("Failed to fetch history");
         }
      }
      catch (error) {
         console.error("Error fetching history: ", error)
      }
   }

   onMount(fetchHistory);
</script>

<div id="history-list">
   {#if history.length === 0}
      <p class="fw-bold fs-5 px-2">No history available</p>
   {:else}
      {#each history as entry}
      <div id="history" class="panel p-2">
         <div class="panel-heading d-inline-block fw-bold fs-5">
            <a href="/results/{entry.id}">History ({entry.date})</a>
         </div>
         <div class="panel-body">
            <p class="sub-history">Dataset: {entry.dataset}</p>
            <p class="sub-history">Domain: {entry.domain}</p>
            <p class="sub-history">Sort by: {entry.sort_by}</p>
            <p class="sub-history">Word cloud numbers: {entry.word_cloud}</p>
         </div>
      </div>
      {/each}
   {/if}
</div>

<style>
   #history {
      background-color: #D9D9D9;
      border-radius: 10px;
      font-family: Roboto, Helvetica, sans-serif;
      display: block;
   }

   p {
      margin: 0;
   }

   .sub-history {
      margin-left: 10px;
   }
</style>