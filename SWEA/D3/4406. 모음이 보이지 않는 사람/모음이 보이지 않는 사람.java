import java.util.Scanner;

class Solution {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        char[] vowels = { 'a', 'e', 'i', 'o', 'u' };

        for (int test_case = 1; test_case <= T; test_case++) {
            String str = sc.next();
            StringBuilder sb = new StringBuilder();

            for (char c : str.toCharArray()) {
                boolean isVowel = false;
                for (char v : vowels) {
                    if (c == v) {
                        isVowel = true;
                        break;
                    }
                }
                if (!isVowel) {
                    sb.append(c);
                }
            }

            System.out.printf("#%d %s\n", test_case, sb.toString());
        }
    }
}