function flattenOneLevel(arr) {
  return arr.flat(1); // flattens only one level
}

// Example:
const nested = [1, [2, 3], 4, [5, 6]];
console.log(flattenOneLevel(nested)); // [1, 2, 3, 4, 5, 6]
