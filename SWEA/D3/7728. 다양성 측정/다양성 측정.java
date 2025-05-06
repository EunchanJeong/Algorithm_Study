import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			Set<Character> set = new HashSet<>();
            
            String str = sc.next();
            
            for(char c : str.toCharArray()) {
            	set.add(c);
            }
            
            System.out.printf("#%d %d\n", test_case, set.size());
		}
	}
}