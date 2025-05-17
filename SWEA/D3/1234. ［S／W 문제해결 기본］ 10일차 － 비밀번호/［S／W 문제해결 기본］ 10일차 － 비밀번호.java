import java.util.Scanner;
import java.util.Stack;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();

		int T = 10;

		for(int test_case = 1; test_case <= T; test_case++)
		{
			sb.append("#" + test_case + " ");
			
			int N = Integer.parseInt(sc.next());
			String password = sc.next();
            Stack<Character> stack = new Stack<>();
            
			for(int i = 0; i < password.length(); i++) {
				if(!stack.isEmpty() && stack.peek() == password.charAt(i)) {
					stack.pop();
				}
				else {
                    stack.push(password.charAt(i));
				}
			}

			for(char c : stack) {
				sb.append(c);
			}
			sb.append("\n");
		}
		System.out.print(sb.toString());
	}
}