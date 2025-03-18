import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        while(true) {
            String num = br.readLine().trim();

            if(num.equals("0")) {
                break;
            }
            
            String result = "yes";
            for(int i = 0; i < num.length()/2; i++) {
                if(num.charAt(i) != num.charAt(num.length() - i - 1)) {
                    result = "no";
                }
            }

            System.out.println(result);
        }
    }
}