import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long X = Long.parseLong(br.readLine());

        String result = "";
        for(long i = 0; i < (X/4); i++) {
            result += "long ";
        }
        result += "int";
        
        System.out.println(result);
    }
}