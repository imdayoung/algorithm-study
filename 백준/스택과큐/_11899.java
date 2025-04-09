package 백준.스택과큐;

import java.io.*;
import java.util.*;

public class _11899 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int answer = 0;

        StringBuilder s = new StringBuilder(br.readLine());
        Deque<Character> stack = new ArrayDeque<>();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ')') {
                if (stack.isEmpty()) {
                    answer++;
                } else {
                    stack.pollLast();
                }
            } else if (s.charAt(i) == '(') {
                stack.offerLast('(');
            }
        }

        answer += stack.size();
        System.out.println(answer);
        br.close();
    }
}
