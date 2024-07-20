public class Climbingstairs {
    public static void main(String[] args) {
        int n=5;
        int one=1,two=1;
        for(int i=0;i<n-1;i++){
            int temp=one;
            one=one+two;
            two=temp;
        }
        System.out.println(one);
        
    }
    
}
