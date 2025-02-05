import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int[] arr = new int[N];
        int[] answer = new int[N];
        for(int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            answer[i] = 0;
        }

        for(int i = 0; i < N; i++) {
            int count = 0;

            for(int j = 0; j < N; j++) {
                if(count == arr[i] && answer[j] == 0) {
                    answer[j] = i + 1;
                    break;
                }
                else if(answer[j] == 0) {
                    count++;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        
        for(int i = 0; i < N; i++) {
            sb.append(answer[i]).append(" ");
        }

        System.out.println(sb.toString());
    }
}