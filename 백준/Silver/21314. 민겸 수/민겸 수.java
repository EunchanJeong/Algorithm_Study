import java.io.*;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine().trim();

        StringBuilder max = new StringBuilder();
        StringBuilder min = new StringBuilder();

        int m = 0;

        for (char c : s.toCharArray()) {
            if (c == 'M') {
                m++;
            } else { 
                if (m > 0) {
                    BigInteger tenPowM = BigInteger.TEN.pow(m);
                    max.append(BigInteger.valueOf(5).multiply(tenPowM)); 
                    min.append(tenPowM.add(BigInteger.valueOf(5))); 
                } else {
                    max.append('5');
                    min.append('5');
                }
                m = 0;
            }
        }

        if (m > 0) {
            max.append("1".repeat(m));
            min.append(BigInteger.TEN.pow(m - 1));
        }

        System.out.println(max);
        System.out.println(min);
    }
}
