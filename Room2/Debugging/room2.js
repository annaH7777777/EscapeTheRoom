//Fix the function so it correctly counts vowels in a string.

function countVowels(str) {
  let vowels = 'aeiou'; // vowels to check
  let count = 0;

  for (let char of str.toLowerCase()) { // make case‑insensitive
    if (vowels.includes(char)) {
      count++;
    }
  }

  return count;
}

console.log(countVowels("hello"));    // 2
console.log(countVowels("education")); // 5
