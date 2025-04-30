import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		/*
		   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
		*/

		for(int test_case = 1; test_case <= T; test_case++)
		{
		
			int a = sc.nextInt();
            int b = sc.nextInt();
            
            if(a >= 10 || b >= 10) {
            	System.out.printf("#%d %d", test_case, -1);
            }
            else {
                System.out.printf("#%d %d", test_case, a*b);
            }
            
            System.out.println();

		}
	}
}