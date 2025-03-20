import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        double[] scores = new double[N];
        for(int i = 0; i < N; i++) {
            scores[i] = Double.parseDouble(br.readLine());;
        }

        int t = (int)Math.round((double) N * 0.15);

        Arrays.sort(scores);
        
        double sum = 0;
        for(int i = t; i < N-t; i++) {
            sum += scores[i];
        }

        System.out.println(Math.round(sum/(N-(t*2))));
    }
}