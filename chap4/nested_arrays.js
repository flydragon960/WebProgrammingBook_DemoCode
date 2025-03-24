var nested_array = [[2, 4, 6], [1, 3, 5], [10, 20, 30]];

for(var row = 0; row<= 2; row++){
	document.write("row ",row, ": ");
	for(var col = 0; col <= 2; col++)
		document.write(nested_array[row][col], " ");
	document.write("<br />");
}