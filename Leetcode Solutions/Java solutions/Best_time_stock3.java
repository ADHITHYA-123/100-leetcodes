import java.util.*;
public class Best_time_stock3 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of the array : ");
        int size = sc.nextInt();
        int array[]=new int[size];
        System.out.println("Enter the elements in the array : ");
        for(int i=0;i<size;i++){
            System.out.println("Enter the price of stock on day "+(i+1)+" : ");
            array[i]=sc.nextInt();
        }
        int b=0,s=0;
        int mp=0;
        int min=array[0];
        for(int i=1;i<size;i++){
            if(array[i]<min){
                min=array[i];
                b=i+1;    
            }
            else if(array[i]-min>mp) {
                mp=array[i]- min;
                s=i+1; 
            }
        }
            System.out.println("The maximum profit is : "+mp);
            System.out.println("Stocks bought on day "+b+" and sold at day "+s);
            sc.close();
}
}