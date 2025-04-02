package 백준.투포인터;

import java.io.*;
import java.util.*;

public class _30804 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int answer = 0;

        int N = Integer.parseInt(br.readLine());
        int[] S = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            S[i] = Integer.parseInt(st.nextToken());
        }

        Map<Integer, Integer> tanghuru = new HashMap<>();

        int start = 0;
        int end = 0;
        int count = 0;

        while (end < N) {
            tanghuru.put(S[end], tanghuru.getOrDefault(S[end], 0) + 1);
            count++;
            while (tanghuru.size() > 2) {
                tanghuru.put(S[start], tanghuru.getOrDefault(S[start], 0) - 1);
                if (tanghuru.get(S[start]) <= 0) {
                    tanghuru.remove(S[start]);
                }
                count--;
                start++;
            }
            end++;
            answer = Math.max(answer, count);
        }

        System.out.println(answer);
        br.close();
    }
}
