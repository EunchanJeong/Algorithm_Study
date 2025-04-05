class Solution {
    public String solution(String s) {
        String[] arr = s.split(" ");
        
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        
        for(String c : arr) {
            int num = Integer.parseInt(c);
            
            if(num < min) {
                min = num;
            }
            if(num > max) {
                max = num;
            }
        }
        return min + " " + max;
    }
}