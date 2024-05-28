/*

F(n)  = 0,1,1,2,3,4,5,..........n

*/

function Fibonacci_Series(n){
     fibo = [0,1]
    // find out the fibonacci series
    for(var i=2; i<=n; i++ ){
        fibo[i] = fibo[i-1]+fibo[i-2]
    }
    return fibo;
}

function Fibonacci_Series_Sum(fibo){
     // sumation of the seires, 
     sum = 0;
     for(var i=0; i<fibo.length; i++){
        sum = sum + fibo[i];
     }
     return sum;
}

console.log("Fibonacci Series : " + Fibonacci_Series(4));
console.log("Fibonacci Series Sumation : " + Fibonacci_Series_Sum(Fibonacci_Series(4)))
