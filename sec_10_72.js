var employee = {
    name : "Sachin Tendulkar",
    job : "Cricketer",
    age : 40,
    nameLen : function () {
        console.log(this.name.length);
    }
}

var emp = {
    name : "Sachin Tendulkar",
    job : "Cricketer",
    age : 40,
    report = function() {
        alert("Name is"+this.name+" Job is: "+this.job+", Age is: "+this.age);
    }
}

var emp = {
    name : "Sachin Tendulkar",
    job : "Cricketer",
    age : 40,
    lastName : function(){
        console.log(this.name.split(" ")[1])
    }
}