import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        
        Arrays.sort(numbers);
        
        int count = 0;
        
        int index = 0;
        while(index < numbers.length) {
            if(numbers[index] == count) {
                count++;
                index++;
                continue;
            }
            
            answer += count;
            count++;
        }
        
        while(count < 10) {
            answer += count;
            count++;
        }
        return answer;
    }
}