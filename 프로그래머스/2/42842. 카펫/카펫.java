class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        int a = brown + yellow;
        
        int M = brown/4;
        
        for(int i = M; i <= brown/2; i++) {
            for(int j = i; j >= 1; j--) {
                if (i * j == a) {
                    if((i*2) + (j*2) - 4 == brown) {
                        answer[0] = i;
                        answer[1] = j;
                    }
                }
            }
        }
        return answer;
    }
}