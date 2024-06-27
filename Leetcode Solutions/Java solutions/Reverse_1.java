import java.util.*;
public class Reverse_1 {
    public static void main(String args[]) {
        Scanner s=new Scanner(System.in);
        System.out.println("Enter the size of the array :");
        int n=s.nextInt();
        char[] array=new char[n];
        System.out.println("Enter the characters in the array :");
        for(int i =0;i<n;i++)
        {
            array[i]=s.next().charAt(0);
        }
        System.out.println("The String is : "+new String(array));
        reverse(array,n);
        System.out.println("The Reversed string is : "+new String(array));
        s.close(); 
    }
    public static void reverse(char[] array,int n){
        int l=0,r=n-1;
        while(l<r)
        {
            char temp=array[l];
            array[l]=array[r];
            array[r]=temp;
            l++;
            r--;
        }
       
    }
}
