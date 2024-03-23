

import java.util.Scanner;

public class BigSort {
    

    // Insert Data Into Array, 
    public void InsertDataInArray(int n, int[] arr){
        for(int a=0; a<n; a++){
            Scanner sc2 = new Scanner(System.in);
            arr[a] = sc2.nextInt();
        }
    }

    // Print Array's Data,
    public void PrintData(int n,int[] arr){
        for(int a=0; a<n; a++){
            System.out.println(arr[a]);
        }
    }

    // Big Sort Method, 
    public void Bigsort(int n, int[] arr){
        int temp = 0;
        for(int a=0; a<n; a++){
            for(int b=a+1; b<n; b++){
                if(arr[a]>arr[b]){
                    temp = arr[a];
                    arr[a] = arr[b];
                    arr[b] = temp;
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc1 = new Scanner(System.in);
        int n = sc1.nextInt();
        int[] unsorted = new int[n];

        BigSort bs = new BigSort();
        bs.InsertDataInArray(n,unsorted);
        bs.Bigsort(n, unsorted);
        bs.PrintData(n, unsorted);
        
    }
}
