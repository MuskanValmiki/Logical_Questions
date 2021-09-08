//accesing object properties
var vegetables = {veg1:"potato",veg2:"brinjal",veg3:"bottle gourd"};
var vegetable1 = vegetables.veg1;
var vegetable2 = vegetables.veg2;
var vegetable3 = vegetables.veg3;
console.log(vegetable1);
console.log(vegetable2);
console.log(vegetable3);
  
var array = {1:"one",2:"two",3:"three"};
var array1 = array[1];
var array2 = array[2];
var array3 = array[3];
console.log(array1);
console.log(array2);
console.log(array3);

//updating a properties
var myHome = {"name": "Mussu","location":"Kanpur","Colour":"black","owner":"My home","neighbours": ["everything!"]};  
myHome.name="Muskan";
console.log(myHome);

//for add new key in object
myHome.isGood= true;
console.log(myHome);

//delete key in object
var life = {1:"muskan","2":"kajal",3:"kashish",4:"aditya",5:"kittu"};
delete life[5];
console.log(life);

//check element is there or not
var myDetails={"name":"kumar","age":24}
console.log(myDetails.hasOwnProperty("name"));
 
