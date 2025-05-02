import java.util.Scanner;

class Solution {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            String input = sc.next();
            int len = input.length();
            StringBuilder sb = new StringBuilder();

            int idx = 0;
            boolean isCheck = false;

            for (int i = 0; i < len; i++) {
                if (input.charAt(i) == '1') {
                    idx = i;
                    isCheck = true;
                    break;
                }
            }

            if (isCheck) {
                for (int i = 0; i < len; i++) {
                    if (i < idx) sb.append('0');
                    else sb.append('1');
                }

                int count = 1;

                while (idx + 1 < len) {
                    idx++;

                    if (sb.charAt(idx) == input.charAt(idx)) continue;

                    char target = input.charAt(idx);
                    for (int i = idx; i < len; i++) {
                        sb.setCharAt(i, target);
                    }

                    count++;
                }

                System.out.printf("#%d %d\n", test_case, count); 
            } else {
                System.out.printf("#%d 0\n", test_case);
            }
        }
    }
}