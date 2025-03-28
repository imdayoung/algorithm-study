package 백준.브루트포스;
import java.io.*;
import java.util.*;

public class _15658 {
    private static int maxValue = -Integer.MAX_VALUE;
    private static int minValue = Integer.MAX_VALUE;

    private static int N;
    private static int[] A;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
        N = Integer.parseInt(br.readLine());
        A = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        StringTokenizer st2 = new StringTokenizer(br.readLine());
        int[] cal = new int[4];
        for (int i = 0; i < 4; i++) {
            cal[i] = Integer.parseInt(st2.nextToken());
        }

        backtracking(A[0], 1, cal[0], cal[1], cal[2], cal[3]);

        System.out.println(maxValue);
        System.out.println(minValue);
        br.close();
    }

    private static void backtracking(int cur, int idx, int plus, int minus, int mul, int div) {
        if (idx == N) {
            minValue = Math.min(minValue, cur);
            maxValue = Math.max(maxValue, cur);
            return;
        }
        
        if (plus > 0) {
            backtracking(cur + A[idx], idx + 1, plus - 1, minus, mul, div);
        }

        if (minus > 0) {
            backtracking(cur - A[idx], idx + 1, plus, minus - 1, mul, div);
        }

        if (mul > 0) {
            backtracking(cur * A[idx], idx + 1, plus, minus, mul - 1, div);
        }

        if (div > 0) {
            backtracking(cur / A[idx], idx + 1, plus, minus, mul, div - 1);
        }
    }
}
