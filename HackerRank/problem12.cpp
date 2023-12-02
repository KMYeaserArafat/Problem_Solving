/*
Input s, = 7 (Starting)
Input t, = 10 (ending)
here house range[7-10]

Apple Tree position -> a = 4
Orange Tree position -> b = 12

Total Apple = 3
Total Orange = 3

Apples Position = [2,3,-4]
Orange Position = [3,-2,-2]

landPositionofApple = [4+2, 4+3, 4+-4] = [6,7,0]
labdPositionOfOrange = [12+3, 12+-2, 12+-4] = [15,10,8]

In the House Range = 7-10, 
In the HouseRange, Apple = 1
In the HouseRange, Orange = 2

*/

#include<iostream>
using namespace std;

void countApplesAndOranges(){
    //here declear the house range, 
    int s,t;
    cin>>s;
    cin>>t;

    //tree position, 
    int a,b;
    cin>>a;
    cin>>b;
   
   //total apple, orange,
    int apple,orange;
    cin>>apple;
    cin>>orange;

    //position, 
    int positionApple[apple];
    int positionOrange[orange];

    for(int a=0; a<apple; a++){
        cin>>positionApple[a];
    }

    for(int o=0; o<orange; o++){
        cin>>positionOrange[o];
    }

    //land-position, 
    int landPositionApple[apple];
    int landPositionOrange[orange];

//for apple, 
    for(int i=0; i<apple; i++){
        int p1 = positionApple[i]+a;
        landPositionApple[i] = p1;
    }

//for orange,
    for(int j=0; j<orange; j++){
        int p2 = positionOrange[j]+b;
        landPositionOrange[j] = p2;
    }

    int applecount = 0;
    int orangecount = 0;

    for(int x=0; x<apple; x++){
        if(landPositionApple[x]>=s && landPositionApple[x]<=t){
            applecount++;
        }
    }

    for(int y=0; y<orange; y++){
        if(landPositionOrange[y]>=s && landPositionOrange[y]<=t){
            orangecount++;
        }
    }

    cout<<applecount<<endl;
    cout<<orangecount<<endl;


}

int main(){

    countApplesAndOranges();

    return 0;
}