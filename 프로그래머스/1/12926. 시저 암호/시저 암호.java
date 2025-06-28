class Solution {
    public String solution(String s, int n) {
         StringBuilder answer = new StringBuilder();
        
        for (char c : s.toCharArray()) {
            if (c >= 'A' && c <= 'Z') {
                answer.append((char)((c - 'A' + n) % 26 + 'A'));
            } else if (c >= 'a' && c <= 'z') {
                answer.append((char)((c - 'a' + n) % 26 + 'a'));
            } else {
                answer.append(c);
            }
        }
        
        return answer.toString();
    }
}