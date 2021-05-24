var users = [
    {
        name: "Michael",
        age: 37
    },
    {
        name: "John",
        age: 30
    },
    {
        name: "David",
        age: 27
    }
];

// 1)print/log John's age?
console.log("John's age is:",(users[1].age))
// OUTPUT: John's age is: 30

// 2)print/log the name of the first object?
console.log("Name of first object/user is:",(users[0].name))
// OUTPUT: Name of first object/user is: Michael

// 3) print/log the name and age of each user using a for loop?
for (var i=0; i<users.length; i++){
    console.log(users[i]["name"],"-", users[i]["age"]);  
}
// OUTPUT
// Michael - 37
// John - 30
// David - 27
