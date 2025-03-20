import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] nums = new int[N];
        int sum = 0;
        
        for(int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(br.readLine());
            sum += nums[i];
        }

        Arrays.sort(nums);

        System.out.println((int)Math.round((double)sum/N));

        System.out.println(nums[N/2]); 

        System.out.println(findFreq(nums));
        
        System.out.println(Math.abs(nums[N-1] - nums[0]));
    }

    static int findFreq(int[] arr) {
         Map<Integer, Integer> map = new HashMap<>();

        if(arr.length == 1) {
            return arr[0];
        }
        else {
            for(int i = 0; i < arr.length; i++) {
                if(map.containsKey(arr[i])) {
                    map.put(arr[i], map.get(arr[i]) + 1);
                }
                else {
                    map.put(arr[i], 1);
                }
            }

            int max = Collections.max(map.values());

            List<Integer> list = new ArrayList<>();

            for(Map.Entry<Integer, Integer> tmp : map.entrySet()) {
                if(tmp.getValue() == max) {
                    list.add(tmp.getKey());
                }
            }

            Collections.sort(list);

            if(list.size() > 1) {
                return list.get(1);
            }
            else {
                return list.get(0);
            }
        }
    }
}