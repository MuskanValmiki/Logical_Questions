var array = [1,0,0,1,1,0,1,1];
var a = 0;
var sum = 0;
var i = array.length-1;
while (i>=0){
    sum = sum + array[i]*2**a;
    a ++;
    i --;
}
console.log(sum);
