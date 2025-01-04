<script>
   /* Set the width of the side navigation to 250px */
   function openNav() {
      document.getElementById("main-sidebar").style.width = "250px";
      document.getElementById("header-main").style.marginLeft = "250px";
      document.getElementById("body-main").style.marginLeft = "250px";
      document.getElementById("footer-main").style.marginLeft = "250px";

      const openBtn = document.getElementById("openBtn");
      openBtn.remove();
   }

   /* Set the width of the side navigation to 0 */
   function closeNav() {
      document.getElementById("main-sidebar").style.width = "0";
      document.getElementById("header-main").style.marginLeft = "0";
      document.getElementById("body-main").style.marginLeft = "0";
      document.getElementById("footer-main").style.marginLeft = "0";

      const closeBtn = document.getElementById("closeBtn");
   }
</script>

<section id="header-main" class="p-4">
   <header>
      <div id=main-sidebar class="sidebarNav">
         <button type="button" class="closeBtn" on:click="{closeNav()}">
            &#9776;
         </button>
         <div id=history-sidebar>
            <h2 style="font-family: Roboto, Helvetica, sans-serif">
               HISTORY
            </h2>
            <a>History 1</a>
         </div>
      </div>
   
      <!-- svelte-ignore a11y_consider_explicit_label -->
      <button id="openBtn" type="button" on:click="{openNav()}">
         &#9776;
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

<section id="body-main" class="p-4">
   <div id="main">

   </div>
</section>

<section id="footer-main" class="p-4">
   <footer>
      <p
         style="font-family: Roboto, Helvetica, sans-serif"
         class="d-block text-center m-0">
         2024 | Sentiment Analyzer by Amirul Khairi
      </p>
   </footer>
</section>

<style>
   #header-main, #body-main {
      background-color: #8B5DFF;
   }

   h1, h5 {
      color: #FFF7D1;
      -webkit-text-stroke-width: 1px;
      -webkit-text-stroke-color: #000000;
      text-shadow: 1px 2px 4px #000000;
   }

   h5 {
      -webkit-text-stroke-width: 0.75px;
   }

   #main-sidebar, #footer-main {
      background-color: #6A42C2;
   }

   /* The side navigation menu */
   .sidebarNav {
      height: 100%; /* 100% Full-height */
      width: 0; /* 0 width - change this with JavaScript */
      position: fixed; /* Stay in place */
      z-index: 1; /* Stay on top */
      top: 0; /* Stay at the top */
      left: 0;
      background-color: #111; /* Black*/
      overflow-x: hidden; /* Disable horizontal scroll */
      padding-top: 20px; /* Place content 60px from the top */
      transition: 0.5s; /* 0.5 second transition effect to slide in the sidenav */
   }

   /* The navigation menu links */
   .sidebarNav a, h2 {
      padding: 8px 8px 8px 32px;
      text-decoration: none;
      font-size: 25px;
      color: #000000;
      display: block;
      transition: 0.3s;
   }

   h2 {
      color: #FFF7D1;
      -webkit-text-stroke-width: 0.95px;
      -webkit-text-stroke-color: #000000;
      text-shadow: 1px 2px 4px #000000;
      margin: 0;
      padding-left: 65px;
      padding-right: 65px;
      font-size: 30px;
   }

   /* When you mouse over the navigation links, change their color */
   .sidebarNav a:hover {
      color: #f1f1f1;
   }

   /* Position and style the close button (top right corner) */
   .sidebarNav .closeBtn {
      top: 10px;
      left: 10px;
      font-size: 40px;
      border: none;
      background-color: #6A42C2;
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

   button {
      position: absolute;
      transition-duration: 0.5s;
      background-color: #8B5DFF;
      float: left;
      padding: 0;
   }

   button:hover {
      color: #f1f1f1;
   }

   #openBtn {
      font-size: 50px;
      border: none;
   }
</style>