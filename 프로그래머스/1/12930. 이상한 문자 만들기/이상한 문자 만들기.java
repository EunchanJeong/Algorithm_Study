class Solution {
    public String solution(String s) {
        String[] words = s.split(" ", -1);
        
        StringBuilder answer = new StringBuilder();
        
        for(String w : words) {
            for(int i = 0; i < w.length(); i++) {
                if(i % 2 == 0) {
                    answer.append(Character.toUpperCase(w.charAt(i)));
                }
                else {
                    answer.append(Character.toLowerCase(w.charAt(i)));
                }
            }
            answer.append(" ");
        }
        
        if(answer.length() > 0) {
            answer.setLength(answer.length() - 1);
        }
        
        return answer.toString();
    }
}