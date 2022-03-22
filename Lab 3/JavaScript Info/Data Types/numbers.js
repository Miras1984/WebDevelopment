let a = +prompt("The first number?", "");
let b = +prompt("The second number?", "");

alert(a + b);



alert(Math.round(6.35 * 10) / 10);



function readNumber(){
    a = prompt("Enter a number");
    if(isFinite(a)) return alert(a);
    else if(a === "") return alert(null);
    return readNumber();
}
readNumber();


let i = 0;
while (i != 10) {
    i += 0.2;
} // will never stop because i won't be equal exactly 10


function random(min, max) {
    return min + Math.random() * (max - min);
}

alert( random(1, 5) );
alert( random(1, 5) );
alert( random(1, 5) );
