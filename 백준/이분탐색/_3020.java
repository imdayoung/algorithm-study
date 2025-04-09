package 백준.이분탐색;

import java.io.*;
import java.util.*;

public class _3020 {
    private static StringTokenizer st;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int H = Integer.parseInt(st.nextToken());

        int[] down = new int[N / 2];
        int[] up = new int[N / 2];
        
        for (int i = 0; i < N / 2; i++) {
            up[i] = Integer.parseInt(br.readLine());
            down[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(up);
        Arrays.sort(down);

        int answerMin = Integer.MAX_VALUE;
        int answerCnt = 0;

        for (int i = 1; i < H + 1; i++) {
            int d = getDestroyCount(0, N / 2, down, i);
            int u = getDestroyCount(0, N / 2, up, H - i + 1);

            if (d + u < answerMin) {
                answerMin = d + u;
                answerCnt = 1;
            } else if (d + u == answerMin) {
                answerCnt++;
            }
        }
        
        System.out.println(answerMin + " " + answerCnt);
        br.close();
    }

    private static int getDestroyCount(int start, int end, int[] arr, int h) {
        while (start < end) {
            int mid = (start + end) / 2;

            if (arr[mid] >= h) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }

        return arr.length - end;
    }
}
