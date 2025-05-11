import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        
        for (int t = 0; t < 10; t++) {
            int test_case = sc.nextInt();
            Queue<Integer> q = new LinkedList<>();
            
            for (int j = 0; j < 8; j++) { 
                q.offer(sc.nextInt());
            }
            
            int count = 1;
            while (true) {
                int front = q.poll();
                front -= count;
                
                if (front <= 0) {
                    q.offer(0);
                    break; 
                }
                
                q.offer(front);
                
                count++;
                if (count > 5) {
                    count = 1;
                }    
            }
            
            sb.append("#").append(test_case).append(" ");
            for (int num : q) {
                sb.append(num).append(" ");
            }
            sb.append("\n");
        }
       
        System.out.print(sb.toString());
    }
}