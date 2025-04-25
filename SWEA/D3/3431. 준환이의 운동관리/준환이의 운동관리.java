import java.util.Scanner;
import java.io.FileInputStream;
import java.io.IOException;

class Solution
{
    public static void main(String args[]) throws IOException 
    {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
        {
            int l = sc.nextInt();
            int h = sc.nextInt();
            int x = sc.nextInt();
            
            int result = 0;
            
            if(x < l) {
                result = l - x;  
            } 
            else if(x > h) 
            {
                result = -1; 
            } else 
            {
                result = 0;     
            }
            
            System.out.printf("#%d %d\n", test_case, result);
        }
    }
}