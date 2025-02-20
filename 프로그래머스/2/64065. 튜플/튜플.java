import java.util.*;

class Solution {
    public int[] solution(String s) {
        s = s.substring(2, s.length() - 2);
        String[] sets = s.split("\\},\\{");

        Arrays.sort(sets, Comparator.comparingInt(String::length)); 
        
        Set<Integer> seen = new HashSet<>();
        List<Integer> answer = new ArrayList<>();

        for (String set : sets) {
            String[] elements = set.split(",");
            for (String elem : elements) {
                int num = Integer.parseInt(elem);
                if (!seen.contains(num)) {
                    seen.add(num);
                    answer.add(num);
                }
            }
        }

        // 리스트를 배열로 변환
        return answer.stream().mapToInt(i -> i).toArray();
    }
}