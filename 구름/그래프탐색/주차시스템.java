package 구름.그래프탐색;
import java.io.*;
import java.util.*;

class 주차클래스 {
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	static boolean[][] visited;
	static int[][] board;
	static int N;
	static int M;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int answer = 0;

		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		visited = new boolean[N][M];
		board = new int[N][M];
		
		for (int i = 0; i < N; i++) {
			StringTokenizer st2 = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				board[i][j] = Integer.parseInt(st2.nextToken());
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (board[i][j] != 1 && !visited[i][j]) {
					int score = bfs(i, j);
					answer = Math.max(answer, score);
				}
			}
		}

		System.out.println(answer);
	}

	private static int bfs(int startX, int startY) {
		int result = 0;
		if (board[startX][startY] == 0) {
			result = 1;
		} else {
			result = -2;
		}
		
		Deque<int[]> queue = new ArrayDeque<>();
		queue.offerLast(new int[]{startX, startY});
		visited[startX][startY] = true;

		while (!queue.isEmpty()) {
			int[] coords = queue.pollFirst();
			int x = coords[0];
			int y = coords[1];

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx < 0 || nx > N - 1 || ny < 0 || ny > M - 1 || visited[nx][ny] || board[nx][ny] == 1) {
					continue;
				}

				if (board[nx][ny] == 0) {
					result += 1;
				} else if (board[nx][ny] == 2) {
					result -= 2;
				}

				queue.offerLast(new int[]{nx, ny});
				visited[nx][ny] = true;
			}
		}
		
		return result;
	}
}