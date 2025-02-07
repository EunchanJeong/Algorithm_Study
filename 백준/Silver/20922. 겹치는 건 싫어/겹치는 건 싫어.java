import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] nums = new int[N];

        st = new StringTokenizer(br.readLine());
        
        int maxNum = 0;
        for(int i = 0; i < nums.length; i++) {
            nums[i] = Integer.parseInt(st.nextToken());

            if(nums[i] > maxNum) {
                maxNum = nums[i];
            }
        }
        
        int left = 0;
        int right = 0;

        int[] counter = new int[maxNum + 1];
        int answer = 0;

        while(right < N) {
            if(counter[nums[right]] < K) {
                counter[nums[right]]++;
                right++;
            }
            else {
                counter[nums[left]]--;
                left++;
            }

            answer = Math.max(answer, right - left);
        }

        System.out.println(answer);
    }
}