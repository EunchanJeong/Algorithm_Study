import java.util.Scanner;

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
            
            int max = 0;
            int min = Integer.MAX_VALUE;
          	char[] input;
            for(int i = 0; i < 10; i++) {
            	input = sc.next().toCharArray();
                
                int sum = 0;
                for(char c : input) {
                	int tmp = c - '0';
                    sum += tmp;
                }
                
                if(max < sum) {
                	max = sum;
                }
                if(min > sum) {
                	min = sum;
                }
            }
            sb.append(max + " " + min + "\n");
		}
        
        System.out.print(sb.toString());
	}
}