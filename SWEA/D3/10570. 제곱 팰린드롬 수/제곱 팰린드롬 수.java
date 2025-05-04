import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
  	public static boolean isInteger(double num) {
    	return num % 1 == 0.0;
	}
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
	
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int start = sc.nextInt();
            int end = sc.nextInt();
            
            int count = 0;
            for(int i = start; i <= end; i++) {
                String str1 = String.valueOf(i);
            	String str2 = new StringBuilder(str1).reverse().toString();
                
                if(str1.equals(str2)) {
                	double q = Math.sqrt(i);
                    
                    if(isInteger(q)) {
                    	String sqrtInt = String.valueOf((int)q);
            			String reverse = new StringBuilder(sqrtInt).reverse().toString();
                        
                        if(sqrtInt.equals(reverse)) {
                        	count++;
                        }
                    }
                }
            }
			System.out.printf("#%d %d\n", test_case, count);
		}
	}
}