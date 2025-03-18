import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] nums = new int[6];
        int count = 0;
        for(int i =0; i < 6; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
            count += nums[i];
        }

        st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        int result1 = 0;
        for(int i = 0; i < nums.length; i++) {
            for(int j = 0; j <= N; j++) {
                if(T*j >= nums[i]) {
                    result1 += j;
                    break;
                }
            }
        }

        System.out.println(result1);
        System.out.println(N/P + " " + N%P);
    }
}