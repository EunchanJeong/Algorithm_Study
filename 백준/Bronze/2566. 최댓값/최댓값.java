import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int[][] nums = new int[9][9];
        int max = 0;
        int x = 0;
        int y = 0;

        StringTokenizer st;
        for(int i = 0; i < 9; i++) {
            st = new StringTokenizer(br.readLine());
            
            for(int j = 0; j < 9; j++) {
                int num = Integer.parseInt(st.nextToken());
                
                if(num >= max) {
                    max = num;
                    x = i + 1;
                    y = j + 1;
                }
            }
        }

        System.out.println(max);
        System.out.println(x + " " + y);
    }
}