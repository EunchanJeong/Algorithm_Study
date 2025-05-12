import java.util.Scanner;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        StringBuilder sb = new StringBuilder();
        
        
        for (int test_case = 1; test_case <= T; test_case++)
        {
            sb.append("#" + test_case + " ");
            
            for (int i = 0; i < 3; i++) {
                String input = sc.next();
                sb.append(Character.toUpperCase(input.charAt(0)));
            }
            sb.append("\n");
        }
        
        System.out.print(sb.toString());
    }
}