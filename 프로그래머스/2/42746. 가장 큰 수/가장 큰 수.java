import java.util.Arrays;

class Solution {
    public String solution(int[] numbers) {
        String[] str = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            str[i] = String.valueOf(numbers[i]);
        }

        Arrays.sort(str, (s1, s2) -> (s2 + s1).compareTo(s1 + s2));

        if (str[0].equals("0")) {
            return "0";
        }

        StringBuilder answer = new StringBuilder();
        for (String s : str) {
            answer.append(s);
        }

        return answer.toString();
    }
}