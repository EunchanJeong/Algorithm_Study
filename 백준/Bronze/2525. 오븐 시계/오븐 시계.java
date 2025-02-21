import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long hour = Long.parseLong(st.nextToken());
        long minute = Long.parseLong(st.nextToken());

        long input = Long.parseLong(br.readLine());

        minute += input;

        if(minute >= 60) {
            hour += minute/60;
            minute = minute%60;
        }
        hour %= 24;
    
        System.out.println(hour + " " + minute);
        
    }
}