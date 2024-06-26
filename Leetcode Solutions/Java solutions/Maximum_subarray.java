import java.util.*;
public class Maximum_subarray{
    public static int Max_subarray(int[] array){
        int max_sum=array[0];
        int curr_sum=0;
        for(int i=0;i<array.length;i++){
            if (curr_sum<0){
                curr_sum=0;
            }
            curr_sum+=array[i];
            max_sum=Math.max(curr_sum,max_sum);
        }
        return max_sum;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the size of the array :");
        int size=sc.nextInt();
        int[] array=new int[size];
        System.out.println("Enter the elements in the array :");
        for(int i=0;i<size;i++){
            array[i]=sc.nextInt();
        }
        System.out.println("The maximum subarray sum is : "+Max_subarray(array));
        sc.close();
    }
}