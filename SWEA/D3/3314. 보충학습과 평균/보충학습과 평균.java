import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
        
        int T;
		T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T; test_case++)
		{	
            sb.append("#").append(test_case).append(" ");
            
            int score = 0;
            int sum = 0;
            
			for(int i = 0; i < 5; i++) {
            	score = sc.nextInt();
                
                if(score < 40) {
                	score = 40;
                }
      
                sum += score;
            }
            
            sb.append(sum/5).append("\n");
		}
        
        System.out.print(sb.toString());
	}
}