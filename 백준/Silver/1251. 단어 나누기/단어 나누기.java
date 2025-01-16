import java.util.*;
import java.io.*;


class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String word = br.readLine().trim();
        ArrayList<String> words = new ArrayList<>();

        for(int i = 1; i < word.length()-1; i++) {
            for(int j = i + 1; j < word.length(); j++) {
                String part1 = new StringBuilder(word.substring(0, i)).reverse().toString();
                String part2 = new StringBuilder(word.substring(i, j)).reverse().toString();
                String part3 = new StringBuilder(word.substring(j)).reverse().toString();
                words.add(part1 + part2 + part3);
            }
         }

        Collections.sort(words);
        System.out.println(words.get(0));
    }
}