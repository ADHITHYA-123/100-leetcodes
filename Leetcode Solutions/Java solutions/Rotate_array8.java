import java.util.Scanner;

public class Rotate_array8 {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        int size,i,k,l,r,temp;
        System.out.print("Enter the size of the array :");
        size=sc.nextInt();
        int[] array=new int[size];
        System.out.print("Enter the number of rotation :");
        k=sc.nextInt();
        System.out.println("Enter the elements of the array :");
       
        for(i=0;i<size;i++){
            array[i]=sc.nextInt();
        }
        System.out.print("The current array is : ");
        for(i=0;i<size;i++){
            System.out.print(array[i]+" ");
        }
        l=0;
        r=size-1;
        while(l<r){
            temp=array[l];
            array[l]=array[r];
            array[r]=temp;
            l=l+1;
            r=r-1;
        }
        l=0;
        r=k-1;
        while(l<r){
            temp=array[l];
            array[l]=array[r];
            array[r]=temp;
            l=l+1;
            r=r-1;
        }
        l=k;
        r=size-1;
        while(l<r){
            temp=array[l];
            array[l]=array[r];
            array[r]=temp;
            l=l+1;
            r=r-1;
        }
        System.out.println("");
        for(i=0;i<size;i++){

            System.out.print(array[i]+" ");
        }
        sc.close();
    }
    
}
