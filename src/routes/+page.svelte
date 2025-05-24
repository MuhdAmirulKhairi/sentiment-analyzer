<title>Sentiment Analyzer</title>

<script>
   import { onMount } from "svelte";
   import { goto } from "$app/navigation"; // Enables site navigation

   import Dataset from "$lib/dataset.svelte";
   import { CSVdata, datasetName } from "$lib/stores"; // Shared across components

   // Input UIs
   import History from "$lib/history.svelte";
   import AnalyzerSettings from "$lib/analyzerSettings.svelte";

   // Set default values
   let user_ID;
   let process = "none";
   let domain_select = "none";
   let show_only = "All";
   let word_cloud = 45;
   let history = [];
   let dataset_array = [];
   let dataset_name = "";
   let isLoading = false;
   
   // Set the width of the side navigation to 300px when opening the nav bar
   function openNav() {
      let sidebar = document.getElementById("main-sidebar");

      if (window.innerWidth <= 768) {
         sidebar.style.width = "100%";
         sidebar.style.height = "100vh";
         sidebar.style.position = "fixed";
      } else {
         sidebar.style.width = "300px";
      }

      document.body.classList.add("no-scroll");
      document.getElementById("openBtn").style.display = "none"; //Make the open navbar disappear
      sidebar.setAttribute("data-open", "true");
   }

   // Set the width of the side navigation to 0 when closing the nav bar
   function closeNav() {
      let sidebar = document.getElementById("main-sidebar");
      sidebar.style.width = "0";

      document.body.classList.remove("no-scroll");
      document.getElementById("openBtn").style.display = "inline"; //Make the open navbar reappear
      sidebar.setAttribute("data-open", "false");
   }

   CSVdata.subscribe(value => dataset_array = value);
   datasetName.subscribe(value => dataset_name = value);

   // Handles data submission to the Python backend
   async function runAnalyzer(event) {
      event.preventDefault(); // Prevent default form submission

      // If a user pressed the button without a dataset
      const dataset = $CSVdata;
      if (!dataset.length) {
         alert("No dataset uploaded!");
         return;
      }

      let settings;

      //Retrieve values from dataset, analyzer settings, output settings
      if (process === "Testing only") {
         settings = {
            user_id: user_ID,
            process: process,
            dataset_name: dataset_name || "Unnamed Dataset",
            show_only: show_only,
            word_cloud: word_cloud,
            texts: dataset.map(row => row.text)
         };
      }
      else if (process === "Training and Testing") {
         settings = {
            user_id: user_ID,
            process: process,
            dataset_name: dataset_name || "Unnamed Dataset",
            domain_select: domain_select,
            show_only: show_only,
            word_cloud: word_cloud,
            texts: dataset.map(row => ({text: row.text, sentiment: row.sentiment}))
         };
      }
      else {
         alert("No settings updated!");
         return
      }
      
      isLoading = true; // Show loading popup
      console.log("Running analysis with: ", settings)

      try {
         let endpoint = 
            process === "Testing only" 
            ? "http://127.0.0.1:8000/api/analyze_sentiment/" 
            : "http://127.0.0.1:8000/api/analyze_sentiment_deux/";
         let response = await fetch(endpoint, {
            method: 'POST',
            headers: {
               "Content-Type": "application/json",
            },
            body: JSON.stringify(settings)
         });

         if (response.ok) {
            let data = await response.json();
            console.log("Analysis completed!");
            goto(`/results/${data.id}`); // Redirect after success
         }
         else {
            let error_data = await response.json()
            console.error("Error: ", response.status, error_data);
         }
      }
      catch (error) {
         console.error("Fetch failed: ", error);
      }
      finally {
         isLoading = false;
      }
   }

   // Generate UUID
   function generateUUID() {
      return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
         const r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8);
         return v.toString(16);
      });
   }

   async function fetchHistory() {
      try {
         const response = await fetch(`http://127.0.0.1:8000/api/get_history/?user_id=${user_ID}`, {
            method: 'GET'
         });

         if (response.ok) {
            const data = await response.json();
            history = data.history;
         }
      }
      catch (error) {
         console.error("Error fetching history: ", error);
      }
   }

   onMount(() => {
      user_ID = localStorage.getItem("user_id");

      if (!user_ID) {
         user_ID = generateUUID();
         localStorage.setItem("user_id", user_ID);
      }

      fetchHistory();
   });
</script>

<!-- Header of the application -->
<section id="header-main" class="p-4">
   <header>
      <div id=main-sidebar class="sidebarNav">
         <!-- svelte-ignore a11y_consider_explicit_label -->
         <button type="button" class="closeBtn" on:click="{closeNav}">
            <img src="/navbarButton.png" alt="navbar button"/>
         </button>
         <div id=history-sidebar>
            <h2 style="font-family: Roboto, Helvetica, sans-serif">
               HISTORY
            </h2>
            <div id="history-entry"><History {history}/></div>
         </div>
      </div>

      <button  id="openBtn" type="button" on:click="{openNav}">
         <img src="/navbarButton.png" alt="navbar button"/>
      </button>
      <div>
         <h1 
            style="font-family: Roboto, Helvetica, sans-serif"
            class="text-center m-0">
            SENTIMENT ANALYZER
         </h1>
         <h5 
            style="font-family: Roboto, Helvetica, sans-serif" 
            class="text-center m-0">
            By: Amirul Khairi
         </h5>
      </div>
   </header>
</section>

