var n=require("readline-sync");
const num=n.question("enter number: ");
let i=1
var count=0;
while (i<num) {
       if (num%i===0) {
       count=count+1
       }
       i++;
}
if (count===1) {
       console.log("prime number")
}
else {
   console.log("not prime number")
}
//prime number