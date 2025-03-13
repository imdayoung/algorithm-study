import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        
        int n = numbers.length;
        int[] answer = new int[n];
        
        Deque<Integer> deque = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            int number = numbers[i];
            while (deque.size() > 0 && numbers[deque.peekLast()] < number) {
                int temp = deque.pollLast();
                answer[temp] = number;
            }
                
            deque.add(i);
        }
        
        while (deque.size() > 0) {
            int i = deque.poll();
            answer[i] = -1;
        }
        
        deque.offer(1);
        deque.offer(2);
        deque.offer(3);
        deque.offer(4);
        deque.offer(5);
        for (Integer num : deque) {
            System.out.println(num);
        }
        
        return answer;
    }
}