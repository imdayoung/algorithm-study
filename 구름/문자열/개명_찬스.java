package 구름.문자열;
import java.io.*;

class 개명_찬스 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String answer = "";
		String name = br.readLine();
		int N = name.length();
		
		for (int i = 0; i < N - 1; i++) {
			int num1 = (int)name.charAt(i);
			int num2 = (int)name.charAt(i + 1);

			if (num1 > num2) {
				answer += name.substring(0, i) + name.substring(i + 1, N);
				break;
			}
		}

		if (answer == "") {
			answer = name.substring(0, N - 1);
		}
		
		System.out.println(answer);
	}
}