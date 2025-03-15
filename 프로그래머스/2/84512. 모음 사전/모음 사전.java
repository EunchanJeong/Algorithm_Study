class Solution {
    
    private static final char[] vowels = {'A', 'E', 'I', 'O', 'U'};
    private boolean check = false;
    private int count = 0;
    
    private void DFS(String current, String target) {
        if(current.equals(target)) {
            check = true;
            return;
        }
        
        if(current.length() >= 5) {
            return;
        }
        
        for(char v : vowels) {
            if(!check) {
                count++;
                DFS(current + v, target);
            }
        }
    }
    
    public int solution(String word) {
        DFS("", word);
        return count;
    }
}