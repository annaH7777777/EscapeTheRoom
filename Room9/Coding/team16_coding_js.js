function sortByNumericKey(arr, key) {
  return [...arr].sort((a, b) => a[key] - b[key]);
}
const users = [
  { name: "A", age: 30 },
  { name: "B", age: 20 },
  { name: "C", age: 25 }
];

const sorted = sortByNumericKey(users, "age");

console.log(sorted);
