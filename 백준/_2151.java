package 백준;

import java.io.*;
import java.util.*;

public class _2151 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        char[][] house = new char[N][N];

        for (int i = 0; i < N; i++) {
            String temp = br.readLine();
            for (int j = 0; j < N; j++) {
                house[i][j] = temp.charAt(j);
            }
        }
    }
}
