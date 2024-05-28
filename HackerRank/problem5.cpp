/*
A very big sum, 
----------------------
How many number want-to take . From User take this number and fillup their values, 


here use a method whose name is a veryBigSum, his datatype is long type. 

Input: 
5
10 20 40 50 60

Output: 
180


*/

#include<iostream>
using namespace std;


long aVeryBigSum(int ar[],int n){
    long sum = 0;
    for(int i=0; i<n; i++){
       sum = sum+ar[i];
    }
   
   return sum;

}


int main(){

    int n;
    cin>>n;
    int arr[n];

    for(int i=0; i<n; i++){
        cin>>arr[i];
    }


cout<<aVeryBigSum(arr,n);




    return 0;
}