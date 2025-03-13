import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] students = new int[31];

        for(int i = 0; i < 28; i++) {
            int num = Integer.parseInt(br.readLine());
            students[num] = 1;
        }

        for(int i = 1; i < students.length; i++) {
            if(students[i] != 1) {
                System.out.println(i);
            }
        }
    }
}