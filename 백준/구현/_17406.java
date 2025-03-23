package 백준.구현;
import java.io.*;
import java.util.*;

public class _17406 {
    private static int N;
    private static int M;
    private static int K;
    private static int[][] A;
    private static Map<Integer, int[]> rotateInfo = new HashMap<>();

    private static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        A = new int[N][M];

        for (int i = 0; i < N; i++) {
            StringTokenizer stA = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                A[i][j] = Integer.parseInt(stA.nextToken());
            }
        }

        for (int i = 0; i < K; i++) {
            StringTokenizer stR = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(stR.nextToken()) - 1;
            int c = Integer.parseInt(stR.nextToken()) - 1;
            int s = Integer.parseInt(stR.nextToken());

            rotateInfo.put(i, new int[]{r, c, s});
        }

        getRotateOrder(new ArrayList<>(), new boolean[K]);
        System.out.println(answer);
    }

    private static void getRotateOrder(List<Integer> order, boolean[] visited) {
        if (order.size() == K) {
            rotate(order);
            return;
        }

        for (int i = 0; i < K; i++) {
            if (!visited[i]) {
                visited[i] = true;
                order.add(i);
                getRotateOrder(order, visited);
                visited[i] = false;
                order.remove(Integer.valueOf(i));
            }
        }
    }

    private static void rotate(List<Integer> order) {
        int[][] tempA = new int[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                tempA[i][j] = A[i][j];
            }
        }

        for (int o : order) {
            int r = rotateInfo.get(o)[0];
            int c = rotateInfo.get(o)[1];
            int s = rotateInfo.get(o)[2];

            for (int k = 1; k <= s; k++) {
                int temp = tempA[r - k][c - k];

                // 왼쪽
                for (int i = r - k + 1; i <= r + k; i++) {
                    tempA[i - 1][c - k] = tempA[i][c - k];
                }

                // 아래
                for (int j = c - k + 1; j <= c + k; j++) {
                    tempA[r + k][j - 1] = tempA[r + k][j];
                }

                // 오른쪽
                for (int i = r + k - 1; i >= r - k; i--) {
                    tempA[i + 1][c + k] = tempA[i][c + k];
                }

                // 위
                for (int j = c + k - 1; j > c - k; j--) {
                    tempA[r - k][j + 1] = tempA[r - k][j];
                }

                tempA[r - k][c - k + 1] = temp;
            }
        }

        answer = Math.min(answer, getMinimumA(tempA));
    }

    private static int getMinimumA(int[][] A) {
        int result = Integer.MAX_VALUE;

        for (int i = 0; i < N; i++) {
            int temp = 0;
            for (int j = 0; j < M; j++) {
                temp += A[i][j];
            }
            result = Math.min(result, temp);
        }

        return result;
    }
}