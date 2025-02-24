<script context="module">
   export async function load({fetch}) {
      const response = await fetch("/.json");
      const { users } = await response.json();
   }
</script>

<script>
   import { onMount } from "svelte";
   import { goto } from "$app/navigation";
   import Dataset from "$lib/dataset.svelte";
   import History from "$lib/history.svelte";
   import AnalyzerSettings from "$lib/analyzerSettings.svelte";
   import OutputSettings from "$lib/outputSettings.svelte";
   
   // Set the width of the side navigation to 300px when opening the nav bar
   function openNav() {
      document.getElementById("main-sidebar").style.width = "300px";
      document.getElementById("header-main").style.marginLeft = "300px";
      document.getElementById("body-main").style.marginLeft = "300px";
      document.getElementById("footer-main").style.marginLeft = "300px";

      document.getElementById("openBtn").style.display = "none"; //Make the open navbar disappear
   }

   // Set the width of the side navigation to 0 when closing the nav bar
   function closeNav() {
      document.getElementById("main-sidebar").style.width = "0";
      document.getElementById("header-main").style.marginLeft = "0";
      document.getElementById("body-main").style.marginLeft = "0";
      document.getElementById("footer-main").style.marginLeft = "0";

      document.getElementById("openBtn").style.display = "inline"; //Make the open navbar reappear
   }
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
            <a href="/results"><History /></a>
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
   <div id="main" class="panel-group row">
      <div id="dataset-panel" class="panel panel-default d-block col">
         <div class="panel-heading text-center">DATASET</div>
            <div class="panel-body justify-content-center">
               <label class="panel-texts col-12 text-center" for="csv-file-upload">Upload your dataset...</label>
               <Dataset />
            </div>
      </div>
      <div class="panel panel-default col-1"></div>
      <div id="settings-panel" class="panel panel-default d-block col">
         <form class="form-group">
            <div class="panel-heading text-center">ANALYZER SETTINGS</div>
               <div class="panel-body justify-content-center">
                  <AnalyzerSettings />
               </div>
            <div class="panel-heading text-center">OUTPUT SETTINGS</div>
               <div class="panel-body d-block justify-content-center">
                  <OutputSettings />
               </div>
               <div class="text-center p-2">
                  <a href="/results">
                     <button
                        class="px-4 py-1"
                        id="run-analyzer"
                        type="submit"
                        >
                        Run Analyzer
                     </button>
                  </a>
               </div>
         </form>
      </div>
   </div>
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

   /* The side navigation menu */
   .sidebarNav {
      height: 100%; /* 100% Full-height */
      width: 0; /* 0 width - change this with JavaScript */
      position: fixed; /* Stay in place */
      z-index: 1; /* Stay on top */
      top: 0; /* Stay at the top */
      left: 0;
      background-color: #6A42C2; 
      overflow-x: hidden; /* Disable horizontal scroll */
      padding-top: 20px; /* Place content 60px from the top */
      transition: 0.5s; /* 0.5 second transition effect to slide in the sidenav */
   }

   /* The navigation menu links */
   .sidebarNav a, h2 {
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

   /* On smaller screens, where height is less than 450px, change the style of the sidenav (less padding and a smaller font size) */
   @media screen and (max-height: 450px) {
      .sidebarNav {padding-top: 15px;}
      .sidebarNav a {font-size: 18px;}
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
</style>