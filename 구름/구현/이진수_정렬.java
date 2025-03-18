package 구름.구현;
import java.io.*;
import java.util.*;

class 이진수_정렬 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		Integer[] numbers = new Integer[N];
		
		StringTokenizer st2 = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			Integer n = Integer.parseInt(st2.nextToken());
			numbers[i] = n;
		}

		Arrays.sort(numbers, (a, b) -> {
			int aCount = Integer.bitCount(a);
			int bCount = Integer.bitCount(b);
			int temp = bCount - aCount;
			if (temp == 0){
				return b - a;	
			}
			return temp;
		});

		System.out.println(numbers[K - 1]);
	}
}