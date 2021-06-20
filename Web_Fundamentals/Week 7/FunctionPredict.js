function greeting(){
    return "Hello";
    console.log("World");//UNreachable code. won't execute. But if outside the Function will print World after Hello
}
var word = greeting();//calling greeting function
console.log(word);
// console.log("World"); Can print World after Hello if code line is here
// OUTPUT--
// Hello
// [Done] exited with code=0 in 0.051 seconds




function add(num1, num2){//Function to add two numbers and display results per console.log
    console.log("Summing Numbers!");
    console.log("num1 is: " + num1);
    console.log("num2 is: " + num2);
    var sum = num1 + num2;
    return sum;
}
var result1 = add(3,5);// first function called
var result2 = add(4,7);// second function called
console.log(result1);
console.log(result2);
// OUTPUT---
// Summing Numbers!
// num1 is: 3
// num2 is: 5
// Summing Numbers!
// num1 is: 4
// num2 is: 7
// 8
// 11 



function highFive(num){ //print numbers less than 6 and if equals to 5 then print High Five!
    for(var i=0; i<num; i++){
        if(i == 5){// if num equals to 5, log below
            console.log("High Five!");
        }
        else{//print i
            console.log(i);
        }
    }
}
    
highFive(6);// calling function with num 6
// OUTPUT---
// 0
// 1
// 2
// 3
// 4
// High Five!