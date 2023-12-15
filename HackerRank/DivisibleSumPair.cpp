
#include<iostream>
using namespace std;


int divisibleSumPairs(int arr[],int k,int n){

    int count = 0;

    for(int i=0; i<n; i++){
        int temp = arr[i];
        for(int j=i+1; j<n; j++){
            int sum = temp+arr[j];
            if(sum%k==0){
                count++;
            }
        }
    }

    return count;
}

int main(){
    int n;
    cin>>n;

    int k;
    cin>>k;

    int arr[n];
    for(int a=0; a<n; a++){
        cin>>arr[a];
    }

    cout<<divisibleSumPairs(arr,k,n);




    return 0;
}