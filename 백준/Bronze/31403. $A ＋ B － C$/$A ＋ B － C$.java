import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] nums = new String[3];

        for(int i = 0; i < 3; i++) {
            nums[i] = br.readLine().trim();
        }

        System.out.println(Integer.parseInt(nums[0]) + Integer.parseInt(nums[1]) - Integer.parseInt(nums[2]));
        System.out.println(Integer.parseInt(nums[0] + nums[1]) - Integer.parseInt(nums[2]));
    }
}