//Fix the async function to properly wait for multiple Promises using the correct syntax.

async function loadData() {
    const result = await Promise.all("first", "second");
    console.log(result);
  }