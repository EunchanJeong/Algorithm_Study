class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        int numMax = 0;
        
        for(int a : arr) {
            if(numMax < a) {
                numMax = a;
            }
        }
        
        for(int i = numMax;; i++) {
            boolean check = true;
            
            for(int j = 0; j < arr.length; j++) {
                if(i%arr[j] != 0) {
                    check = false;
                    break;
                }
            }
            
            if(check) {
                return i;
            }
        }
    }
}