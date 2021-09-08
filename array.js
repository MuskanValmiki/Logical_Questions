// create array
let names = ['muskan','kajal','kashish','aditya'];
console.log(names.length);

//acess element from array
let plays = ['kanpur','pune','banglore','agra'];
console.log(plays[0]);

//loop over an array
let array = [1,2,3,4,5,6];
for (var i = 0;i<array.length;i++){
    console.log(i,'index');
    console.log(array[i],'element of array');
}

// add any elememt at the last
let fruits = ['apple','banana'];
fruits.push('mango');
console.log(fruits);

//remove the element at the last
let family = ['papa','maa','bhai','di','me','batu','pgl'];
family.pop();
console.log(family);

// if you want to remove any element for beggning so shift use
var array_ = [0,1,2,3,4,5];
array_.shift();
console.log(array_);

//if you want to ad any element for beggning so unshift use
let num = [1,2,3,4,5,6,7,8,9];
num.unshift(0);
console.log(num);

//find index of array
let num1 = ['a','b','c','d','e'];
let postiotion = num1.indexOf();
console.log(num1);
console.log(postiotion);

//remove any element 
let fruits_ = ['Apple', 'Banana', 'Orange']; 
let removedItem = fruits_.splice(1,1);
console.log(removedItem);
console.log(fruits_);



