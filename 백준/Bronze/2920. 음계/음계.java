import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] nums = new int[8];
        for(int i = 0; i < 8; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        String output = "";

        for(int i = 0; i < 7; i++) {
            if(nums[i] == nums[i+1] - 1) {
                output = "ascending";
            }
            else if (nums[i] == nums[i+1] + 1) {
                output = "descending";
            }
            else {
				output = "mixed";
				break;
			}
        }
        System.out.println(output);
    }
}