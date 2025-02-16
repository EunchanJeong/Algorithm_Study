import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int h = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());

        int[] block = new int[w];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < w; i++) {
            block[i] = Integer.parseInt(st.nextToken());
        }

        int answer = 0;

        for (int i = 1; i < w - 1; i++) {
            int leftMax = 0, rightMax = 0;

            for (int j = 0; j < i; j++) {
                leftMax = Math.max(leftMax, block[j]);
            }

            for (int j = i + 1; j < w; j++) {
                rightMax = Math.max(rightMax, block[j]);
            }

            int minHeight = Math.min(leftMax, rightMax);
            if (minHeight > block[i]) {
                answer += minHeight - block[i];
            }
        }

        System.out.println(answer);
    }
}