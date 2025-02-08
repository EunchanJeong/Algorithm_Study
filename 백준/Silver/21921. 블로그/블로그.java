import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        int[] nums = new int[N];
        for(int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int right = 0;
        int left = 0;
        int visitMax = 0;
        int count = 0;
        int visit = nums[0];
        
        while(right < N && left < N) {
            if(right - left + 1 == X) {
                if(visitMax == visit) {
                    count++;
                } 
                else if(visitMax < visit) {
                    visitMax = visit;
                    count = 1;
                }

                visit -= nums[left];
                left++;
            }
            else {
                right++;

                if(right < N) {
                    visit += nums[right];
                }
            }
        }

        if(visitMax == 0) {
            System.out.println("SAD");
        }
        else {
            System.out.println(visitMax);
            System.out.println(count);
        }
    }
}