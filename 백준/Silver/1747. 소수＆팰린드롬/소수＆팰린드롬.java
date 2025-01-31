import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        while (true) {
            if (isPrime(N) && isPalindrome(N)) {
                System.out.println(N);
                break;
            }
            N++;
        }
    }

    private static boolean isPrime(int x) {
        if (x == 1) return false;
        if (x == 2) return true;
        if (x % 2 == 0) return false; 

        int sqrtX = (int) Math.sqrt(x);
        for (int i = 3; i <= sqrtX; i += 2) {
            if (x % i == 0) return false;
        }
        return true;
    }

    private static boolean isPalindrome(int x) {
        String str = String.valueOf(x);
        return str.equals(new StringBuilder(str).reverse().toString());
    }
}