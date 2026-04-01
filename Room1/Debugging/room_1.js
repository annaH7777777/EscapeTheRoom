//Fix the scope issue so that the outer x remains 1 and the inner x is only 2.

function testScope() {
  var x = 1;
  if (true) {
    var x = 2;
    console.log("Inside block:", x);
  }
  console.log("Outside block:", x);
}