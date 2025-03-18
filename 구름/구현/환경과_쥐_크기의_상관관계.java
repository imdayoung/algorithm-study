package 구름.구현;
import java.io.*;
import java.util.*;

class 환경과_쥐_크기의_상관관계 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String answer = "bad";
		
		int N = Integer.parseInt(br.readLine());
		int[] A = new int[N];
		int[] B = new int[N];

		StringTokenizer stA = new StringTokenizer(br.readLine());
		StringTokenizer stB = new StringTokenizer(br.readLine());

		for (int i = 0; i < N; i++) {
			A[i] = Integer.parseInt(stA.nextToken());
			B[i] = Integer.parseInt(stB.nextToken());
		}

		Arrays.sort(A);
		Arrays.sort(B);

		int a = getRepresentValue(A, N);
		int b = getRepresentValue(B, N);
		if (a > b) {
			answer = "good";
		}

		System.out.println(a + " " + b);
		System.out.println(answer);
	}

	private static int getRepresentValue(int[] weights, int N) {
		int result = 0;
		
		Deque<Integer> queue = new ArrayDeque<>();
		List<Integer> list = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			queue.offerLast(weights[i]);
			while (queue.peekLast() - queue.peekFirst() > 4) {
				queue.pollFirst();
			}
			
			if (queue.size() > list.size()) {
				list = new ArrayList<>(queue);
			}
		}

		result = list.get(0) + 2;
		if (list.get(list.size() - 1) < result + 2) {
			int diff = result + 2 - list.get(list.size() - 1);
			result -= diff;
		}
		return result;
	}
}