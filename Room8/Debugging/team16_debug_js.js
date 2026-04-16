const p1 = Promise.resolve("A");
const p2 = Promise.resolve("B");

Promise.any([p1, p2]).then(console.log);
