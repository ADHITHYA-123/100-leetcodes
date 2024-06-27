import java.util.Scanner;

public class Move_zeros6{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int size,i,l=0,temp;
        System.out.print("Enter the size of the array: ");
        size=sc.nextInt();
        int[] array=new int[size];
        for(i=0;i<size;i++){
            System.out.print("Enter the element "+(i+1)+": ");
            array[i]=sc.nextInt();
        }
        for(i=0;i<size;i++){
            if(array[i]!=0){
                temp=array[l];
                array[l]=array[i];
                array[i]=temp;
                l+=1;
            }
        }
        for(i=0;i<size;i++){
            System.out.print(array[i]+" ");
        }
        sc.close();
    }
}
