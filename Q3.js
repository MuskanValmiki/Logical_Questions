var mainString = 'My name is muskan, and my friend’s name is shivanshi';
var subString = 'is';
var count = 0;
var list = mainString.split(" ");
for (var i = 0;i<list.length;i++){
    if (list[i] == (subString)){
        count ++
    }
}
console.log("The substring is there",count,"times in the main string");
//here we count substring how much time it came in mainstring