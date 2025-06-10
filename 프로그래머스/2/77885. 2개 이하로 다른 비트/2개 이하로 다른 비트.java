class Solution {
    public long[] solution(long[] numbers) {
        long[] answer = new long[numbers.length];
        
        for(int i = 0; i < numbers.length; i++) {
            long num = numbers[i];
            
            if(num%2 == 0) {
                answer[i] = num+1;
            }
            else {
                String n = Long.toBinaryString(num);
                
                if(n.contains("0")) {
                    int index = n.lastIndexOf("0");
                    n = n.substring(0, index) + "10" + n.substring(index + 2);
                }
                else {
                    n = "10" + n.substring(1);
                }
                answer[i] = Long.parseLong(n, 2);
            }
        }
        return answer;
    }
}