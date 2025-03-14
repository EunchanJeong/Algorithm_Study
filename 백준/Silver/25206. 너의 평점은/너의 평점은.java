import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        double num = 0;
        double score = 0;

        for (int i = 0; i < 20; i++) {
            String[] input = br.readLine().split(" ");
            double credit = Double.parseDouble(input[1]);
            String grade = input[2];

            if (grade.equals("P")) continue;

            if (grade.equals("A+")) score += credit * 4.5;
            else if (grade.equals("A0")) score += credit * 4.0;
            else if (grade.equals("B+")) score += credit * 3.5;
            else if (grade.equals("B0")) score += credit * 3.0;
            else if (grade.equals("C+")) score += credit * 2.5;
            else if (grade.equals("C0")) score += credit * 2.0;
            else if (grade.equals("D+")) score += credit * 1.5;
            else if (grade.equals("D0")) score += credit * 1.0;
            else if (grade.equals("F")) score += credit * 0.0;

            num += credit; // "P"가 아닌 경우에만 num 증가
        }

        if (num == 0) {
            System.out.printf("%.6f", 0.0);
        } else {
            System.out.printf("%.6f", score / num);
        }
    }
}