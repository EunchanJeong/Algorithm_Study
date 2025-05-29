import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public String[] solution(String[] files) {
        Arrays.sort(files, new Comparator<String>() {
            @Override
            public int compare(String f1, String f2) {
                String head1 = f1.split("[0-9]")[0];
                String head2 = f2.split("[0-9]")[0];

                int result = head1.toLowerCase().compareTo(head2.toLowerCase());

                if(result == 0) {
                    result = convertNum(f1, head1) - convertNum(f2, head2);
                }

                return result;
            }
        });
        return files;
    }
    
    public int convertNum(String str, String head) {
        str = str.substring(head.length());
        
        String result = "";
        
        for(char c : str.toCharArray()) {
            if(Character.isDigit(c) && result.length() < 5) {
                result += c;
            }
            else {
                break;
            }
        }
        
        return Integer.valueOf(result);
    }
}