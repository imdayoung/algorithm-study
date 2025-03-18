package 구름.그래프탐색;
import java.io.*;
import java.util.*;

class 초급_마법사의_시험 {
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	static int R;
	static int C;
	static int K;
	static int[][] forest;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		forest = new int[R][C];
		
		for (int i = 0; i < R; i++) {
			String temp = br.readLine();
			for (int j = 0; j < C; j++) {
				forest[i][j] = Character.getNumericValue(temp.charAt(j));
			}
		}

		System.out.println(bfs(0, 0));
		br.close();
	}

	private static int bfs(int startX, int startY) {
		Deque<int[]> queue = new ArrayDeque<>();
		queue.offerLast(new int[]{startX, startY, K, 0});

		boolean[][][] visited = new boolean[R][C][K + 1];
		visited[startX][startY][K] = true;

		while (!queue.isEmpty()) {
			int[] cur = queue.pollFirst();
			int x = cur[0];
			int y = cur[1];
			int mana = cur[2];
			int cost = cur[3];

			if (x == R - 1 && y == C - 1) {
				return cost;
			}

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx < 0 || nx > R - 1 || ny < 0 || ny > C - 1 || (forest[nx][ny] == 1 && mana < 10) || visited[nx][ny][mana]) {
					continue;
				}

				if (forest[nx][ny] == 0) {
					queue.offerLast(new int[]{nx, ny, mana, cost + 1});
					visited[nx][ny][mana] = true;
				} else {
					int nnx = nx + dx[i];
					int nny = ny + dy[i];
					if (nnx < 0 || nnx > R - 1 || nny < 0 || nny > C - 1 || forest[nnx][nny] == 1) {
						continue;
					}
					queue.offerLast(new int[]{nnx, nny, mana - 10, cost + 1});
					visited[nnx][nny][mana - 10] = true;
				}
			}
		}
		
		return -1;
	}
}