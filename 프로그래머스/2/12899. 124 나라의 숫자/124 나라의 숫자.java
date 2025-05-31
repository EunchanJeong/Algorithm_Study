class Solution {
    public String solution(int n) {
        String answer = "";
        String[] nums = {"4", "1", "2"};
        
        while(n > 0) {
            int t = n % 3;
            n /= 3;
            
            if(t == 0) {
                n--;
            }
            answer = nums[t] + answer;
        }
        return answer;
    }
}