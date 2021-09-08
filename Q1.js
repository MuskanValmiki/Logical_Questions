var d1 = {'a': 100, 'b': 200, 'c':300};
var d2 = {'a': 300, 'b': 200, 'd':400};
for (key in d1){
     if(key in d2){
         d2[key]=d1[key]+d2[key];
     }
     else{
         d2[key]=d1[key];
    }
}
console.log(d2);
//same key add and different also in dic