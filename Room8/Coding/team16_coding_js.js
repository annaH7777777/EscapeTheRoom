function capitalizeStringValues(obj) {
  const result = {};

  for (const key in obj) {
    const value = obj[key];

    if (typeof value === "string") {
      result[key] = value.toUpperCase();
    } else {
      result[key] = value;
    }
  }

  return result;
}
const data = {
  name: "john",
  age: 25,
  city: "yerevan"
};

console.log(capitalizeStringValues(data));
// { name: "JOHN", age: 25, city: "YEREVAN" }
