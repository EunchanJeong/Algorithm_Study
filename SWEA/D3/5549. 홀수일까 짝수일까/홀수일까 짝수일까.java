import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
        
        StringBuilder sb = new StringBuilder();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			sb.append("#" + test_case + " ");
            
            String input = sc.next();
            int num = input.charAt(input.length() - 1) - '0';
            
            sb.append((num % 2 == 0) ? "Even" : "Odd").append("\n");
		}
        System.out.print(sb.toString());
	}
}