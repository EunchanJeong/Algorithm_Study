import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        List<String> words = new ArrayList<>();
        int maxLen = 0;
        for(int i = 0; i < 5; i++) {
            String word = br.readLine().trim();
            words.add(word);

            if(word.length() > maxLen) {
                maxLen = word.length();
            }
        }

        String result = "";
        for(int i = 0; i < maxLen; i++) {
            for(int j = 0; j < 5; j++) {
                if(i < words.get(j).length()) {
                    result += words.get(j).charAt(i);
                }
            }
        }

        System.out.println(result);
    }
}