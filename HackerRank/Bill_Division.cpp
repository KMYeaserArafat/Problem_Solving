//Bill Divicion, 

#include<iostream>
using namespace std;

int main(){

    int n,k;
    cin>>n>>k;
    int bill[n];
    int sum = 0;

    for(int a=0; a<n; a++){
        int c = 0;
        cin>>c; 
        if(a !=c){
            sum +=a;
        }
    }

    int l = 0;
    cin>>l;
    if(sum/2==l){
        cout<<"Bon Appetit";
    }
    else{
        cout<<l-sum/2;
    }

    return 0;
}