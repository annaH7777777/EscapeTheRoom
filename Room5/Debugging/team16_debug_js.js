function fetchData() {
  return Promise.resolve("data");
}

fetchData()
  .then(data => {
    console.log(data);
    console.log("Done");
  });
