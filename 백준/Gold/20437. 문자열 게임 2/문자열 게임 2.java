import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        
        while(T-- > 0) {
            String W = br.readLine().trim();
            int K = Integer.parseInt(br.readLine());

            Map<Character, List<Integer>> charIdx = new HashMap<>();

            for(int i = 0; i < W.length(); i++) {
                char c = W.charAt(i);

                charIdx.putIfAbsent(c, new ArrayList<>());
                charIdx.get(c).add(i);
            }

            int minLen = Integer.MAX_VALUE;
            int maxLen = -1;

            for(List<Integer> idxList : charIdx.values()) {
                if(idxList.size() < K) {
                    continue;
                }

                for(int i = 0; i <= idxList.size() - K; i++) {
                    int length = idxList.get(i + K - 1) - idxList.get(i) + 1;

                    minLen = Math.min(minLen, length);
                    maxLen = Math.max(maxLen, length);
                }
            }

            if(minLen == Integer.MAX_VALUE) {
                sb.append("-1\n");
            }
            else {
                sb.append(minLen).append(" ").append(maxLen).append("\n");
            }
        }
        System.out.println(sb.toString());
    }
}
