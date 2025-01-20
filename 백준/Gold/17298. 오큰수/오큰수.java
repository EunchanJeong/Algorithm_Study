import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException  {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] nums = new int[N];
        int[] result = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
            result[i] = -1;
        }

        Stack<Integer> stack = new Stack<>();
        stack.push(0);
        
        for(int i = 1; i < N; i++) {
            while(!stack.isEmpty() && nums[stack.peek()] < nums[i]) {
                result[stack.pop()] = nums[i];
            }
            stack.push(i);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(result[i]).append(" ");
        }

        System.out.println(sb.toString().trim());
    }
}