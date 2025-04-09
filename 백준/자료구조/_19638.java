package 백준.자료구조;

import java.io.*;
import java.util.*;

public class _19638 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int HCenti = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());

        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0; i < N; i++) {
            pq.offer(Integer.parseInt(br.readLine()));
        }

        int count = 0;
        for (int i = 0; i < T; i++) {
            int h = pq.poll();

            if (h < HCenti) {
                count = i;
                System.out.println("YES");
                System.out.println(count);
                return;
            }

            int newH = h;

            if (h > 1) {
                newH = h / 2;
            }

            pq.offer(newH);
        }

        if (pq.peek() < HCenti) {
            count = T;
            System.out.println("YES");
            System.out.println(count);
        } else {
            System.out.println("NO");
            System.out.println(pq.poll());
        }

        br.close();
    }
}
