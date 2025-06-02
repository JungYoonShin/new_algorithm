import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCase = sc.nextInt();

        for (int i = 0; i < testCase; i++) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            Integer[] a = new Integer[n];
            Integer[] b = new Integer[m];

            for (int x = 0; x < n; x++) a[x] = sc.nextInt();
            for (int x = 0; x < m; x++) b[x] = sc.nextInt();
            Arrays.sort(b);

            int result = 0;
            for(int p=0; p<n; p++) {
                int start = 0;
                int index = 0;
                int end = m-1;
                int mid = (start+end) / 2;

                while(start<=end) {
                    mid = (start + end) / 2;
                    if(b[mid] < a[p]) {
                        index = mid+1;
                        start = mid + 1;
                    }
                    else {
                        end = mid - 1;
                    }
                }

                result += index;
            }

            System.out.println(result);
            
        }
        sc.close();
    }
}