import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();
        
        StringBuilder sb = new StringBuilder();
        
        for (int test_case = 1; test_case <= T; test_case++)
        {
            sb.append("#" + test_case + " ");
            
            Map<Integer, Integer> map = new HashMap<>();
            
            int[] nums = new int[3];
            for (int i = 0; i < 3; i++) {
                nums[i] = sc.nextInt();
            }
            
            for (int num : nums) {
                map.put(num, map.getOrDefault(num, 0) + 1);
            }
            
            for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
                if (entry.getValue() == 1) {
                    sb.append(entry.getKey()).append("\n");
                    break;
                }
                if (entry.getValue() == 3) {
                    sb.append(entry.getKey()).append("\n");
                    break;
                }
            }
        }
        System.out.print(sb.toString());
    }
}