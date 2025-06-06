class Solution {
    public int[] solution(int n, int s) {
        
        if(n > s) {
            return new int[] {-1};
        }
        
        int[] answer = new int[n];
        
        for(int i = 0; i < n; i++) {
            answer[i] = s/n;
        }
        
        int r = s%n;
        
        for(int i = n-1; i >= 0; i--) {
            if(r == 0) {
                break;
            }
            
            answer[i] += 1;
            r--;
        }
        return answer;
    }
}