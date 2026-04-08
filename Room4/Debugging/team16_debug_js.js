function filterPositives(arr) {
  return arr.filter(num => num > 0);
}

console.log(filterPositives([-1, 2, -3, 4])); // [2, 4]