function isPalindrome(str) {
  // reverse the string
  const reversed = str.split('').reverse().join('');
  // check if the original equals the reversed
  return str === reversed;
}

// Example usage
console.log(isPalindrome("racecar")); // true
console.log(isPalindrome("dfgdgfdg"));   // fals