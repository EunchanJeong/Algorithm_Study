import java.util.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Map<String, String> map = new HashMap<>();
        
        
        for(int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            
            map.put(st.nextToken(), st.nextToken());
        }

        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < M; i++) {
            String search = br.readLine();
            sb.append(map.get(search)).append("\n");
          
        }

        System.out.println(sb.toString());
        br.close();
    }
}