//Predict 1:
var arr = [8, 6, 7, 5, 3, 0, 9];
for (var i = 0; i < arr.length; i++) {
    console.log(arr[i]); //print the array value at the index 1
}
// Output
// 8
// 6
// 7
// 5
// 3
// 0
// 9

//Predict 2:
var arr = [7, 3, 8, 4, 2, 0, 1];
for (var i = 0; i < arr.length; i++) { //arr.length=7, check condition and increment i
    if (arr[i] % 2 == 0) {//If index value mod with 2 is equal to 0, print value at that index
        console.log(arr[i]);
    }
    else {
        console.log("That is odd!");//If index value mod with 2 is not equal to 0, print ''That is odd!''
    }
}
//Output
// That is odd!
// That is odd!
// 8
// 4
// 2
// 0
// That is odd!

//Predict 3:
var arr = [1, 3, 8, -5, 0, -2, 4, -1];
var newArr = [];
for (var i = 0; i < arr.length; i++) {//arr.length=8, check condition and increment i
    if (arr[i] < 0) {
        newArr.push(arr[i]);
        arr[i] = arr[i] * -1;
    }
    else if (arr[i] == 0) {
        arr[i] = "Zero";
    }
    else {
        arr[i] = arr[i] * -1;
    }
}
console.log(arr);
console.log(newArr);
//Output
// [-1, -3, -8, 5,'Zero', 2, -4, 1]
// [ -5, -2, -1 ]
