import java.util.Scanner;

public class Kth_largest_element {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size of the array : ");
        int size = sc.nextInt();
        int[] array=new int[size];
        System.out.println("Enter the elements in the array :");
        for(int i=0;i<size;i++){
            array[i]=sc.nextInt();
        }
        System.out.print("Enter the value of K :");
        int k=sc.nextInt();
        k=size-k;//to print the kth smallest element just need the value ok k
        int result = quickselect(array,k,0,size-1);
        System.out.println("the kth largest element is : "+result);
        sc.close();
    }
    public static int quickselect(int arr[], int k, int l, int r) {
        if (l == r) {
            return arr[l];
        }

        int pivotIndex = partition(arr, l, r);

        if (k == pivotIndex) {
            return arr[k];
        } else if (k < pivotIndex) {
            return quickselect(arr, k, l, pivotIndex - 1);
        } else {
            return quickselect(arr, k, pivotIndex + 1, r);
        }
    }

    public static int partition(int[] arr, int l, int r) {
        int pivot = arr[r];
        int p = l;
        for (int i = l; i < r; i++) {
            if (arr[i] <= pivot) {
                int temp = arr[i];
                arr[i] = arr[p];
                arr[p] = temp;
                p++;
            }
        }
        int temp = arr[p];
        arr[p] = arr[r];
        arr[r] = temp;
        return p;
    }
}