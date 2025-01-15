import java.util.*;
import java.io.*;


class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String S = br.readLine().trim();
        
        int count = 0;

        for(int i = 0; i < S.length()-1; i++) {
            if(S.charAt(i) != S.charAt(i+1)) {
                count++;
            }
        }

        System.out.println((count+1)/2);
    }
}