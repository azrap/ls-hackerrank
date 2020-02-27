*
 * Complete the 'subsetA' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY arr as parameter.
 * /

function subsetA(arr) {
    // Write your code here
    let arrA = [];
    let arrB = arr.sort(function (a, b) { return b - a });
    let sumA = arrA.reduce((a, b) => a + b, 0);
    let sumB = arrB.reduce((a, b) => a + b, 0);

    while (sumA < sumB) {

        arrA.unshift(arrB.shift());
        console.log("arrA", arrA);
        console.log("arrB", arrB);

        sumA = arrA.reduce((a, b) => a + b, 0);
        sumB = arrB.reduce((a, b) => a + b, 0);
    }

    return arrA;
}