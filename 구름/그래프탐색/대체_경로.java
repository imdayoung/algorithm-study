package 구름.그래프탐색;

import java.io.*;
import java.util.*;

class 대체_경로 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int S = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());

		List<List<Integer>> edges = new ArrayList<>();
		for (int i = 0; i < N + 1; i++) {
			edges.add(new ArrayList<>());
		}
		
		for (int i = 0; i < M; i++) {
			StringTokenizer st2 = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st2.nextToken());
			int v = Integer.parseInt(st2.nextToken());
			edges.get(u).add(v);
			edges.get(v).add(u);
		}

		int result = -1;
		
		for (int i = 1; i < N + 1; i++) {
			if (S == i || E == i) {
				result = -1;
			} else {
				result = bfs(S, E, edges, i, N);
			}

			System.out.println(result);
		}
	}

	private static int bfs(int start, int end, List<List<Integer>> edges, int unavailabe, int N) {
		Deque<Integer> queue = new ArrayDeque<>();
		queue.offerLast(start);

		int[] visited = new int[N + 1];
		visited[start] = 1;

		while (!queue.isEmpty()) {
			int city = queue.pollFirst();
			if (city == end) {
				return visited[city];
			}
			
			List<Integer> temp = edges.get(city);
			for (int next : temp) {
				if (visited[next] != 0 || next == unavailabe) {
					continue;
				}

				visited[next] = visited[city] + 1;
				queue.offerLast(next);
			}
		}
		
		return -1;
	}
}