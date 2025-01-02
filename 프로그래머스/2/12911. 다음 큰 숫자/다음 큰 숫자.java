class Solution {
    public int solution(int n) {
        int answer = 0;
        
        int oneCount1 = 0;
        
        for(char c : Integer.toBinaryString(n).toCharArray()) {
            if(c == '1') {
                oneCount1++;
            }
        }
        
        int oneCount2 = 0;
        while(oneCount1 != oneCount2) {
            n++;
            oneCount2 = 0;
            
            for(char c : Integer.toBinaryString(n).toCharArray()) {
                if(c == '1') {
                    oneCount2++;
                }
            }
        }
        
        return n;
    }
}