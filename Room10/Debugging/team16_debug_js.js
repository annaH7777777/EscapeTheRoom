function validateString(str) {
  if (str.length === 5 && str.includes("js")) {
    return "Good job";
  } else {
    return "Try again";
  }
}

console.log(validateString("js123"));
