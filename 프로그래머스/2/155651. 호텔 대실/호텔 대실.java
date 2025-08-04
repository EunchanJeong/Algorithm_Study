import java.util.*;

class Solution {
    public int solution(String[][] book_time) {
        Arrays.sort(book_time, (a, b) -> a[0].compareTo(b[0]));
        PriorityQueue<Integer> pq = new PriorityQueue<>(); 
        
        for (String[] book : book_time) {
            String[] startArr = book[0].split(":");
            String[] endArr = book[1].split(":");

            int start = Integer.parseInt(startArr[0]) * 60 + Integer.parseInt(startArr[1]);
            int end = Integer.parseInt(endArr[0]) * 60 + Integer.parseInt(endArr[1]) + 10;

           
            if (!pq.isEmpty() && pq.peek() <= start) {
                pq.poll(); 
            }

            pq.offer(end); 
        }

        return pq.size(); 
    }
}