import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();

        while (T-- > 0) {
            String S = br.readLine().replace(" ", ""); 
            int[] count_s = new int[26]; 

            for (char c : S.toCharArray()) {
                count_s[c - 'a']++;
            }

            int maxFreq = 0;
            char mostFrequentChar = '?';
            boolean multipleMax = false;

            for (int i = 0; i < 26; i++) {
                if (count_s[i] > maxFreq) {
                    maxFreq = count_s[i];
                    mostFrequentChar = (char) (i + 'a');
                    multipleMax = false; 
                } else if (count_s[i] == maxFreq && maxFreq > 0) {
                    multipleMax = true; 
                }
            }

            sb.append(multipleMax ? "?\n" : mostFrequentChar + "\n");
        }

        System.out.print(sb);
    }
}
