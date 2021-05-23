// 1) Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255.
function counter(startnum) {
    var numberArray = [];// set a variable
    for (var num = startnum; num <= 255; num++) { 
        numberArray.push(num);// if number is <=255 enter the number to numberArray
    }
    console.log(numberArray);
}
counter(1);
// Output
// [1,  2,  3,   4,  5,  6,  7,  8,  9, 10, 11, 12,
// 13, 14, 15,  16, 17, 18, 19, 20, 21, 22, 23, 24,
// 25, 26, 27,  28, 29, 30, 31, 32, 33, 34, 35, 36,
// 37, 38, 39,  40, 41, 42, 43, 44, 45, 46, 47, 48,
// 49, 50, 51,  52, 53, 54, 55, 56, 57, 58, 59, 60,
// 61, 62, 63,  64, 65, 66, 67, 68, 69, 70, 71, 72,
// 73, 74, 75,  76, 77, 78, 79, 80, 81, 82, 83, 84,
// 85, 86, 87,  88, 89, 90, 91, 92, 93, 94, 95, 96,
// 97, 98, 99, 100,... 155 more items]




// 2) Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator for this exercise.
function SumofEvenNumbers(startnum){
    var sum =0;
    for (var i=1; i<=1000; i++){
        if (i%2 == 0){// if modulus of i with 2 is 0(0 remainder), number is even
            sum=sum + i //add even number to sum
        } 
    }
    console.log("Sum of Even Numbers between 1 to 1000 is:", sum)
}
SumofEvenNumbers(1);
// OUTPUT
// Sum of Even Numbers between 1 to 1000 is: 250500



// 3) Sum odd 5000 - Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999).
function SumofOddNumbers(startnum){
    var sum =0;
    for (var i=1; i<=5000; i++){
        if (i % 2 == 1){// if modulus of i with 2 is 1(1 remainder), number is odd
            sum=sum + i//add odd number to sum
        }
    }
    console.log("Sum of Odd Numbers between 1 to 5000 is:", sum)
}
SumofOddNumbers(1);
// OUTPUT
// Sum of Odd Numbers between 1 to 5000 is: 6250000



// 4) Iterate an array - Write a function that returns the sum of all the values within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14).
function SumOfValues(array) {
    var sum = 0;
    for (var i = 0; i <array.length; i++) {
        sum= sum + array[i] //add to sum till end value of array
        }
    console.log("Sum of values in an array is:", sum)
}
var array=[-5,2,5,12];
SumOfValues(array);
// OUTPUT
// Sum of values in an array is:: 14

// 5) Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)
function MaxValueInArray(array){
    var MaxValue= 0;
    for (var i = 0; i <array.length; i++){// for loop to examine each value in the array
        if (array[i] > MaxValue){//if value is greater than MaxValue, insert to MaxValue variable
            MaxValue= array[i]; 
        }
        // return max;
    } 
    console.log('Max Value in number array is:', MaxValue)
}
var array=[-3,9,-10,7];
MaxValueInArray(array);
// OUTPUT
// Max Value in number array is: 9


// 6) Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)
function Average(numArray) {
    var sum = 0;
    var avg = 0;
    for (var i = 0; i <numArray.length; i++) {
        sum= sum + numArray[i];
        }
        avg = sum / numArray.length;
        // return avg;
        console.log('Average is:', avg)
    }
var numArray=[1,3,5,7,20];
Average(numArray);
// OUTPUT---
// Average is: 7.2


// 7) Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.
function oddArray(){
    var array = [];
    for (var x = 1; x <=50; x+=2){
        array.push(x);//start from 1 and push second number after that to array
    }
    // return array;
    console.log(array);
}
oddArray(1);
// OUTPUT
// [1,  3,  5,  7,  9, 11, 13, 15,
// 17, 19, 21, 23, 25, 27, 29, 31,
// 33, 35, 37, 39, 41, 43, 45, 47,
// 49]



// 8) Greater than Y - Given value of Y, write a function that takes an array and returns the number of values that are greater than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. (There are two values in the array greater than 3, which are 5, 7).
function greaterThanY(array, y){
    var Ycount = 0;
    for (var i = 0; i < array.length; i++){
        if (array[i] > y){ // check if value in array is greater than y
            Ycount++;//increase count when value is greater than y
        }
    }
    console.log('number of values in array greater than Y:', Ycount)
    // return counter;
}
var array= [1,3,5,7,9];
y=2;
greaterThanY(array, y);
// output
// number of values in array greater than Y: 4



// 9) Squares - Given an array with multiple values, write a function that replaces each value in the array with the product of the original value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4])
function squares(array){
    newArray=[];
    for (var i = 0; i < array.length; i++){
        array[i] = array[i]*array[i];// square each value and reassign that new value to that index
        newArray.push(array[i]);
    }
    console.log('squares of array values are:', newArray)
}
squares([1, -2, 5, 10]);
// output
// squares of array values are: [ 1, 4, 25, 100 ]




// 10) Negatives - Given an array with multiple values, write a function that replaces any negative numbers within the array with the value of 0. When the program is done the array should contain no negative values. (e.g. [1,5,10,-2] will become [1,5,10,0])
function nonNegatives(array){
    for (var i = 0; i < array.length; i++){
        if (array[i] < 0){// is each value <0, or is negative?
            array[i] = 0;//If yes-change that vallue to 0
        }
    }
    console.log(array);
}
nonNegatives([-1,2,-5]);
// output
// [ 0, 2, 0 ]



// 11) Max/Min/Avg - Given an array with multiple values, write a function that returns a new array that only contains the maximum, minimum, and average values of the original array. (e.g. [1,5,10,-2] will return [10,-2,3.5])
function MaxMinAvg(arr){
    var sum = 0;
    var max = arr[0];
    var min = arr[0];
    for (var i = 0; i < arr.length; i++){
        sum = sum + arr[i];//addition of numbers in array
        if (arr[i] > max){
            max = arr[i];//If more than max so far, add to var max
        }
        else if (arr[i] < min){
            min = arr[i];//If less than min so far, add to var min
        }
    }
    var newArr = [];
    newArr.push(max);// bring max
    newArr.push(min);//bring min
    var avg = sum/arr.length// calculate average
    newArr.push(avg);

    return newArr;
}
console.log(MaxMinAvg([2,10,-3,4]));
// output
// [ 10, -3, 3.25 ]



// 12) Swap Values - Write a function that will swap the first and last values of any given array. The default minimum length of the array is 2. (e.g. [1,5,10,-2] will become [-2,5,10,1]).
function swap(arr){
    var temp = arr[arr.length-1];//put last value in temp
    arr[arr.length-1] = arr[0];//convert array last value equal to 1st place value
    arr[0] = temp;//convert value of last value(temp value)to value in 1st place
}
var tester = [1,4,10,-2];
swap(tester);
console.log(tester);
// output
// [ -2, 4, 10, 1 ]




// 13) Number to String - Write a function that takes an array of numbers and replaces any negative values within the array with the string 'Dojo'. For example if array = [-1,-3,2], your function will return ['Dojo','Dojo',2].
function NegativesToDojo(arr){
    for (var idx = 0; idx < arr.length; idx++){
        // examine each value and see if it's negative.
        if (arr[idx] < 0){
            arr[idx] = "Dojo";
        }
    }
    console.log(arr);
}
NegativesToDojo([-1,2,-5]);
// output
// [ 'Dojo', 2, 'Dojo' ]