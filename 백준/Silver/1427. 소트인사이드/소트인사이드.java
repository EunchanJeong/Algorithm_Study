import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String N = br.readLine().trim();

        Character[] nums = new Character[N.length()];

        for(int i = 0; i < N.length(); i++) {
            nums[i] = N.charAt(i);
        }

        Arrays.sort(nums, Collections.reverseOrder());

        StringBuilder result = new StringBuilder();
        for(char n : nums) {
            result.append(n);
        }
        System.out.println(result);
    }
}