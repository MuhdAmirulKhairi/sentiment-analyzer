<script>
   export let history = [];

   async function fetchHistory() {
      try {
         const response = await fetch("http://127.0.0.1:8000/api/get_history");
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

   async function deleteHistoryEntry(entryID) {
      try {
         const response = await fetch(`http://127.0.0.1:8000/api/delete_history/${entryID}`, {
            method: "DELETE",
         });

         if (response.ok) {
            history = history.filter(entry => entry.id !== entryID); // Remove history entry
         }
         else {
            console.error("Failed to delete history.");
         }
      }
      catch (error) {
         console.error("Error deleting history.", error);
      }
   }

   async function clearAllHistory() {
      try {
         const response = await fetch("http://127.0.0.1:8000/api/clear_all_history", {
            method: "DELETE",
         });

         if (response.ok) {
            history = []; // Clears all and leave it blank
         }
         else {
            console.error("Failed to clear history.");
         }
      }
      catch (error) {
         console.error("Error clearing history.", error);
      }
   }

   function formatDate(dateString) {
      if (!dateString) return "Unknown date"; // Handles missing dates
      const date = new Date(dateString);
      return date.toLocaleDateString("en-GB", {
         day: "2-digit",
         month: "2-digit",
         year: "numeric"
      });
   }
</script>

<div id="history-list">
   <button on:click={clearAllHistory} class="delete-btn px-4 py-1">Clear All</button>

   {#if history.length === 0}
      <p class="fw-bold fs-5 px-2">No history available</p>
   {:else}
      {#each history as entry}
      <div id="history" class="panel p-2 mx-2 my-4">
         <div class="panel-heading d-inline-block fw-bold fs-5">
            <a href="/results/{entry.id}">History ({formatDate(entry.date)})</a>
         </div>
         <div class="panel-body">
            <p class="sub-history">Dataset: {entry.dataset}</p>
            <p class="sub-history">Domain: {entry.domain}</p>
            <p class="sub-history">Sort by: {entry.sort_by}</p>
         </div>
         <button on:click={() => deleteHistoryEntry(entry.id)} class="delete-btn px-4 py-1">Delete</button>
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

   .delete-btn {
      color: #F5F5F5;
      background-color: #2C2C2C;
      border-radius: 11px;
   }
</style>