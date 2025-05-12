import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
        
		for(int i = 1; i <= 10; i++)
		{
			int test_case = sc.nextInt();
            sb.append("#" + test_case + " ");
            
            String search = sc.next();
            String str = sc.next();
            
            int count = (str.length() - str.replace(search, "").length()) / search.length();
            
            sb.append(count + "\n");
		}
        
        System.out.print(sb.toString());
	}
}