// load.js
//   An example to illustrate the load event
      
// The onload event handler

function fade () {
   var dom = document.getElementById("mybody");
   let level = 1;
   function step(){
      var h = level.toString(16);  
      dom.style.backgroundColor = '#FFFF' +h +h;  
      if(level < 15) {   //level 0-15 
          level += 1;
          setTimeout(step, 200);
      }
  }
  setTimeout(step, 100);
}