<!-- Body of the main page, where it hosts the dataset upload and settings -->
<section id="body-main" class="p-4">
   <div id="main" class="panel-group row justify-content-center">
      <div id="dataset-panel" class="panel panel-default d-block col-md-5 col-12">
         <div class="panel-heading text-center">DATASET</div>
            <div class="panel-body justify-content-center">
               <label class="panel-texts col-12 text-center" for="csv-file-upload">Upload your dataset...</label>
               <Dataset />
            </div>
      </div>
      <div class="panel panel-default col-md-1 d-none d-md-block"></div>
      <div class="d-block d-md-none my-3"></div> 
      <div id="settings-panel" class="panel panel-default d-block col-md-5 col-12">
         <form class="form-group" on:submit="{runAnalyzer}">
            <div class="panel-heading text-center">ANALYZER SETTINGS</div>
               <div class="panel-body justify-content-center">
                  <AnalyzerSettings bind:process bind:domain_select />
               </div>
               <div class="text-center p-2">
                  <button
                     class="px-4 py-1"
                     id="run-analyzer"
                     type="submit"
                     >
                     Run Analyzer
                  </button>
               </div>
         </form>
      </div>
   </div>
   {#if isLoading}
      <div class="loading-overlay">
         <div class="loading-popup fs-2">
            <p>Processing...</p>
            <div class="loader"></div>
         </div>
      </div>
   {/if}
</section>

<!-- Footer which shows related info at the bottom -->
<section id="footer-main" class="p-4">
   <footer>
      <p
         style="font-family: Roboto, Helvetica, sans-serif;
                color: #2C2C2C;"
         class="d-block text-center m-0">
         2025 | Sentiment Analyzer by Amirul Khairi
      </p>
   </footer>
</section>

<style>
   #header-main, #body-main {
      background-color: #8B5DFF;
   }

   #body-main {
      min-height: calc(100vh - 160px);
   }

   h1, h5, .panel-heading {
      color: #FFF7D1;
      -webkit-text-stroke-width: 1px;
      -webkit-text-stroke-color: #000000;
      text-shadow: 1px 2px 4px #000000;
   }

   h5 {
      -webkit-text-stroke-width: 0.6px;
   }

   .panel-heading {
      font-size: 33px;
   }

   #main-sidebar, #footer-main, #dataset-panel, #settings-panel {
      background-color: #6A42C2;
   }

   #dataset-panel, #settings-panel {
      border-radius: 25px;
      padding-top: 40px;
      padding-bottom: 40px;
      padding-left: 20px;
      padding-right: 20px;
   }

   .sidebarNav {
      height: 100vh;
      width: 0;
      position: fixed;
      top: 0;
      left: 0;
      background-color: #6A42C2; 
      overflow-y: auto;
      padding-top: 20px;
      transition: 0.5s ease-in-out;
      z-index: 999;
   }

   /* The navigation menu links */
   h2 {
      padding: 6px 15px 6px 15px;
      text-decoration: none;
      font-size: 15px;
      color: #000000;
      display: block;
   }

   h2 {
      color: #FFF7D1;
      -webkit-text-stroke-width: 0.95px;
      -webkit-text-stroke-color: #000000;
      text-shadow: 1px 2px 4px #000000;
      margin: 0;
      padding-left: 90px;
      padding-bottom: 30px;
      font-size: 30px;
   }

   /* Position and style the close button (top right corner) */
   .closeBtn {
      position: absolute;
      border: none;
      background: none;
   }

   /* Style page content - use this if you want to push the page content to the right when you open the side navigation */
   #main {
      transition: margin-left .5s;
      padding: 20px;
   }

   #header-main/*, #body-main.no-scroll*/ {
      overflow: hidden;
   }

   /* On smaller screens, where height is less than 450px, change the style of the sidenav (less padding and a smaller font size) */
   @media screen and (max-height: 450px) {
      .sidebarNav {padding-top: 15px;}
   }

   #openBtn {
      position: absolute;
      transition-duration: 0.5s;
      background: none;
      float: left;
      padding: 0;
   }

   #run-analyzer {
      color: #F5F5F5;
      background-color: #2C2C2C;
      border-radius: 11px;
   }

   button:hover {
      color: #F1F1F1;
   }

   #openBtn {
      font-size: 50px;
      border: none;
   }

   .panel-texts {
      color: #D9D9D9;
      font-size: 20px;
      -webkit-text-stroke-width: 0.25px;
      -webkit-text-stroke-color: #000000;
      text-shadow: 1px 2px 4px #000000;
      padding-bottom: 10px;
   }

   #history-entry {
      margin-left: 10px;
      margin-right: 10px;
   }

   .loading-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(139, 93, 255, 0.5);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 9999;
   }

   .loading-popup {
      background: #6A42C2;
      padding-top: 20px;
      padding-bottom: 20px;
      padding-left: 100px;
      padding-right: 100px;
      border-radius: 10px;
      text-align: center;
   }

   .loading-popup p {
      color: #D9D9D9;
      -webkit-text-stroke-width: 0.25px;
      -webkit-text-stroke-color: #000000;
      text-shadow: 1px 2px 4px #000000;
      padding-bottom: 10px;
   }

   .loader {
      border: 5px solid #D9D9D9;
      border-top: 5px solid #6A42C2;
      border-radius: 50%;
      width: 40px;
      height: 40px;
      animation: spin 1s linear infinite;
      margin: 10px auto;
   }

   @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
   }
</style>