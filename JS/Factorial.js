/*
Factorial 

2! = 1*2
3! = 1*2*3
4! = 1*2*3*4
5! = 1*2*3*4*5
*/


function factorial(n){
    var number = 1
    for(var i=1; i<=n; i++){
        number = number*i;
    }
    return number;
}

console.log(factorial(3))