package 백준.수학;

import java.io.*;
import java.util.*;

public class _13116 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            Set<Integer> aParents = new HashSet<>();
            aParents.add(A);
            while (A > 1) {
                A /= 2;
                aParents.add(A);
            }

            System.out.println(aParents);

            while (B > 0) {
                if (aParents.contains(B)) {
                    System.out.println(B * 10);
                    break;
                }
                B /= 2;
            }
        }
        br.close();
    }
}
