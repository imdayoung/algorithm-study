package 구름.그리디;
import java.io.*;
import java.util.*;

class 통증 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int answer = 0;
		
		int N = Integer.parseInt(br.readLine());

		if (N >= 14) {
			while (N >= 14) {
				N -= 14;
				answer++;
			}	
		}
		
		if (N >= 7) {
			while (N >= 7) {
				N -= 7;
				answer++;
			}
		}

		if (N >= 1) {
			while (N >= 1) {
				N -= 1;
				answer++;
			}
		}

		System.out.println(answer);
	}
}