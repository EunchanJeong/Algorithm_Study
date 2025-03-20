import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        StringTokenizer st;
        for(int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());

            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            String str = br.readLine();
            System.out.println(finder(N, M, str));
        }
    }
    static int finder(int n, int m, String str) {
        StringTokenizer st = new StringTokenizer(str);
        Queue<int[]> queue = new LinkedList<>();

        int order = 1;

        for(int i = 0; i < n; i++) {
            int[] arr = {i, Integer.parseInt(st.nextToken())};
            queue.add(arr);
        }

        while(true) {
            int[] peek = queue.peek();
            boolean pass = true;

            for(int[] arr : queue) {
                if(peek[1] < arr[1]) {
                    int[] tmp = queue.poll();
                    queue.add(tmp);

                    pass = false;
                    break;
                }
            }

            if(pass && peek[0] == m) {
                return order;
            }
            else if(pass && peek[0] != m) {
                queue.poll();
                order++;
            }
        }
        
    }
}