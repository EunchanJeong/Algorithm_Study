import java.util.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine().trim();
        boolean check = true;
        for(int i = 0; i < input.length()/2; i++) {
            if(input.charAt(i) == input.charAt(input.length()-i-1)) {
                continue;
            }
            else {
                check = false;
                break;
            }
        }

        if(check) {
            System.out.println(1);
        }
        else {
            System.out.println(0);
        }
    }
}