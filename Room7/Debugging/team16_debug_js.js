async function getData() {
  return "data";
}

async function useData() {
  const response = await getData(); // wait for the Promise
  console.log(response); // just log the string
}
