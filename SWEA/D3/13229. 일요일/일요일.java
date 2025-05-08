import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;
class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		
        Map<String, Integer> map = new HashMap<>();
        map.put("SUN", 7);
        map.put("MON", 6);
        map.put("TUE", 5);
        map.put("WED", 4);
        map.put("THU", 3);
        map.put("FRI", 2);
        map.put("SAT", 1);
        
		for(int test_case = 1; test_case <= T; test_case++)
		{
			String day = sc.next();
            
            System.out.printf("#%d %d\n", test_case, map.get(day));
		}
	}
}