#include<iostream>
using namespace std;


void MagratoryBirds(int arr[], int n){
    int max = 0;
    int id = 0;

    for(int i=0; i<n; i++){
        if(arr[i]>arr[max]){
            max = arr[i];
            id = i+1;
        }
    }

    cout<<id;
    
}


int main(){

    int n; 
    cin>>n;
    int arr[n];
    //insert data into the array, 
    for(int a=0; a<n; a++){
        cin>>arr[a];
    }

    MagratoryBirds(arr,n);



    return 0;
}