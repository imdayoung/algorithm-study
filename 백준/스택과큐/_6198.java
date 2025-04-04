package 백준.스택과큐;

import java.io.*;
import java.util.*;

public class _6198 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long answer = 0;

        int N = Integer.parseInt(br.readLine());
        int[] H = new int[N];

        for (int i = 0; i < N; i++) {
            H[i] = Integer.parseInt(br.readLine());
        }

        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            while (!stack.isEmpty() && H[i] >= H[stack.peekLast()]) {
                int j = stack.pollLast();
                answer += (i - j - 1);
            }

            stack.offerLast(i);
        }

        while (!stack.isEmpty()) {
            int i = stack.pollLast();
            answer += (N - i - 1);
        }

        System.out.println(answer);
        br.close();
    }
}
