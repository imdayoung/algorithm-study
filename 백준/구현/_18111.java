package 백준.구현;

import java.io.*;
import java.util.*;

public class _18111 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        int[][] ground = new int[N][M];

        for (int i = 0; i < N; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                int temp = Integer.parseInt(st2.nextToken());
                ground[i][j] = temp;
            }
        }

        int answerTime = Integer.MAX_VALUE;
        int answerHeight = 0;

        for (int height = 0; height < 256 + 1; height++) {
            int time = 0;
            int block = B;

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (ground[i][j] > height) {
                        int temp = ground[i][j] - height;
                        time += 2 * temp;
                        block += temp;
                    } else if (ground[i][j] < height) {
                        int temp = height - ground[i][j];
                        time += temp;
                        block -= temp;
                    }
                }
            }
            
            if (block < 0) {
                continue;
            }

            if (time <= answerTime) {
                answerTime = time;
                answerHeight = height;
            }
        }

        System.out.println(answerTime + " " + answerHeight);
        br.close();
    }
}