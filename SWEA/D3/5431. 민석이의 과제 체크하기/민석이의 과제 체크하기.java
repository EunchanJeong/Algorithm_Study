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
            int K = sc.nextInt();
            
            boolean[] students = new boolean[N];
            
            for(int i = 0; i < K; i++) {
            	int num = sc.nextInt() - 1;
                students[num] = true;
            }
            
            for(int i = 0; i < N; i++) {
            	if(!students[i]) {
                	sb.append((i+1) + " ");
                }
            }
            
            sb.append("\n");
		}
        
        System.out.print(sb.toString());
	}
}