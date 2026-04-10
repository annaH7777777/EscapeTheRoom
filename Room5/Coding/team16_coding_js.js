function deepClone(obj) {
  if (obj === null || typeof obj !== "object") {
    return obj; // return primitives as is
  }

  const clone = Array.isArray(obj) ? [] : {};

  for (let key in obj) {
    clone[key] = deepClone(obj[key]);
  }

  return clone;
}
const original = {
  name: "John",
  age: 30,
  info: {
    city: "Yerevan",
    country: "Armenia"
  }
};

const copy = deepClone(original);

copy.info.city = "Gyumri";

console.log(original.info.city); // "Yerevan"
console.log(copy.info.city);     // "Gyumri"
