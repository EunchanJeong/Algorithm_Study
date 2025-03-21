import java.util.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        HashSet<Integer> set = new HashSet<>();
        StringBuilder sb = new StringBuilder();
        
        StringTokenizer st;
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            String command = st.nextToken();

            if(command.equals("all")) {
                set.clear();
                for(int j = 1; j <= 20; j++) {
                    set.add(j);
                }
            }
            else if(command.equals("empty")) {
                set.clear();
            }
            else {
                int num = Integer.parseInt(st.nextToken());

                if(command.equals("add")) {
                    set.add(num);
                }
                else if(command.equals("remove")) {
                    set.remove(num);
                }
                else if(command.equals("check")) {
                    if(set.contains(num)) {
                        sb.append("1").append("\n");
                    }
                    else {
                        sb.append("0").append("\n");
                    }
                }
                else if(command.equals("toggle")) {
                    if(set.contains(num)) {
                        set.remove(num);
                    }
                    else {
                        set.add(num);
                    }
                }
            }
        }
        System.out.println(sb.toString());
        br.close();
    }
}