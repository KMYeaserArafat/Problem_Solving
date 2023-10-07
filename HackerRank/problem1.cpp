//Complete the function solveMeFirst to compute the sum of two integers.

#include<iostream>
using namespace std;


int solveMeFirst(int a,int b){
    if(a>=1 && a<=1000 && b>=1 && b<=1000){
         int sum = a+b;
         return sum;
    }
    return -1;
    
}

int main(){

    int a, b;
    cin>>a>>b;
    int calculation = solveMeFirst(a,b);
    cout<<calculation<<endl;

   

    return 0;
}