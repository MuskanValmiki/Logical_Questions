//simple while loop
var a = 1;
while(a <= 100){
    if (a%2==0){
        console.log("love you mummy");
    }
    else{
        console.log("love you papa");
    }
  a = a + 1
}

//simple for  loop
for(var i = 0; i < 3; i++){
    if (i%2==0){
       console.log("di");
    }
    else{
        console.log("bhai");
    }
}


//do while loop
var i=1;
do{
  if(i%2==1){
  console.log(i);
  }
  i++
}
while (i <=10);

//for in loop is a special type of loop that iterates over the object or an array of elements.
var names = ["Muskan", "Anu", "Shivanshi"];
for (name in names){
console.log(names[name]);
console.log(name);
}

var person={"name":"muskan","surname":"Valmikee","age":18}
for (person_details in person){
console.log(person_details+ " = "+person[person_details]);
}

//for of loop is run the array but it can't run object.
arr=["a","b","g","r","t"]
for(let le of arr){
console.log(le);
}

//To find the length of an object we can use Object.keys() either we can use  Object.values().
const birds={name:"Bald Eagle",type:"Hawk",
   ScientificName:"HaliaeetusLeucocephalus"}         
console.log(Object.keys(birds).length);
