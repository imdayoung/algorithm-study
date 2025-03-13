import java.util.*;

class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        
        Map<Integer, Integer> older = new HashMap<>();
        Map<Integer, Integer> younger = new HashMap<>();
        
        for (int t : topping) {
            older.put(t, older.getOrDefault(t, 0) + 1);
        }
        
        for (int t : topping) {
            younger.put(t, younger.getOrDefault(t, 0) + 1);
            older.put(t, older.get(t) - 1);
            if (older.get(t) == 0) {
                older.remove(t);
            }
            
            if (older.size() == younger.size()) {
                answer++;
            }
        }
        
        return answer;
    }
}