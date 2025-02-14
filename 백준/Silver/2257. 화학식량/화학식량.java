import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String chemical = br.readLine().trim();
        Stack<Integer> stack = new Stack<>();

        HashMap<Character, Integer> atom = new HashMap<>();
        atom.put('H', 1);
        atom.put('C', 12);
        atom.put('O', 16);
        
        for (char c : chemical.toCharArray()) {
            if (c == '(') {
                stack.push(-1);
            } else if (atom.containsKey(c)) {
                stack.push(atom.get(c));
            } else if (c == ')') {
                int temp = 0;
                while (!stack.isEmpty()) {
                    if (stack.peek() == -1) {
                        stack.pop();
                        break;
                    }
                    temp += stack.pop();
                }
                stack.push(temp);
            } else {
                int multiplier = c - '0';
                if (!stack.isEmpty()) {
                    stack.push(stack.pop() * multiplier);
                }
            }
        }
        
        int totalWeight = 0;
        while (!stack.isEmpty()) {
            totalWeight += stack.pop();
        }
        
        System.out.println(totalWeight);
    }
}
