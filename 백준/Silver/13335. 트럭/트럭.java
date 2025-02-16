import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        
        Queue<Integer> trucks = new LinkedList<>(); 
        
        for(int i = 0; i < n; i++) {
            trucks.add(Integer.parseInt(st.nextToken()));
        }

        Queue<Integer> bridge =new LinkedList<>(); 
        for(int i = 0; i < w; i++) {
            bridge.add(0);
        }

        int time = 0;
        int bridgeWeight = 0;
        
        while(!bridge.isEmpty()) {
            time++;

            bridgeWeight -= bridge.poll();

            if(!trucks.isEmpty()) {
                if(bridgeWeight + trucks.peek() <= L) {
                    int truck = trucks.poll();
                    bridge.add(truck);

                    bridgeWeight += truck;
                } 
                else {
                     bridge.add(0);
                }
            }
        }

        System.out.println(time);
    }
}