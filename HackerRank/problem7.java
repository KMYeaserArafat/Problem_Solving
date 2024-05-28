/*

plusMinus Problem, 

1. Take User Input How Much Data want-to take in a array, n--> 5
2. Take n number of Data into the array, 
3. Find out the How much positive Data, Negative Data, Zero Numner
    Example :->  possitive = 2, negative = 2, zero = 1
4. Divide Positive, negetive, zero by n
    Example :-> positive/n, negative/n, zero/n

*/


import java.util.Scanner;



public class problem7 {

    public void plusMinus(int[] arr, int n){
        int positive = 0;
        int negative = 0;
        int zero  = 0;

        for(int i=0; i<n; i++){
            if(arr[i]==0){
                zero++;
            }
            if(arr[i]>0){
                positive++;
            }
            if(arr[i]<0){
                zero++;
            }
        }

        double Pn = positive/Double.valueOf(n);
        double Nn = negative/Double.valueOf(n);
        double Zn = zero/Double.valueOf(n);


        System.out.println(Pn);
        System.out.println(Nn);
        System.out.println(Zn);
    }


    public static void main(String[] args) {
         Scanner sc1 = new Scanner(System.in);

    int size = sc1.nextInt();
    int[] arr = new int[size];

    for(int i=0; i<size; i++){
       arr[i] = sc1.nextInt();
    }

    problem7 p = new problem7();
    p.plusMinus(arr,size);


    }


}
