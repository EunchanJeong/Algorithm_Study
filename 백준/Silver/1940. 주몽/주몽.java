import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        int[] nums = new int[N];
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken()); 
        }

        Arrays.sort(nums);

        int left = 0;
        int right = N - 1;
        int count = 0;
        while(left < right) {
            int sumNum = nums[left] + nums[right];

            if(sumNum < M) {
                left++;
            }
            else if(sumNum > M) {
                right--;
            }
            else {
                count++;
                left++;
                right--;
            }
        }

        System.out.println(count);
    }
}