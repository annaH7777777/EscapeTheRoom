function chainPromises(p1, p2) {
  return p1.then(result1 => {
    return p2.then(result2 => {
      return [result1, result2];
    });
  });
}
const p1 = Promise.resolve(10);
const p2 = Promise.resolve(20);

chainPromises(p1, p2)
  .then(result => {
    console.log(result); // [10, 20]
  });
