import java.util.*;

class Solution {
    private static List<String> allRoutes = new ArrayList<>();
    private static int N;
    private static boolean[] visited;
    
    public String[] solution(String[][] tickets) {        
        N = tickets.length;
        visited = new boolean[N];
        dfs("ICN", "ICN", tickets);
        
        String[] answer = new String[N + 1];
        
        Collections.sort(allRoutes);
        String temp = allRoutes.get(0);
        
        for (int i = 0; i < N + 1; i++) {
            answer[i] = temp.substring(i * 3, i * 3 + 3);
        }
        
        return answer;
    }
    
    private static void dfs(String cur, String curRoute, String[][] tickets) {
        if (curRoute.length() == (N + 1) * 3) {
            allRoutes.add(curRoute);
            return;
        }
        
        for (int i = 0; i < N; i++) {
            if (!visited[i] && tickets[i][0].equals(cur)) {
                visited[i] = true;
                dfs(tickets[i][1], curRoute + tickets[i][1], tickets);
                visited[i] = false;
            }
        }
    }
}