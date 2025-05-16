import java.util.Scanner;

class Solution {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        
        int T = 10;
        
        for (int test_case = 1; test_case <= T; test_case++) {
            sb.append("#").append(test_case).append(" ");
            
            int N = sc.nextInt();
            int[][] board = new int[N][N];
            
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    board[i][j] = sc.nextInt();
                }
            }

            int count = 0;
            
            for (int col = 0; col < N; col++) {
                boolean flag = false;
                
                for (int row = 0; row < N; row++) {
                    if (board[row][col] == 1) {
                        flag = true;
                    } else if (flag && board[row][col] == 2) {
                        count++;
                        flag = false;
                    }
                }
            }

            sb.append(count).append("\n");
        }
        
        System.out.print(sb.toString());
    }
}