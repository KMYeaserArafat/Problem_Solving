

#include<iostream>
#include <climits>
using namespace std;


void minMax(int n, int arr[],int arr1[]){
      for(int i=0; i<n; i++){
        int sum = 0;

        for(int j=0; j<n; j++){
            if(i!=j){
                sum=sum+arr[j];
            }
        }
        arr1[i] = sum;
        cout<<"Without "<< i+1 << " Sumation : "<< sum<<endl;
    }

    int minvalue = INT_MAX;
    int maxvalue = INT_MIN;

    for(int a=0; a<n; a++){
        if(arr1[a]<minvalue){
            minvalue = arr1[a];
        }

        if(arr1[a]>maxvalue){
            maxvalue=arr1[a];
        }
    }

    cout<<minvalue<<" "<<maxvalue;

}


int main(){

    int n = 5;
    int arr[n];
    int arr1[n];

    //Insert Data, 
    for(int a=0; a<n; a++){
        cin>>arr[a];
    }

    for(int a=0; a<n; a++){
        if(1<= a && 1000000000>=a){
            minMax(n,arr,arr1);
        }
    }

    return 0;
}