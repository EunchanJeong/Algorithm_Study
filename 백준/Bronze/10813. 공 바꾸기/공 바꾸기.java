import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");

        int N = Integer.parseInt(inputs[0]);
        int M = Integer.parseInt(inputs[1]);

        int[] nums = new int[N];
        for(int i = 1; i <= N; i++) {
            nums[i-1] = i;
        }

        for(int i = 0; i < M; i++) {
            inputs = br.readLine().split(" ");
            int n1 = Integer.parseInt(inputs[0]);
            int n2 = Integer.parseInt(inputs[1]);

            int tmp = nums[n1-1];
            nums[n1-1] = nums[n2-1];
            nums[n2-1] = tmp;
        }

        for(int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] + " ");
        }
    }
}