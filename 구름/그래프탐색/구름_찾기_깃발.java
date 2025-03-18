package 구름.그래프탐색;
import java.io.*;
import java.util.*;

class 구름_찾기_깃발 {
	static int[] dx = {0, 1, 0, -1, 1, 1, -1, -1};
	static int[] dy = {1, 0, -1, 0, 1, -1, 1, -1};
	static int N;
	static int[][] board;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int answer = 0;
		
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		board = new int[N][N];

		for (int i = 0; i < N; i++) {
			StringTokenizer stB = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				board[i][j] = Integer.parseInt(stB.nextToken());
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (board[i][j] == 0) {
					int goorm = findGoorm(i, j);
					if (goorm == K) {
						answer++;
					}
				}
			}
		}

		System.out.println(answer);
	}

	private static int findGoorm(int x, int y) {
		int count = 0;
		
		for (int i = 0; i < 8; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || nx > N - 1 || ny < 0 || ny > N - 1) {
				continue;
			}

			if (board[nx][ny] == 1) {
				count++;
			}
		}

		return count;
	}
}