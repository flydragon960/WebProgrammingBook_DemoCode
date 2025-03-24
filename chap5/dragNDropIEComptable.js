<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Drag and drop</title>
    <script type="text/javascript" src="dragNdropIEComptable.js"></script>
</head>
<body style="font-size: 20;">
    <p>
        <!-- Your body content here -->
    </p>
</body>
</html>

// dragNDrop.js
//   An example to illustrate the DOM 2 Event model
//   Allows the user to drag and drop words to complete
//   a short poem
//   Does not work with IE7

// Define variables for the values computed by 
//  the grabber event handler but needed by mover
//  event handler

      var diffX, diffY, theElement;

// *******************************************************

// The event handler function for grabbing the word

function grabber(event) {

// Set the global variable for the element to be moved

  var theElement = event.currentTarget;

// Determine the position of the word to be grabbed,
//  first removing the units from left and top

  var posX = parseInt(theElement.style.left);
  var posY = parseInt(theElement.style.top);

// Compute the difference between where it is and 
//  where the mouse click occurred

  diffX = event.clientX - posX;
  diffY = event.clientY - posY;

// Now register the event handlers for moving and 
//  dropping the word
 
  //document.addEventListener("mousemove", mover, true);
  //document.addEventListener("mouseup", dropper, true);
  
      if (document.addEventListener){  
      document.addEventListener("mousemove", mover, true); 
      document.addEventListener("mouseup", dropper, true);  
    } else if (document.attachEvent){  
	    alert("registerIE");
      document.attachEvent("mousemove", mover);  
      document.attachEvent("mouseup", dropper);  
    }  

// Stop propagation of the event and stop any default 
//  browser action

  event.stopPropagation();
  event.preventDefault();

}  //** end of grabber

// *******************************************************

// The event handler function for moving the word

function mover(event) {

// Compute the new position, add the units, and move the word

  theElement.style.left = (event.clientX - diffX) + "px";
  theElement.style.top = (event.clientY - diffY) + "px";

// Prevent propagation of the event

  event.stopPropagation();
}  //** end of mover

// *********************************************************
// The event handler function for dropping the word

function dropper(event) {

// Unregister the event handlers for mouseup and mousemove

  document.removeEventListener("mouseup", dropper, true);
  document.removeEventListener("mousemove", mover, true);

// Prevent propagation of the event

  event.stopPropagation();
}  //** end of dropper
