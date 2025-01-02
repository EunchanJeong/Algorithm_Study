class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        
        while(!s.equals("1")) {
            answer[0]++;
            int zeroCount = 0;
            
            StringBuilder x = new StringBuilder();
            for(char c : s.toCharArray()) {
                if(c == '1') {
                    x.append("1");
                }
                else {
                    zeroCount++;
                }
            }
            
            answer[1] += zeroCount;
            s = Integer.toBinaryString(x.length());
        }
        
        return answer;
    }
}