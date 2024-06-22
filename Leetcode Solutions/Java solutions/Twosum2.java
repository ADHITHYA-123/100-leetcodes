import java.util.*;

public class Twosum2{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int i;
        System.out.println("\nEnter the size of the array :");
        int n=sc.nextInt();
        int[] array=new int[n];
        System.out.println("Enter the elements in the array :");
        for(i=0;i<n;i++){
            array[i]=sc.nextInt();
        }
        System.out.println("Enter the target :");
        int x=sc.nextInt();
        for(i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                if(array[i]+array[j]==x){
                    System.out.println("Indices : "+i+","+j);
                }
            }
        }
    }
}