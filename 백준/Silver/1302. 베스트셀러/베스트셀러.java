import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        HashMap<String, Integer> words = new HashMap<>();
        
        for(int i = 0; i < N; i++){
            String word = br.readLine().trim();
            words.put(word, words.getOrDefault(word, 0) + 1);
        }
        
        int maxValue = 0;
        for(int value : words.values()) {
            maxValue = Math.max(maxValue, value);
        }
        
        ArrayList<String> S = new ArrayList<>();
        
        for (Map.Entry<String, Integer> e : words.entrySet()) {
            if(e.getValue() == maxValue) {
                S.add(e.getKey());
            }
        }
        Collections.sort(S);
        System.out.print(S.get(0));
    }
}