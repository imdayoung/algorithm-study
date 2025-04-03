package 백준.그래프탐색;

import java.io.*;
import java.util.*;

public class _2151 {
    private static int answer = Integer.MAX_VALUE;

    private static int[] dx = {1, 0, -1, 0};
    private static int[] dy = {0, 1, 0, -1};

    private static int N;
    private static char[][] house;
    private static int[][][] visited;

    private static int startX = -1;
    private static int startY = -1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        house = new char[N][N];
        visited = new int[N][N][4];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                Arrays.fill(visited[i][j], Integer.MAX_VALUE);
            }
        }

        for (int i = 0; i < N; i++) {
            house[i] = br.readLine().toCharArray();
            for (int j = 0; j < N; j++) {
                if (house[i][j] == '#') {
                    if (startX == -1 && startY == -1) {
                        startX = i;
                        startY = j;
                    }
                }
            }
        }

        for (int i = 0; i < 4; i++) {
            visited[startX][startY][i] = 0;
        }

        List<int[]> temp = new ArrayList<>();
        temp.add(new int[]{startX, startY, 0 ,0});
        temp.add(new int[]{startX, startY, 1, 0});
        temp.add(new int[]{startX, startY, 2, 0});
        temp.add(new int[]{startX, startY, 3, 0});
        bfs(temp);

        System.out.println(answer);
        br.close();
    }

    private static void bfs(List<int[]> first) {
        Deque<int[]> queue = new ArrayDeque<>();
        for (int[] f : first) {
            queue.offerLast(f);
        }

        while (!queue.isEmpty()) {
            int[] pop = queue.pollFirst();
            int x = pop[0];
            int y = pop[1];
            int d = pop[2];
            int count = pop[3];

            int nx = x + dx[d];
            int ny = y + dy[d];
            
            if (nx < 0 || nx > N - 1 || ny < 0 || ny > N - 1 || house[nx][ny] == '*' || visited[nx][ny][d] < count) {
                continue;
            }

            if (house[nx][ny] == '!') {
                queue.offerLast(new int[]{nx, ny, d, count});
                queue.offerLast(new int[]{nx, ny, (d + 1) % 4, count + 1});
                queue.offerLast(new int[]{nx, ny, (d + 3) % 4, count + 1});
                visited[nx][ny][d] = count;
                visited[nx][ny][(d + 1) % 4] = count;
                visited[nx][ny][(d + 3) % 4] = count;
            } else if (house[nx][ny] == '.') {
                queue.offerLast(new int[]{nx, ny, d, count});
                visited[nx][ny][d] = count;
            } else if (house[nx][ny] == '#') {
                answer = Math.min(answer, count);
            }
        }
    }
}
