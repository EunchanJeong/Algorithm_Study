import java.util.LinkedList;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        
        LinkedList<String> cache = new LinkedList<>();
        
        for(String city : cities) {
            city = city.toLowerCase();
            
            if(cacheSize > 0) {
                if(!cache.contains(city)) {
                    if(cache.size() == cacheSize) {
                        cache.removeFirst();
                    }
                    cache.add(city);
                    answer += 5;
                }
                else {
                    cache.remove(city);
                    cache.add(city);
                    answer += 1;
                }
            }
            else {
                answer += 5;
            }
        }
        return answer;
    }
}