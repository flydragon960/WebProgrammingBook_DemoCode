// showHide.js
//   Illustrates visibility control of elements
     
// The event handler function to toggle the visibility 
//    of the images of Saturn 

function rememberName() {
  dom = document.getElementById("saturn").style; 
  name = document.getElementById("custName").value; 
  placeholder = document.getElementById("saturn");
  placeholder.value = name;

  //dom = name;

  alert("custName=" + name + "; placeholder=" + placeholder.value);

 // document.write("<br/>"+name);

// Flip the visibility adjective to whatever it is not now 
 if (dom.visibility == "visible")
   dom.visibility = "hidden";
 else
   dom.visibility = "visible";
}
