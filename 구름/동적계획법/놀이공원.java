package 구름.동적계획법;
import java.io.*;
import java.util.*;

class 놀이공원 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
	
			int[][] board = new int[N][N];
			for (int i = 0; i < N; i++) {
				StringTokenizer st2 = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					board[i][j] = Integer.parseInt(st2.nextToken());
				}
			}
			
			int answer = N * N;
			
			for (int i = 0; i < N - K + 1; i++) {
				for (int j = 0; j < N - K + 1; j++) {
					int count = 0;
					for (int x = i; x < i + K; x++) {
						for (int y = j; y < j + K; y++) {
							count += board[x][y];
						}
					}
					answer = Math.min(answer, count);
				}
			}

			System.out.println(answer);
		}
	}
}