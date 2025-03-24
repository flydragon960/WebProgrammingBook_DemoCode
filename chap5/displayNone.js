// showHide.js
//   Illustrates visibility control of elements
     
// The event handler function to toggle the visibility 
//    of the images of Saturn 

function flipImag() {
  dom = document.getElementById("nebula1").style;  
  //dom.display = "none";
  


// Flip the visibility adjective to whatever it is not now 
 if (dom.display == "inline")
   dom.display = "none";
    else
   dom.display = "inline";
}
