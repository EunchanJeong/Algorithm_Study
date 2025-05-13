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
		
        Map<Character, Character> map = new HashMap<>();
        map.put('b', 'd');
        map.put('d', 'b');
        map.put('p', 'q');
        map.put('q', 'p');
        
        StringBuilder sb = new StringBuilder();
        
		for(int test_case = 1; test_case <= T; test_case++)
		{
            sb.append("#" + test_case + " ");
            
			char[] input = sc.next().toCharArray();
            
            for(int i = (input.length - 1); i >= 0; i--) {
            	sb.append(map.get(input[i]));
            }
            sb.append("\n");
		}
        System.out.print(sb.toString());
	}
}