//PRINT EACH ARRAY VALUE AND SUM SO FAR
var testArr = [6, 3, 5, 1, 2, 4];
var Sum = 0; //Set variable Sum 
for (var x = 0; x < testArr.length; x++) {//start varibale x at 1, check condition x<6
    Sum = Sum + testArr[x];         //add variable x with sum and store the result as Sum
    console.log('Num:', testArr[x] + ',', 'Sum:', Sum); // print current number and sum
}
//Output
// [Running] node "/Users/mhira/Documents/Coding Dojo/Week 6/ArrayAlgo.js"
// Num: 6, Sum: 6
// Num: 3, Sum: 9
// Num: 5, Sum: 14
// Num: 1, Sum: 15
// Num: 2, Sum: 17
// Num: 4, Sum: 21

//MULTIPLY EACH VALUE IN THE ARRAY BY ITS ARRAY POSITION
var testArr = [6, 3, 5, 1, 2, 4];
var testArr2 =[]//array 2 for console log
for (var x = 0; x < testArr.length; x++){
    testArr2[x]=testArr[x] * x;//multiply array value with its index number
}
console.log(testArr2);
// Output
// [ 0, 3, 10, 3, 8, 20 ]