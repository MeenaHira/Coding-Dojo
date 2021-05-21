// Print odd numbers between 1-20
for (var num = 1; num < 20; num += 2) {
    //start variable num at 1, check condition num<20

    if (num % 2 != 0) {//check if num not divisible by 2
        console.log(num);
    }
}
//print num and increment by 1, repeat the loop 
//Odds Output
// 1
// 3
// 5
// 7
// 9
// 11   
// 13
// 15
// 17
// 19

//Print the number between 1-5 and sum of previus sum and current number
// Sum numbers from 1 to 5, printing out the current number and sum so far at each step of the way
var Sum = 0; //Set variable Sum to 0
for (var x = 1; x <= 5; x++) {//start varibale x at 1, check condition x<=5
    Sum = Sum + x;         //add variable x with sum and store the result as Sum
    console.log('Num:', x + ',', 'Sum:', Sum); // print current number and sum
}
// Output
// Num: 1, Sum: 1
// Num: 2, Sum: 3
// Num: 3, Sum: 6
// Num: 4, Sum: 10
// Num: 5, Sum: 15

var arr =[2,4,6,8,10];
for (var i=0; i<arr.length; i++){
    console.log(i);
    console.log(arr[i]);
}