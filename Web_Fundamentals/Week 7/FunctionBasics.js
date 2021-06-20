// 1st ---example
function counter() {  //code to be executed  
    for(var num = 0; num <= 5; num++){
        console.log(num);
    }
}
counter();    // run the function 


// 2nd-- Example
function counter(startNum) {    //The function is expecting some PARAMETER in order to run
    for (var num = startNum ; num >= 0 ; num--) {        
        console.log(num);    
    }
}
counter(6);    // Passing in an ARGUMENT of 6, the console would display: 6, 5, 4, 3, 2, 1, 0
counter(3);    // Passing in an ARGUMENT of 3, the console would display: 3, 2, 1, 0



// 3rd---example---return VS console.log()
function createArray(num) {        
    var newArray = [];        
    for (var i = 0; i <= num; i++) {                
        newArray.push(i);        
    }        
    return newArray;        // added the return statement
}
var y = createArray(5);        // now y is the variable that is calling on createArray




// 4th--- example
function cNames(arrayOfNames) {
    var cCount = 0;
    for (var i = 0; i < arrayOfNames.length; i++) {
        if (arrayOfNames[i][0] == 'C') {
            cCount++;
        }
    }
    return cCount;
}
var names = ["Charles", "Peter", "Clinks", "Canny", "Christina", "Candy"]
console.log(cNames(names));



// 5th--- Example
function cNames(arrayOfNames) {
    var cCount = 0;
    for (var i = 0; i < arrayOfNames.length; i++) {
        for(var j=0; j<arrayOfNames[i].length; j++){
            if (arrayOfNames[i][j] == 'c' | arrayOfNames[i][j]=='c'){
                cCount++
            }
        }    
    } 
    return cCount; 
}
var names = ["Charles", "Peter", "Clinks", "Canny", "Christina", "Candy"]
console.log(cNames(names));

