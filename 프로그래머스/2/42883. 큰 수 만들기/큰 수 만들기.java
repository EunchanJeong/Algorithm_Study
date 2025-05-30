class Solution {
    public String solution(String number, int k) {
        
        StringBuilder sb = new StringBuilder();
        
        int len = number.length();
        
        int remain = len - k; 
        
        for (int i = 0; i < len; i++) {
            char c = number.charAt(i);
            
            while (k > 0 && sb.length() > 0 && sb.charAt(sb.length() - 1) < c) {
                sb.deleteCharAt(sb.length() - 1);
                k--;
            }
            sb.append(c);
        }

        return sb.substring(0, remain);
    }
}