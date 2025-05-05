import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);

		for(int i = 1; i <= 10; i++)
		{
            int test_case = sc.nextInt();
			int num1 = sc.nextInt();
            int num2 = sc.nextInt();
            
            int result = func(1, num1, num2);
            
           System.out.printf("#%d %d\n", test_case, result);

		}
	}
    
    public static int func(int n1, int n2, int n3) {
    	if(n3 == 0) {
        	return n1;
        }
        
        return func(n1 * n2, n2, n3-1);
    }
}