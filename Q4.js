 const n=require("readline-sync");
var name=n.question("enter any name:");
const store=name;
var string='';
for (let i=name.length-1;i>=0;i--){
    string+=name[i]
}
if (store==string){
    console.log("its palindrome string")
}
else{
    console.log("its not a palindrome string")
}
//palindrome number