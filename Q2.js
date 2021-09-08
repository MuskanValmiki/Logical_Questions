let readlineSync = require("readline-sync");
var num = readlineSync.question("enter any number : ");
var dict = {};
for (var i =1;i <= num;i ++){
    dict[i] = i*i
}
console.log(dict)
//store key in value in dic key is number and value is that number square  