import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        LinkedList<int[]> nums = new LinkedList<>();

        for (int i = 1; i <= N; i++) {
            nums.add(new int[]{i, Integer.parseInt(st.nextToken())});
        }

        List<Integer> result = new ArrayList<>();

        while (!nums.isEmpty()) {
            int[] current = nums.pollFirst();

            int idx = current[0];
            int move = current[1];
            result.add(idx);

            if (nums.isEmpty()) {
                break;
            }

            if (move > 0) {
                move--;
            }

            Collections.rotate(nums, -move);
        }

        StringBuilder sb = new StringBuilder();
        for (int n : result) {
            sb.append(n).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}