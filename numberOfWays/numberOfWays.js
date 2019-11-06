/*
 * Complete the 'numberOfWays' function below.
 *
 * The function is expected to return a LONG_INTEGER_ARRAY.
 * The function accepts 2D_INTEGER_ARRAY cases as parameter.
 * eg. [[1,2]]. [[4,10], [3,4]]
 */

//  * Complete the 'numberOfWays' function below.
//  *
//  * The function is expected to return a LONG_INTEGER_ARRAY.
//  * The function accepts 2D_INTEGER_ARRAY cases as parameter.
//  * /

function numberOfWays(cases) {
  let num_array = [];

  for (let i = 0; i < cases.length; i++) {
    let N = cases[i][0];
    let M = cases[i][1];

    var num_ways = 0;
    while (N > 0 && M > 0) {
      num_ways += N * M;
      N = N - 1;
      M = M - 1;
    }
    num_array.push(num_ways);

    // Write your code here
  }
  return num_array;
}

console.log(numberOfWays(2)); //expect 0
console.log(numberOfWays([2, 3])); //expect 8
console.log(numberOfWays([3, 4])); //expect 20
console.log(numberOfWays([[6, 5]])); //expect 70
