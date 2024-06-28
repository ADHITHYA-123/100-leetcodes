import java.util.*;

public class Remove_duplicate7 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the size of the array : ");
        int size,i,l=1;
        size= sc.nextInt();
        int[] array=new int[size];
        System.out.println("Enter the elements of the array : ");
        for(i=0;i<size;i++){
            array[i]=sc.nextInt();
        }
        for(i=1;i<size;i++){
            if(array[i]!=array[i-1]){
                array[l]=array[i];
                l+=1;
            }
        }
        System.out.println("No. of unique elements is : "+l);

        sc.close();
    }
}
