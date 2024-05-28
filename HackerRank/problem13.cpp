/*
Wanbo Problem, 
Here have 2 kangaroo, x1 and x2; 
2 kangaroo has 2 another jumping point, v1,v2;
2 kangaroo last ending point (x)  is same, print YES otherwise print NO.

Example, 
x1= 2,
v1 =1,
x2 = 1,
v2 = 2,

if (x1+v1) == (x2+v2) are same print YES, 
else: print NO,

Sample Input : 0 3 4 2
Sample Output: YES
*/

#include<iostream>
using namespace std;

void kangaroo(){
    int x1,v1,x2,v2;
    cin>>x1;
    cin>>v1;
    cin>>x2;
    cin>>v2;

    int kangaroo1 = (x1+v1);
    int kangaroo2 = (x2+v2);

    if(kangaroo1==kangaroo2 && x2>x1 || v2>v1){
        cout<<"YES";
    }
    else{
        cout<<"NO";
    }


}

int main(){

    kangaroo();


    return 0;
}