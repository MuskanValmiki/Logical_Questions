var n=require("readline-sync");
var choose_ascii=n.questionInt("enter a number:");
var i=97;
var ascii_char=i+choose_ascii;
while (i<=ascii_char){
    console.log(String.fromCharCode(i));
    i++;
}
//if we but 2 it run the loop till 97 and gave output a,b
