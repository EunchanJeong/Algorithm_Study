import java.util.Arrays;

class Solution {
    public String solution(String s) {
    
        String[] strArray = s.split(" ");
        
        int[] intArray = Arrays.stream(strArray)
                                .mapToInt(Integer::parseInt)
                                .toArray();
        
        Arrays.sort(intArray);
        
        return intArray[0] + " " + intArray[intArray.length - 1];
    }
}