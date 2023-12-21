
//Sales by Match

#include<iostream>
using namespace std;

int sockMerchant(int arr[],int n){
    int num = 0;
    for(int i=0; i<n; i++){
        int id = 1;
        for(int j=i+1; j<n; j++){
            if(arr[i]==arr[j] && id==1){
                num+=1;
                id+=1;
            }
        }
    }
    return num;
}


void InsertData(int arr[],int n){
    for(int a=0; a<n; a++){
        cin>>arr[a];
    }
}

int main(){
    int n; 
    cin>>n;
    int arr[n];
    InsertData(arr,n);
    cout<<sockMerchant(arr,n);



    return 0;
}