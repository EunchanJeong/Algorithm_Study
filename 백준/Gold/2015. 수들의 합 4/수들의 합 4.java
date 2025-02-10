import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] inputData = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            inputData[i] = Integer.parseInt(st.nextToken());
        }

        Map<Long, Integer> sumDict = new HashMap<>();
        sumDict.put(0L, 1);

        long sumNum = 0;
        long answer = 0;

        for (int num : inputData) {
            sumNum += num;

            if (sumDict.containsKey(sumNum - k)) {
                answer += sumDict.get(sumNum - k);
            }

            sumDict.put(sumNum, sumDict.getOrDefault(sumNum, 0) + 1);
        }

        System.out.println(answer);
    }
}
