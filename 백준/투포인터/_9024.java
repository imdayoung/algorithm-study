package 백준.투포인터;

import java.io.*;
import java.util.*;

public class _9024 {
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < t; tc++) {
            int answer = 0;
            int diffWithK = Integer.MAX_VALUE;

            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            int[] S = new int[n];

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                S[i] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(S);

            int start = 0;
            int end = n - 1;

            while (start < end) {
                int cur = S[start] + S[end];

                int diff = Math.abs(cur - K);
                if (diff < diffWithK) {
                    diffWithK = diff;
                    answer = 1;
                } else if (diff == diffWithK) {
                    answer++;
                }

                if (cur > K) {
                    end--;
                } else {
                    start++;
                }
            }

            System.out.println(answer);
        }

        br.close();
    }
}
