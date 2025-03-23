package 백준.동적계획법;
import java.io.*;
import java.util.*;

public class _9657 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Map<Integer, String> dict = new HashMap<>();
        dict.put(0, "SK");
        dict.put(1, "CY");

        int N = Integer.parseInt(br.readLine());

        if (N == 1) {
            System.out.println("SK");
            return;
        }

        int[] winner = new int[N + 1];
        winner[2] = 1;

        for (int i = 7; i < N + 1; i++) {
            if (winner[i - 1] == 0 && winner[i - 3] == 0 && winner[i - 4] == 0) {
                winner[i] = 1;
            }
        }

        System.out.println(dict.get(winner[N]));
    }
}