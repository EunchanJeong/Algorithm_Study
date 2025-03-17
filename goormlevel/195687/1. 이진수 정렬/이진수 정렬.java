import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		Integer[] nums = new Integer[N];
		st = new StringTokenizer(br.readLine());
		
		for(int i = 0; i < N; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(nums, new Comparator<Integer>() {
						@Override
						public int compare(Integer a, Integer b) {
								int countA = Integer.bitCount(a); 
								int countB = Integer.bitCount(b);
								
								if (countA != countB) {
										return countB - countA; 
								} else {
										return b - a; 
								}
						}
		});
		System.out.println(nums[K-1]);
	}
}