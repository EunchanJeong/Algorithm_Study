import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int solution(int[] people, int limit) {
        
        Arrays.sort(people);
        
        int answer = 0;
        int total = 0;

        int left = 0;
        int right = people.length-1;
        
        while(left <= right) {
            if(people[left] + people[right] <= limit) {
                left++;
            }
            
            right--;
            answer++;
        }
        return answer;
    }
}