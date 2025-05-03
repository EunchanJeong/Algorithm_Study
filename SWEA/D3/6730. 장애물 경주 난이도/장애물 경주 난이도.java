import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int N = sc.nextInt();
            
            int up = 0;
            int down = 0;
         	
            int num = sc.nextInt();
     
            int input;
            int cal;
            for(int i = 0; i < N-1; i++) {
            	input = sc.nextInt();
                
                cal = num - input;
                if(cal > 0 && down < cal) {
                    down = cal;
                }
                else if(cal < 0 && up < -cal){
                    up = -cal;
                }
                
                num = input;
            }
            
            if(down == Integer.MAX_VALUE) down = 0;
                
        	System.out.printf("#%d %d %d\n", test_case, up, down);
		}
	}
}