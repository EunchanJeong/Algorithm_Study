import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer strtk = new StringTokenizer(br.readLine()," ");
		
		int basket = Integer.parseInt(strtk.nextToken());
		int count = Integer.parseInt(strtk.nextToken()); 
		
		int n1, n2, ball = 0;
		
		int array1[] = new int[basket];
		
		for(int i=0;i<count;i++) {
			strtk = new StringTokenizer(br.readLine()," ");
			
			n1 = Integer.parseInt(strtk.nextToken())-1;
			n2 = Integer.parseInt(strtk.nextToken())-1;
			ball = Integer.parseInt(strtk.nextToken());
			
			for(int j=n1;j<=n2;j++) {
				array1[j] = ball;
			}
		}
		
		
		for(int i=0;i<array1.length;i++) {
			System.out.print(array1[i]+" ");
		}
		
	}
}