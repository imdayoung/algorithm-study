package 백준.그리디;

import java.io.*;
import java.util.*;

public class _1911 {
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        int[][] puddle = new int[N][2];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            puddle[i][0] = Integer.parseInt(st.nextToken());
            puddle[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(puddle, (a, b) -> a[0] - b[0]);
        
        int answer = 0;
        int range = 0;

        for (int i = 0; i < N; i++) {
            int start = puddle[i][0];
            int end = puddle[i][1];

            if (start > range) {
                range = start;
            }

            while (end > range) {
                range += L;
                answer++;
            }
        }
        
        System.out.println(answer);
        br.close();
    }
}
