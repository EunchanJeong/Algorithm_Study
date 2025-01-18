import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args)  throws IOException  {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");

        int[] L = new int[N];
        for(int i = 0; i < N; i++) {
            L[i] = Integer.parseInt(input[i]);
        }

        Arrays.sort(L);

        int left = 0;
        int right = N-1;
        int minValue = Integer.MAX_VALUE;
        int resultLeft = L[left];
        int resultRight = L[right];

        while(left < right) {
            int value = L[left] + L[right];

            if(Math.abs(value) < minValue) {
                minValue = Math.abs(value);
                resultLeft = L[left];
                resultRight = L[right];
            }

            if(value < 0) {
                left++;
            }
            else if(value > 0) {
                right--;
            }
            else {
                break;
            }
        }

        System.out.println(resultLeft + " " + resultRight);
    }
}