const result = {success: ["max-length", "no-amd","prefer-arrow-functions"],failure: ["no-var", "var-on-top", "linebreak"],skipped: ["no-extra-semi", "no-dup-keys"]};
for(var value in result){
   console.log(result[value]);
}
// here we are printing value