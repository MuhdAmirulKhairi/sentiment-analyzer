<script>
   import DownloadButton from "./downloadButton.svelte";

   function downloadIMG() {
      let img = document.querySelector("img");
      if (!img) {
         alert("No image found!");
         return;
      }

      let imgURL = img.src;
      let filename = imgURL.split("/").pop(); // Extract file name from image URL

      fetch(imgURL)
         .then(response => response.blob())
         .then(blob => {
            let url = URL.createObjectURL(blob);
            let link = document.createElement("a");

            link.href = url;
            link.download = filename; // Set the name of the file to be downloaded
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            URL.revokeObjectURL(url);
         })
         .catch(error => console.error("Error while downloading the image.", error));
   }
</script>

<div id="chart" class="mx-5">
   <img src="https://www.myqbook.com/userfiles/The%20bar%20graph%20below%20shows%20the%20colors%20of%20toy%20trains%20bought%20from%20a%20store%20last%20year.gif" alt="chart"/>
   <DownloadButton download_link={downloadIMG}/>
</div>

<style>
   #chart {
      padding: 25px;
   }

   img {
      display: block;
      margin: auto auto;
      width: 80%;
      padding-bottom: 25px;
   }
</style>