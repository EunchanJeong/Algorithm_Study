class Solution {
    public long solution(int price, int money, int count) {
        long answer = -1;
        
        long n = 0;
        for(int i = 1; i <= count; i++) {
            n += price * i;
        }
        return n - money > 0 ? n - money : 0;
    }
}