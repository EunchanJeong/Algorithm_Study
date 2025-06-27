class Solution {
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        
        answer[0] = gdc(n, m);
        answer[1] = lcm(n, m);
        
        return answer;
    }
    
    int gdc(int a, int b) { 
		if(a < b) 
		{
			int temp = a;
			a = b;
			b = temp;
		}
		while(b != 0) { 
            int r = a % b;
			a = b;
			b = r;
		}
		return a;
	}
	
	int lcm(int a, int b) { 
		return (a * b) / gdc(a,b);
	}
}