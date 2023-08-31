import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int count = 0;
		
		int a = sc.nextInt();
		
		if(a == 4 || a == 7)
		{
			System.out.println("-1");
		}
		else
		{
			if(a%5 == 0)
			{
				count = a/5;
			}
			else if(a%5 == 1)
			{
				count = ((a-(3*2))/5) + 2;
			}
			else if(a%5 == 2)
			{
					count = ((a-(3*4))/5) + 4;
			}
			else if(a%5 == 3)
			{
				count = (a-3*1)/5 + 1;
			}
			else if(a%5 == 4)
			{
				count = ((a-3*3)/5) + 3;
			}
			System.out.println(count);
		}
	}

}
