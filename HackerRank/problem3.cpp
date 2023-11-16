#include<iostream>
using namespace std;


void plusMinus(int arr[]){
   int positive = 0;
   int negative = 0;
   int zero = 0;
   int n = sizeof(arr);

   for(int i=0; i<n; i++){
    if(arr[i]>0){
        positive++;
    }
    else if(arr[i]<0){
        negative++;
    }
    else if(arr[i]==0){
        zero++;
    }
   }

   cout<<(double(positive/n));
   cout<<(double(negative/n));
   cout<<(double(zero/n));
}

int main(){

   int n;
   int inputData;
   cin>>n;
   int arr[n];
   if(n>0 && n<=100){
    for(int i=0; i<n; i++){
        cin>>inputData;
        if(inputData>=-100 && inputData<=100){
            arr[i] = inputData;
        }
    }
    plusMinus(arr);
   }


    return 0;
}