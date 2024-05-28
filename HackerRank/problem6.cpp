/*

Diagonal Difference, 

Input: 
------------
size : 3 (user Input)
11 2 4
4 5 6
10 8 -12

Process 1: 
-------------
11
   5
    -12

(11+5+(-12)) = 4

Process 2: 
--------------

       4
     5
  10
(4+5+10) = 19 
---------------------------------
Digonal Difference = 4-19 = -15

*/

#include<iostream>
using namespace std;



int main(){

    int n;
    int d1 = 0;
    int d2 = 0;
    cin>>n;

    int arr[n][n];

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin>>arr[i][j];

            if(i==j){
                d1 += arr[i][j];
            }

            if(i==n-j-1){
                d2 += arr[i][j];
            }
        }
    }
    int difference = abs(d1-d2);

    cout<<"Difference : "<< difference<<endl;

    return 0;
    
}