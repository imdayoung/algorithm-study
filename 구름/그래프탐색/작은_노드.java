package 구름.그래프탐색;
import java.io.*;
import java.util.*;

class 작은_노드 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		List<List<Integer>> edges = new ArrayList<>();
		for (int i = 0; i < N + 1; i++) {
			edges.add(new ArrayList<>());
		}
		
		for (int i = 0; i < M; i++) {
			StringTokenizer stE = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(stE.nextToken());
			int e = Integer.parseInt(stE.nextToken());

			edges.get(s).add(e);
			edges.get(e).add(s);
		}

		for (int i = 0; i < N + 1; i++) {
			Collections.sort(edges.get(i));
		}

		Map<Integer, Boolean> visited = new HashMap<>();
		visited.put(K, true);

		int count = 1;
		int current = K;
		
		while (true) {
			int next = 0;
			
			for (int i = 0; i < edges.get(current).size(); i++) {
				int temp = edges.get(current).get(i);
				if (!visited.containsKey(temp)) {
					visited.put(temp, true);
					current = temp;
					next = temp;
					count++;
					break;
				}
			}

			if (next == 0) {
				break;
			}
		}

		System.out.println(count + " " + current);
	}
}