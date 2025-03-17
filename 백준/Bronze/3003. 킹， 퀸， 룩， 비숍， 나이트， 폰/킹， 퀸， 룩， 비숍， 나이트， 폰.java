import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] pieces = {1, 1, 2, 2, 2, 8};

        int[] inputs = new int[6];

        for(int i = 0; i < 6; i++) {
            inputs[i] = Integer.parseInt(st.nextToken());
        }

        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < 6; i++) {
            sb.append(pieces[i] - inputs[i]).append(" ");
        }

        System.out.println(sb.toString());
    }
}