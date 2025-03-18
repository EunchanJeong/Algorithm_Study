import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        while(true) {
            String[] tmp = br.readLine().split(" ");

            int count = 0;
            int[] edges = new int[3];
            for(int i = 0; i < 3; i++) {
                edges[i] = Integer.parseInt(tmp[i]);

                if(edges[i] == 0) {
                    count++;
                }
            }
            
            if(count == 3) {
                break;
            }
            
            Arrays.sort(edges);

            if((edges[2] * edges[2]) == ((edges[0] * edges[0]) + (edges[1] * edges[1]))) {
                System.out.println("right");
            }
            else {
                System.out.println("wrong");
            }
            
        }
    }
}