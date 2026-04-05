function flattenObject(obj, parentKey = '', result = {}) {
  for (let key in obj) {
    const newKey = parentKey ? `${parentKey}.${key}` : key;

    if (typeof obj[key] === 'object' && obj[key] !== null && !Array.isArray(obj[key])) {
      // Recursive call for nested objects
      flattenObject(obj[key], newKey, result);
    } else {
      result[newKey] = obj[key];
    }
  }

  return result;
}

//Example Usage
const nested = {
  user: {
    name: "Alice",
    address: {
      city: "Paris",
      zip: "75000"
    }
  },
  active: true
};

console.log(flattenObject(nested));
