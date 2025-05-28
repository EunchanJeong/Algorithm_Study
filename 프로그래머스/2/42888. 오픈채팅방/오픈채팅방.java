import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public String[] solution(String[] record) {
        
        Map<String, String> userInfo = new HashMap<>();
        Map<String, String> actions = new HashMap<>();
        List<String> logs = new ArrayList<>();
        
        actions.put("Enter", "들어왔습니다.");
        actions.put("Leave", "나갔습니다.");
        
        for(String r : record) {
            
            String[] tmp = r.split(" ");
            String action = tmp[0];
            String userId = tmp[1];
            String nickname = "";
            
            if(tmp.length > 2) {
                nickname = tmp[2];
            }
            
            if(action.equals("Enter")) {
                logs.add(userId + " " + action);
                userInfo.put(userId, nickname);
            }
            else if(action.equals("Leave")) {
                logs.add(userId + " " + action);
            }
            else if(action.equals("Change")) {
                userInfo.replace(userId, nickname);
            }
        }
        String[] answer = new String[logs.size()];
    
        for(int i = 0; i < logs.size(); i++) {
            String[] tmp = logs.get(i).split(" ");
            String userId = tmp[0];
            String action = tmp[1];
            
            answer[i] = userInfo.get(userId) + "님이 " + actions.get(action);
        }
        return answer;
    }
}