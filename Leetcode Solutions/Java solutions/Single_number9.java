import java.util.*;
public class Single_number9 {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        int size,i;
        System.out.print("Enter the size of the array: ");
        size=sc.nextInt();
        int[] array=new int[size];
        System.out.println("Enter the elements of the array : ");
        for(i=0;i<size;i++){
            array[i]=sc.nextInt();
        }
        int res=0;
        for(i=0;i<size;i++){
            res=res^array[i];
        }
        System.out.println("The single number is : "+res);

        sc.close();
    }
}
