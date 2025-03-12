import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] nums = new int[N];

        String[] tmp = br.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(tmp[i]);
        }

        int v = Integer.parseInt(br.readLine());


        int cnt = 0;
        for (int num : nums) {
            if (num == v) {
                cnt++;
            }
        }

        System.out.println(cnt);
    }
}