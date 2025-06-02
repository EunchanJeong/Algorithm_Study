import java.util.Deque;
import java.util.LinkedList;

class Solution {
    
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static int width;
    static int height;
    
    public int solution(String[] maps) {
        int answer = 0;
        width = maps[0].length();
        height = maps.length;
        
        char[][] map = new char[height][width];
        
        int sh = 0;
        int sw = 0;
        int lh = 0;
        int lw = 0;
        
        for(int i = 0; i < height; i++) {
            for(int j = 0; j < width; j++) {
                map[i][j] = maps[i].charAt(j);
                
                if(maps[i].charAt(j) == 'S') {
                    sh = i;
                    sw = j;
                }
                else if(maps[i].charAt(j) == 'L') {
                    lh = i;
                    lw = j;
                }
            }
        }
        
        int leverCount = bfs(map, height, width, sh, sw, 'L');
        
        if(leverCount == -1) {
            return -1;
        }
        
        int exitCount = bfs(map, height, width, lh, lw, 'E');
        
        if(exitCount == -1) {
            return -1;
        }
        
        answer = leverCount + exitCount;
        
        return answer;
    }
    
    public class Point {
        int x;
        int y;
        
        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    public int bfs(char[][] map, int height, int width, int x, int y, char destination) {
        Deque<Point> dq = new LinkedList<>();
        
        int[][] visited = new int[height][width];
        
        for(int i = 0; i < height; i++) {
            for(int j = 0; j < width; j++) {
                visited[i][j] = -1;
            }
        }
        
        visited[x][y] = 0;
        dq.add(new Point(x, y));
        
        while(!dq.isEmpty()) {
            Point point = dq.poll();
            
            x = point.x;
            y = point.y;
            
            for(int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if(nx >= 0 && nx < height && ny >= 0 && ny < width && visited[nx][ny] == -1) {
                    if(map[nx][ny] == destination) {
                        return visited[x][y] + 1;
                    }
                    
                    else if(map[nx][ny] != 'X') {
                        visited[nx][ny] = visited[x][y] + 1;
                        dq.add(new Point(nx, ny));
                    }
                }
            }
        }
        return -1;
        
    }
}