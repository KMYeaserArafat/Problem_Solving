
#include<iostream>
using namespace std;

// For insert data into Unsorted array, 
void InsertDataInArray(int n,int unsorted[]){
    for(int a=0; a<n; a++){
        cin>>unsorted[a];
    }
}

// Print Array's Data : 
void printArray(int n, int arr[]){
    for(int a=0; a<n; a++){
        cout<<arr[a]<<endl;
    }
}

// Big Sort Method, 
void BigSort(int n,int arr[]){
    int temp; 
    for(int a=0; a<n; a++){
        for(int b=a+1; b<n; b++){
            if(arr[a]>arr[b]){
                temp = arr[a];
                arr[a]=arr[b];
                arr[b]=temp;
            }
        }
    }
}


int main(){
    int n;
    cin>>n;
    int unsorted[n];
    InsertDataInArray(n,unsorted);
    BigSort(n,unsorted);
    printArray(n,unsorted);


    return 0;
}