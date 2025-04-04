// params.js
//   The params function and a test driver for it,
//   This example illustrates a variable number of
//   function parameters 

// Function params 
// Parameters: A variable number of parameters
// Returns: nothing
// Displays its parameters

      function params(a, b) {
        document.write("Function params was passed ",
            arguments.length, " parameter(s) <br />");
        document.write("Parameter values are: <br />");

        for (var arg = 0; arg < arguments.length; arg++)
          document.write(arguments[arg], "<br />");
          document.write(a+" "+b+"<br />");

          document.write("<br />");
        }
      
// A test driver for function params

      var a = new params("Mozart");
      
      var b = params;

      document.write(typeof(a)+"<br/>");
      console.log(a);
      console.log(b("Beethoven"));
      console.log(params("Mozart", "Beethoven"));
      params("Mozart", "Beethoven", "Tchaikowsky");

