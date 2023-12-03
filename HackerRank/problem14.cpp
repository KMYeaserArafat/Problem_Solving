
#include<iostream>
using namespace std;


int main(){

    int m,n;
    cin>>n;
    cin>>m;

    int a[n];
    int b[m];

    //input data into a[n],
    for(int i=0; i<n; i++){
        cin>>a[i];
    }

    //input data into b[m],
    for(int j=0; j<m; j++){
        cin>>b[j];
    }



    short(a);
    short(b);

    bool cheack_a, cheack_b;
    int demo = 0;

    for(int i=a[n-1]; i<b[0]; i+=a[n-1]){
        cheack_a = true;
        cheack_b = true;

        for(int j=0; j<n; j++){
            if(i%a[j] != 0){
                cheack_a = false;
                break;
            }
        }


        for(int j=0; j<m; j++){
            if(i%b[j] !=0){
                cheack_b = false;
                break;
            }
        }

        if(cheack_a==cheack_b && cheack_a==true){
            demo++;
        }
    }

    cout<<demo<<endl;

    return 0;
}