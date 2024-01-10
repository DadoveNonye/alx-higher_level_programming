#!/usr/bin/node
let ArgCount = 0;
for (const arg in process.argv){
	ArgCount++;
}
if (ArgCount === 2){
	console.log("No argument");
}else{
	console.log(process.argv[2]);
}
