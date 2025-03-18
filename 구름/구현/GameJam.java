package 구름.구현;
import java.io.*;
import java.util.*;

class GameJam {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st1 = new StringTokenizer(br.readLine());
		int Rg = Integer.parseInt(st1.nextToken()) - 1;
		int Cg = Integer.parseInt(st1.nextToken()) - 1;

		StringTokenizer st2 = new StringTokenizer(br.readLine());
		int Rp = Integer.parseInt(st2.nextToken()) - 1;
		int Cp = Integer.parseInt(st2.nextToken()) - 1;

		String[][] board = new String[N][N];		
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				board[i][j] = st.nextToken();	
			}
		}

		int goorm = playGame(Rg, Cg, board, N);
		int player = playGame(Rp, Cp, board, N);

		if (goorm > player) {
			System.out.println("goorm " + goorm);
		} else {
			System.out.println("player " + player);
		}
	}

	private static int playGame(int x, int y, String[][] board, int N) {
		int result = 1;
		boolean[][] visited = new boolean[N][N];
		visited[x][y] = true;
		boolean flag = true;

		while (flag) {
			String commands = board[x][y];
			int M = commands.length();
			int count = Integer.parseInt(commands.substring(0, M - 1));
			char command = commands.charAt(M - 1);

			if (command == 'U') {
				for (int i = 0; i < count; i++) {
					x--;
					if (x < 0) {
						x = N - 1;
					}
	
					if (visited[x][y]) {
						flag = false;
						break;
					}
	
					visited[x][y] = true;
					result++;				
				}

			} else if (command == 'D') {
				for (int i = 0; i < count; i++) {
					x++;
					if (x > N - 1) {
						x = 0;
					}
	
					if (visited[x][y]) {
						flag = false;
						break;
					}
	
					visited[x][y] = true;
					result++;
				}

			} else if (command == 'R') {
				for (int i = 0; i < count; i++) {
					y++;
					if (y > N - 1) {
						y = 0;
					}
	
					if (visited[x][y]) {
						flag = false;
						break;
					}
	
					visited[x][y] = true;
					result++;	
				}
			} else {
				for (int i = 0; i < count; i++) {
					y--;
					if (y < 0) {
						y = N - 1;
					}
	
					if (visited[x][y]) {
						flag = false;
						break;
					}
	
					visited[x][y] = true;
					result++;	
				}
			}
		}
		
		return result;
	}
}