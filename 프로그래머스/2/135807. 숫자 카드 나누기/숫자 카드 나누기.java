import java.util.Arrays;

class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        Arrays.sort(arrayA);
        Arrays.sort(arrayB);
        
        int gcdA = arrayA[0];
        for (int i = 1; i < arrayA.length; i++) {
            gcdA = gcd(gcdA, arrayA[i]);
        }
        
        int gcdB = arrayB[0];
        for (int i = 1; i < arrayB.length; i++) {
            gcdB = gcd(gcdB, arrayB[i]);
        }
        
        boolean validA = true;
        for (int t : arrayB) {
            if (t % gcdA == 0) {
                validA = false;
                break;
            }
        }
        
        boolean validB = true;
        for (int t : arrayA) {
            if (t % gcdB == 0) {
                validB = false;
                break;
            }
        }
        
        int answer = 0;
        if (validA) answer = gcdA;
        if (validB) answer = Math.max(answer, gcdB);
        
        return answer;
    }
    
    public static int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }
}
