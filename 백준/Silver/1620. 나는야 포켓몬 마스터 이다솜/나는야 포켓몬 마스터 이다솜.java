import java.util.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Map<String, Integer> map1 = new HashMap<>();
        Map<Integer, String> map2 = new HashMap<>();
        
        for(int i = 1; i <= N; i++) {
            String input = br.readLine();
            
            map1.put(input, i);
            map2.put(i, input);
        }

        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < M; i++) {
            String search = br.readLine();

            if(isNumeric(search)) {
                sb.append(map2.get(Integer.parseInt(search))).append("\n");
            }
            else {
                sb.append(map1.get(search)).append("\n");
            }
        }

        System.out.println(sb.toString());
        br.close();
    }

    static boolean isNumeric(String str) {
        return str.chars().allMatch(Character::isDigit);
    }
}