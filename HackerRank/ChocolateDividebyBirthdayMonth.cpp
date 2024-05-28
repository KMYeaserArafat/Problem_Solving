
#include<iostream>
using namespace std;


int birthday(int arr[],int d,int m,int n){
    int count = 0;
    int sum = 0;
    // Solution 1
    for (int i = 0; i<n; ++i) {
        sum = 0;
        // length of the segment
        for (int j = 0; j < m; ++j)
            sum += arr[i + j];
        if (sum == d) // sum of the values in segment
            ++count;
    }
    // Solution 2 // O(1)
    for (int i = 0; i < m; ++i)
        sum += arr[i];
    if (sum == d)
        ++count;
    for (int i = m; i < n; ++i) {
        sum = sum - arr[i - m] + arr[i];
        if (sum == d)
            ++count;
    }
    return count;
}

int main(){
    int n;
    cin>>n;

    int arr[n];

    for(int a=0; a<n; a++){
        cin>>arr[a];
    }
    
    int d, m;
    cin>>d;
    cin>>m;

   cout<<birthday(arr,d,m,n);



    return 0;
}