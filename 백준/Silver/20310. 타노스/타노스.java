import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine().trim();

        ArrayList<Character> S = new ArrayList<>();

        for(char c : input.toCharArray()) {
            S.add(c);
        }

        long zeroCount = S.stream().filter(c -> c == '0').count();
        long oneCount = S.stream().filter(c -> c == '1').count();

        int stopPoint = 0;
        for(int i = 0; i < S.size(); i++) {
            if(S.get(i) == '1') {
                S.remove(i);
                i--;
                stopPoint++;
            }

            if(stopPoint == oneCount/2) {
                break;
            }
        }


        stopPoint = 0;
        for(int i = S.size()-1; i >= 0; i--) {
            if(S.get(i) == '0') {
                S.remove(i);
                stopPoint++;
            }

            if(stopPoint == zeroCount/2) {
                break;
            }
        }

        StringBuilder result = new StringBuilder();

        for(char c : S) {
            result.append(c);
        }

        System.out.println(result.toString());
    }
}