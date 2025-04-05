import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        
        for(int i = 0; i < sizes.length; i++) {
            if(sizes[i][0] < sizes[i][1]) {
                int tmp = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = tmp;
            }
        }
        
        int rMax = 0;
        int cMax = 0;
        
        for(int[] size : sizes) {
            if(size[0] > rMax) {
                rMax = size[0];
            }
            if(size[1] > cMax) {
                cMax = size[1];
            }
        }
            
        return rMax * cMax;
    }
}