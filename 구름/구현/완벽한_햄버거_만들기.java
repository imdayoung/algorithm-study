package 구름.구현;
import java.io.*;
import java.util.*;

class 완벽한_햄버거_만들기 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int[] k = new int[N];

		int maxValue = 0;
		int maxIndex = 0;
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			int temp = Integer.parseInt(st.nextToken());
			k[i] = temp;
			if (temp > maxValue) {
				maxValue = temp;
				maxIndex = i;
			}
		}

		int answer = 0;
		boolean wrong = false;
		
		for (int i = 0; i < maxIndex; i++) {
			if (k[i] > k[i + 1]) {
				wrong = true;
				break;
			}
			answer += k[i];
		}

		if (!wrong){
			for (int i = maxIndex; i < N - 1; i++) {
				if (k[i] < k[i + 1]) {
					wrong = true;
					break;
				}
				answer += k[i];
			}	
		}

		if (wrong) {
			System.out.println(0);
		} else {
			answer += k[N - 1];
			System.out.println(answer);	
		}
	}
}