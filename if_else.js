let readlineSync = require("readline-sync");
var condition = readlineSync.question("In Raksha Bandan  bhai come or not : ");
if (condition == "come" || condition == "Come"){
    console.log("Bhai",condition,"so muskan is too much happy");
    var take = readlineSync.question("which thing he will took : ");
    if (take == "mithai" || take == "Mithai"){
        console.log("muskan will eat",take);
    }
    else if (take == "rasgulla" || take == "Rasgulla"){
        console.log("bhai will eat not muskan");
    }
    else{
        console.log("he did not take any thing");
    }
}
else{
    console.log("Bhai",condition,"so muskan is not a happy");
}

