//Fix the function so it correctly counts vowels in a string.

function countVowels(str) {
    let vowels = 'aeiou';
    let count = 0;
    for (let char of str) {
      if (vowels.includes == char) count++;
    }
    return count;
  }

console.log(countVowels("hello"));  // Expected Output: 2
console.log(countVowels("education")); //Expected Output: 5