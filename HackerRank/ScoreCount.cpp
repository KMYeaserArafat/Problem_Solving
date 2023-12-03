

#include<iostream>
using namespace std;

int main(){

    int n; 
    cin>>n;
    int scores[n];

    //Insert Data, 
    for(int a=0; a<n; a++){
        cin>>scores[a];
    }

    int maximum = scores[0];
    int minimum = scores[0];
    int max  =0;
    int min = 0;

    for(int a=1; a<n; a++){
        if(scores[a]>maximum){
            maximum = scores[a];
            max++;
        }

        if(scores[a]<minimum){
            minimum = scores[a];
            min++;
        }
    }

    cout<<max<<" "<<min<<endl;


    return 0;
}