function plane(newMake, newModel, newYear){   
   this.make = newMake;
   this.model = newModel;
   this.year = newYear;
   this.display = displayPlane;

 }

 
function displayPlane() {
   document.write("Make: ", this.make,
                  "<br />");
   document.write("Model: ", this.model,
                  "<br />");
   document.write("Year: ", this.year,
                  "<br />");
 }

const myPlane = new plane("Cessna",
                     "Centurnian", 
                     "1970");
myPlane.display();

