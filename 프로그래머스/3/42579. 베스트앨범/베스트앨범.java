import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();
 
        Map<String, Integer> count = new HashMap<>();
        Map<String, Map<Integer, Integer>> music = new HashMap<>();
        
        for(int i = 0; i < plays.length; i++) {
            if(!count.containsKey(genres[i])) {
                Map<Integer, Integer> map = new HashMap<>();
                
                map.put(i, plays[i]);
                music.put(genres[i], map);
                count.put(genres[i], plays[i]);
            }
            else {
                music.get(genres[i]).put(i, plays[i]);
                count.put(genres[i], count.get(genres[i]) + plays[i]);
            }
        }
        
        List<String> keySet = new ArrayList(count.keySet());
        Collections.sort(keySet, (s1, s2) -> count.get(s2) - count.get(s1));
        
        for(String key : keySet) {
            Map<Integer, Integer> map = music.get(key);
            List<Integer> genre_key = new ArrayList(map.keySet());
            
            Collections.sort(genre_key, (s1, s2) -> map.get(s2) - map.get(s1));
            
            answer.add(genre_key.get(0));
            if(genre_key.size() > 1) {
                answer.add(genre_key.get(1));
            }
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}