import java.util.Scanner;

public class FibonacciDP {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        System.out.print("Enter the size of fibonacci sequence to be printed : ");
        int n=sc.nextInt();
        int arr[]=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=0;
        }
        arr[1]=1;
        arr[0]=1;
        for(int i=2;i<n;i++){
            arr[i]=arr[i-1]+arr[i-2];
        }
        for(int x:arr){
            System.out.print(x+" ");
        }
        sc.close();
    }
    
}
