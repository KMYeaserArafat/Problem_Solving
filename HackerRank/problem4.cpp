/*
'''
atfirst declear a[] & b[] 2 array, 

If a[i] > b[i], then Alice is awarded 1 point.
If a[i] < b[i], then Bob is awarded 1 point.
If a[i] = b[i], then neither person receives a point.

Input 
17 28 30
99 16 8

Output
2 1

*/


#include<iostream>
using namespace std;


void compareTripletes(int a[], int b[]){
     int Alice = 0;
     int bob = 0;

     for(int i=0; i<3; i++){
        if(a[i]>b[i]){
            Alice+=1;
        }
        else if(a[i]<b[i]){
            bob+=1;
        }
        else if(a[i]==b[i]){
            //cout<<"Neither person receives a point."<<endl;
        }
     }

    cout<<Alice<<" "<<bob<<endl;
}





int main(){



    int a[3], b[3];

    for(int i=0; i<3; i++){
        cin>>a[i];
    }

    for(int i=0; i<3; i++){
        cin>>b[i];
    }

    compareTripletes(a,b);


    return 0;
}