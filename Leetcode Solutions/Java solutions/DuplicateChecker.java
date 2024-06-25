import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class DuplicateChecker {

    // Method to check for duplicates in an array
    public static boolean containDuplicate(int[] array) {
        Set<Integer> seen = new HashSet<>();
        for (int element : array) {
            if (seen.contains(element)) {
                return true;
            }
            seen.add(element);
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the size of the array
        System.out.print("Enter the size of the array: ");
        int size = scanner.nextInt();

        // Initialize the array and read its elements
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            System.out.print("Enter the " + (i + 1) + " element: ");
            array[i] = scanner.nextInt();
        }

        // Check for duplicates and print the result
        boolean hasDuplicate = containDuplicate(array);
        System.out.println(hasDuplicate);

        scanner.close();
    }
}
