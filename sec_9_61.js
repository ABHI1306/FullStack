var firstName = prompt("First name please: ")
var lastName = prompt("Last name please: ")
var age = prompt("How old you are?")
var height = prompt("What is your height?")
var petName = prompt("What is your pet name: ")
alert("Thank you so much for the information..")

var nameCond = null;
var ageCond = null;
var heightCond = null;
var petCond = null;

if (firstName[0] === lastName[0]) {
    nameCond = true;
}else{
    nameCond = false;
}

if (age > 20 && age < 30) {
    ageCond = true;
}else{
    ageCond = false;
}

if (height >= 170) {
    heightCond = true;
}else{
    heightCond = false;
}

if (petName[petName.length-1] === "y") {
    petCond = true;
}else{
    petCond = false;
}

if (nameCond && ageCond && heightCond && petCond) {
    console.log("Welcome spy!!");
}else{
    console.log("Nothing to see here!!")
}