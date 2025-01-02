class Solution {
    public int solution(int n) {
        int answer = 0;
        int start = 1;
        
        while(start <= n) {
            int tmp = 0;
            for(int i = start; i <= n; i++) {
                tmp += i;

                if(tmp == n) {
                    answer++;
                    break;
                }
                else if(tmp < n) {
                    continue;
                }
                else if(tmp > n) {
                    break;
                }
            }
            start += 1;
        }
        
        return answer;
    }
}