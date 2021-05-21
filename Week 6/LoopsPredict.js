//Predict 1 //start a variable at 0, evaluate if num < 15 is true, print num, increment num by 1. Continue executing the code till num < 15 after incrementing num by 1
for(var num = 0; num < 15; num++){
    console.log(num);
}
// Predict 1 Output 
// 0
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
// 9
// 10
// 11
// 12
// 13
// 14

////Predict 2- start a variable 1 at 1, with a condition of i<10 check if modulus of i%3 equals to 0, print i, increment by 2. execute the code till condition is met 
for(var i = 1; i < 10; i+=2){
    if(i % 3 == 0){
        console.log(i);
    }
}
// Predict 2 Output
// 

// Predict 3- 
for(var j = 1; j <= 15; j++){
    if(j % 2 == 0){
        j+=2;
    }
    else if(j % 3 == 0){
        j++;
    }
    console.log(j);
}
// Predict 3 Output
// 1
// 4
// 5
// 8
// 10
// 11
// 14
// 16