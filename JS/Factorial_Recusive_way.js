/*
Factorial applying Resursive-way

2! = (2-1)!*2
3! = (3-1)!*3
4! = (4-1)!*4
5! = (5-1)!*5

*/

function Factorial_RecusiveWay(n){
    var num = 1
    for(var i=1; i<=n-1; i++){
        num = num*i;
    }

    cal = num*3

    return cal;
}

console.log(Factorial_RecusiveWay(3))