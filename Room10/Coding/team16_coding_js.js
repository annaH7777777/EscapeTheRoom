function filterUsers(users) {
  return users
    .filter(user => user.age >= 18)           // keep adults
    .map(user => user.name.toUpperCase());    // capitalize names
}
const users = [
  { name: "alice", age: 17 },
  { name: "bob", age: 22 },
  { name: "charlie", age: 19 }
];

console.log(filterUsers(users));
// ["BOB", "CHARLIE"]
