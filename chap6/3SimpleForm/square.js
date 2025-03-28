//To make objects available outside of a module you just need to expose them as additional properties on the exports object. 

exports.area = function (width) {
  return width * width;
};
exports.perimeter = function (width) {
  return 4 * width;
};