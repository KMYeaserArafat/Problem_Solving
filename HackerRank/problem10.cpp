/*
You are in charge of the cake for a child's birthday. 
You have decided the cake will have one candle for each year of their total age. 
They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

Input: 
---------
4
arr = [3, 2, 1,3]

Output:
----------
2
*/

#include<iostream>
#include <unordered_map>
using namespace std;


int birthdayCakeCandles(int candles[], int n){

    unordered_map<int, int> frequencyMap;
    for(int i=0; i<n; i++){
        frequencyMap[candles[i]]++;
    }

    int maxOccurrence = 0;
    int tallestCandle = 0;
    for (const auto& pair : frequencyMap) {
        if (pair.second > maxOccurrence) {
            maxOccurrence = pair.second;
            tallestCandle = pair.first;
        }
    }


    return maxOccurrence;
}


int main(){

    int n;
    cin>>n;
    int candles[n];

    //Insert Data, 
    for(int a=0; a<n; a++){
        cin>>candles[a];
    }

    cout<<birthdayCakeCandles(candles,n);


    return 0;
}