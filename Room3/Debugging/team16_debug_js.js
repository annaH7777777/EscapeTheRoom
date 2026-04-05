//Fix the code so that each API fetch logs the correct URL and data

function fetchData(urls) {
  for (let i = 0; i < urls.length; i++) {
    fetch(urls[i])
      .then(response => response.json())
      .then(data => console.log('Data from', urls[i], data));
  }
}

fetchData(['api/1', 'api/2', 'api/3']);