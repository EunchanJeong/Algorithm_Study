import java.util.*;
import java.io.*;

class Main {
    public static int[][] APT = new int[15][15];
 
	public static void main(String[] args) throws IOException {
 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = 0;
        boolean check = false;

        for(int i = 0; i < 3; i++) {
            String str = br.readLine();

            char c = str.charAt(0);

            if(c != 'F' && c != 'B') {
                num = Integer.parseInt(str);
                check = true;
            }

             if(check) {
                num++;
            }
            
        }

        if(num%3==0) {
            if(num%5==0) {
                System.out.println("FizzBuzz");
            }
            else {
                System.out.println("Fizz");
            }
        }
        else{
            if(num%5==0) {
                System.out.println("Buzz");
            }
            else {
                System.out.println(num);
            }
        }

        

    }
}