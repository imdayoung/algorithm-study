package 구름.그래프탐색;
import java.io.*;
import java.util.*;

class 폭탄_구현하기_2 {
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	static String[][] ground;
	static int[][] bombGround;
	static int N;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int answer = 0;
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		ground = new String[N][N];
		bombGround = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			StringTokenizer stB = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				ground[i][j] = stB.nextToken();
			}
		}

		for (int i = 0; i < K; i++) {
			StringTokenizer coords = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(coords.nextToken()) - 1;
			int y = Integer.parseInt(coords.nextToken()) - 1;
			bomb(x, y);
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				answer = Math.max(answer, bombGround[i][j]);
			}
		}

		System.out.println(answer);
	}

	private static void bomb(int x, int y) {
		if (ground[x][y].equals("0")) {
			bombGround[x][y] += 1;
		} else if (ground[x][y].equals("@")) {
			bombGround[x][y] += 2;
		}
		
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || nx > N - 1 || ny < 0 || ny > N - 1 || ground[nx][ny].equals("#")) {
				continue;
			}

			if (ground[nx][ny].equals("@")) {
				bombGround[nx][ny] += 2;
			} else {
				bombGround[nx][ny] += 1;
			}
		}
	}
}