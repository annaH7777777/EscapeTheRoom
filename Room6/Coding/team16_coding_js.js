//For JavaScript: Write a function that creates a Promise which resolves after a given delay (in ms).#

 function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// Example usage:
delay(2000).then(() => {
  console.log("Resolved after 2 seconds");
});
