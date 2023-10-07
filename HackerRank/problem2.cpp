//Given an array of integers, find the sum of its elements.

#include<iostream>
using namespace std;


int main(){
    int n; 
    cin>>n;
    int arr[n];

    int sum = 0;


    //Insert Data, 
    for(int a=0; a<n; a++){
        cin>>arr[a];
        sum += arr[a];
    }

    cout<<sum<<endl;
  

    return 0;
}