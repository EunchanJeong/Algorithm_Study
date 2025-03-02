import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        StringTokenizer st;

        int[][] segments = new int[N][2];
        
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());

            segments[i][0] = n1;
            segments[i][1] = n2;
        }
        
        Arrays.sort(segments, (o1, o2) -> o1[0] == o2[0] ? o1[1] - o2[1] : o1[0] - o2[0]);

        int result = 0;
        int start = segments[0][0];
        int end = segments[0][1];

        for(int i = 1; i < N; i++) {
            int s = segments[i][0];
            int e = segments[i][1];

            if(s <= end) {
                end = Math.max(end, e);
            }
            else {
                result += (end - start);
                start = s;
                end = e;
            }
        }

        result += (end - start);

        System.out.println(result);
    }
}