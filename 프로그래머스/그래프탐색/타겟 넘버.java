import java.util.*;

class Solution {
    int answer = 0;
    
    public int solution(int[] numbers, int target) {
        dfs(0, 0, 0, numbers, target, numbers.length);
        return answer;
    }
    
    private void dfs(int cur, int start, int cnt, int[] numbers, int target, int n) {
        if (cnt == n) {
            if (cur == target) {
                answer++;
            }
            return;
        }
        
        for (int i = start; i < n; i++) {
            dfs(cur + numbers[i], i + 1, cnt + 1, numbers, target, n);
            dfs(cur - numbers[i], i + 1, cnt + 1, numbers, target, n);
        }
    }
}