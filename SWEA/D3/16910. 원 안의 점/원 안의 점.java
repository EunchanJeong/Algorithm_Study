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
            
			int N = sc.nextInt();
            int count = 0;
            
            for(int x = 0; x <= N; x++) {
            	for(int y = 0; y <= N; y++) {
                	if(((x*x) + (y*y)) <= (N*N)) {
                    	if(x == 0 && y == 0) {
                        	count++;
                        }
                        else if(x == 0 || y == 0) {
                        	count += 2;
                        }
                        else {
                        	count += 4;
                        }
                    }
                }
            }
            sb.append(count + "\n");
		}
        
        System.out.print(sb.toString());
	}
}