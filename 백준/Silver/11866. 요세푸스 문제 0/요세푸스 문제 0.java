import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        Queue<Integer> q = new LinkedList<>();
    
        for(int i = 1; i <= N; i++) {
            q.add(i);
        }

        int[] result = new int[N];
        int idx = 0;
        while(!q.isEmpty()) {
            for(int i = 0; i < K-1; i++) {
                q.add(q.poll());
            }
            result[idx] = q.poll();
            idx++;
        }

        StringBuilder sb = new StringBuilder();
        
        sb.append("<");
        for(int i = 0; i < result.length; i++) {
            sb.append(result[i]);

            if(i != result.length - 1) {
                sb.append(", ");
            }
        }
        sb.append(">");

        System.out.println(sb.toString());
        
    }
}