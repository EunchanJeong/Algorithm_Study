import java.util.List;
import java.util.ArrayList;

class Solution {
    
    static int[] dx = {1, 1, 0};
    static int[] dy = {0, 1, 1};
    
    public int solution(int m, int n, String[] board) {
        int answer = 0;
        
        List<Index> indexes;
        
        char[][] map = new char[m][n];
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                map[i][j] = board[i].charAt(j);
            }
        }
        while(true) {
            indexes = search(map, m, n);
            
            if(indexes.size() == 0) {
                break;
            }
            
            answer += delete(map, indexes);
            move(map);
        }
        return answer;
    }
    
    public class Index {
        int x;
        int y;
        
        Index(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public ArrayList<Index> search(char[][] map, int m, int n) {
        
        ArrayList<Index> tmp = new ArrayList<>();
        for(int i = 0; i < m-1; i++) {
            for(int j = 0; j < n-1; j++) {
                if(map[i][j] == '0') {
                    continue;
                }
                
                boolean check = true;
                for(int d = 0; d < 3; d++) {
                    if(map[i][j] == map[i + dx[d]][j + dy[d]]) {
                        continue;
                    }
                    else {
                        check = false;
                    }
                }
                
                if(check) {
                    tmp.add(new Index(i, j));
                }
            }
        }

        return tmp;
    }
    
    public int delete(char[][] map, List<Index> indexes) {
        int count = 0;
        for(Index index : indexes) {
            int x = index.x;
            int y = index.y;
            
            if(map[x][y] != '0') {
                map[x][y] = '0';
                count++;
            }
            
            for(int d = 0; d < 3; d++) {
                if(map[x + dx[d]][y + dy[d]] != '0') {
                    map[x + dx[d]][y + dy[d]] = '0';
                    count++;
                }
            }
        }
        
        return count;
    }
    
    public void move(char[][] map) {
        for(int i = map.length-1; i > 0; i--) {
            for(int j = 0; j < map[0].length; j++) {
                if(map[i][j] == '0') {
                    int x = i;
                    int y = j;

                    while((x-1) >= 0) {
                        if(map[x-1][y] != '0') {
                            map[i][j] = map[x-1][y];
                            map[x-1][y] = '0';
                            break;
                        }
                        x--;
                    }
                }
            }
        }
        
        
    }
}