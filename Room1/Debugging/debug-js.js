function testScope() {
  let x = 1; // Function-scoped (or outer block)
  if (true) {
    let x = 2; // Block-scoped to this 'if' statement
    console.log("Inside block:", x); // Output: 2
  }
  console.log("Outside block:", x); // Output: 1
}

testScope();