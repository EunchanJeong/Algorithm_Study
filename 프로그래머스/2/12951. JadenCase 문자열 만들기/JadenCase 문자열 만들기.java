class Solution {
    public String solution(String s) {
        StringBuilder tmp = new StringBuilder();
        StringBuilder result = new StringBuilder();
        boolean isNewWord = true;
        
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
        
            if(c == ' ') {
                result.append(tmp);
                result.append(c);
                tmp.setLength(0);
                isNewWord = true;
            }
            else {
                if(isNewWord) {
                    tmp.append(Character.toUpperCase(c));
                    isNewWord = false;
                }
                else {
                    tmp.append(Character.toLowerCase(c));
                }
            }
        }
        
        result.append(tmp);
        return result.toString();
    }
}