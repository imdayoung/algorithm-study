package 백준.자료구조;
import java.io.*;
import java.util.*;

public class _1822 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int count = 0;
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int nA = Integer.parseInt(st.nextToken());
        int nB = Integer.parseInt(st.nextToken());

        int[] A = new int[nA];
        Map<Integer, Integer> B = new HashMap<>();

        StringTokenizer stA = new StringTokenizer(br.readLine());
        StringTokenizer stB = new StringTokenizer(br.readLine());

        for (int i = 0; i < nA; i++) {
            A[i] = Integer.parseInt(stA.nextToken());
        }
        Arrays.sort(A);

        for (int i = 0; i < nB; i++) {
            B.put(Integer.parseInt(stB.nextToken()), 1);
        }

        for (int i = 0; i < nA; i++) {
            if (!B.containsKey(A[i])) {
                count++;
                sb.append(A[i] + " ");
            }
        }        

        System.out.println(count);
        if (count > 0) {
            System.out.println(sb);
        }

        br.close();
    }
}
