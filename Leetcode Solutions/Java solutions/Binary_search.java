public class Binary_search {
    public static void main(String[] args) {
        int arr[] = { 1, 2, 3, 4, 5, 6, 7, 8 };
        int target = 2;
        int l = 0;
        int check = 0;
        int u = arr.length - 1;

        while (l <= u) {
            int mid = (l + u) / 2;
            if (arr[mid] == target) {
                System.out.print("Item found!");
                check += 1;
                break;
            } else if (arr[mid] < target) {
                l = mid + 1;
            } else {
                u = mid - 1;
            }

        }
        if (check == 0) {
            System.out.print("Item not found!");
        }

    }

}
