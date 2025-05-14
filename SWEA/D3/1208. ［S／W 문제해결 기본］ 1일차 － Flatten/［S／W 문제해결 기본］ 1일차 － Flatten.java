import java.util.Scanner;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        for (int test_case = 1; test_case <= 10; test_case++)
        {
            sb.append("#" + test_case + " ");

            int dump = sc.nextInt();

            int[] boxes = new int[100];
            int max = 0;
            int min = Integer.MAX_VALUE;
            int indexMax = 0;
            int indexMin = 0;

            for (int i = 0; i < boxes.length; i++) 
            {
                boxes[i] = sc.nextInt();

                if (boxes[i] > max) 
                {
                    max = boxes[i];
                    indexMax = i;
                }
                if (boxes[i] < min) 
                {
                    min = boxes[i];
                    indexMin = i;
                }
            }

            while (dump != 0) 
            {
                if (max - min <= 1) 
                {
                    break;
                }

                boxes[indexMax]--;
                boxes[indexMin]++;

                max = 0;
                min = Integer.MAX_VALUE;

                for (int i = 0; i < boxes.length; i++) 
                {
                    if (boxes[i] > max) 
                    {
                        max = boxes[i];
                        indexMax = i;
                    }
                    if (boxes[i] < min) 
                    {
                        min = boxes[i];
                        indexMin = i;
                    }
                }

                dump--;
            }

            sb.append(max - min).append("\n");
        }

        System.out.print(sb.toString());
    }
}