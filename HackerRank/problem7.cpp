/*

plusMinus Problem, 

1. Take User Input How Much Data want-to take in a array, n--> 5
2. Take n number of Data into the array, 
3. Find out the How much positive Data, Negative Data, Zero Numner
    Example :->  possitive = 2, negative = 2, zero = 1
4. Divide Positive, negetive, zero by n
    Example :-> positive/n, negative/n, zero/n

*/

#include<iostream>
using namespace std;

void PlusMinus(int arr[],int n){
    int positive = 0;
    int negative = 0;
    int zero =  0;

    for(int i=0; i<n; i++){
        if(arr[i]==0){
            zero++;
        }
        if(arr[i]>0){
            positive++;
        }
        if(arr[i]<0){
            negative++;
        }
    }

    double Pn = positive/double(n);
    double Nn = negative/double(n);
    double Zn = zero/double(n);

    cout<<Pn<<endl;
    cout<<Nn<<endl;
    cout<<Zn<<endl;
}


int main(){

    int n;
    cin>>n;

    int arr[n];

    for(int i=0; i<n; i++){
        cin>>arr[i];
    }

    PlusMinus(arr,n);


    return 0;
}