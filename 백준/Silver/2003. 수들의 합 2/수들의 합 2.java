import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException  {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] nums = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        
        int left = 0;
        int right = 0;
        int count = 0;
        int total = 0;

        while (right <= N && left <= right) {
            if (total == M) {
                count++;
                total -= nums[left];
                left++; 
            } else if(total < M) {
                if(right < N) {
                    total += nums[right];
                }
                right++; 
            } else { 
                total -= nums[left];
                left++;
            }
        }

        System.out.println(count);
    }
}