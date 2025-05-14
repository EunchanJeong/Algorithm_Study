import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		for(int test_case = 1; test_case <= 10; test_case++)
		{
			sb.append("#" + test_case + " ");
			
			int length = sc.nextInt();
			String[] nums = sc.next().split("\\+");
			
			int result = 0;
			for(String num : nums) {
				boolean isNumber = true;
				for(char c : num.toCharArray()) {
					if(!Character.isDigit(c)) {
						isNumber = false;
						break;
					}
				}
				
				if(isNumber) {
					result += Integer.parseInt(num);
				}
				else {
					break;
				}
			}
			sb.append(result).append("\n");
		}
		System.out.print(sb.toString());
	}
}