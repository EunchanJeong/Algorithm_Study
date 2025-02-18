import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        String[] board = new String[N];

        for(int i = 0; i < N; i++) {
            board[i] = br.readLine().trim();
        }

        int count = N  * M;
        
        for(int i = 0; i < N-7; i++) {
            for(int j = 0; j < M-7; j++) {
                int index1 = 0;
                int index2 = 0;
                for(int x = i; x < i+8; x++) {
                    for(int y = j; y < j+8; y++) {
                        if((x+y)%2 == 0) {
                            if(board[x].charAt(y) == 'W') {
                                index1++;
                            }
                            if(board[x].charAt(y) == 'B') {
                                index2++;
                            }
                        }
                        else {
                            if(board[x].charAt(y) == 'B') {
                                index1++;
                            }
                            if(board[x].charAt(y) == 'W') {
                                index2++;
                            }
                        }
                    }
                }
                int indexMin = Math.min(index1, index2);
                count = Math.min(count, indexMin);
            }
        }

        System.out.println(count);
    }
}