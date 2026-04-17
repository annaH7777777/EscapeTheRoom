function fetchData(url) {
  fetch(url)
    .then(response => response.json()) // ✅ call the function
    .then(data => console.log(data))
    .catch(error => console.error("Error:", error));
}

fetchData("https://jsonplaceholder.typicode.com/posts/1");
