//Fix the async function to properly wait for multiple Promises using the correct syntax.


async function loadData() {
  const result = await Promise.all([
    Promise.resolve("first"),
    Promise.resolve("second")
  ]);
  console.log(result);
}
