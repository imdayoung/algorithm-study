package 백준;

import java.io.*;
import java.util.*;

public class _6591 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            if (n == 0 && k == 0) {
                break;
            }

            long answer = 1;

            if (n - k < k) {
                k = n - k;
            }

            for (int i = 1; i < k + 1; i++) {
                answer = answer * (n - k + i) / i;
            }

            System.out.println(answer);
        }

        br.close();
    }
}
