package 백준;

import java.io.*;
import java.util.*;

public class _19948 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer poem = new StringTokenizer(br.readLine());
        List<Integer> initials = new ArrayList<>();

        while (poem.hasMoreTokens()) {
            String temp = poem.nextToken();
            char initial = Character.toUpperCase(temp.charAt(0));
            int n = (byte) initial;
            initials.add(n - 65);
        }

        int space =  Integer.parseInt(br.readLine());
        int[] counts = new int[26];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 26; i++) {
            counts[i] = Integer.parseInt(st.nextToken());
        }

        

        for (int initial : initials) {
            System.out.println(initial);
        }

        br.close();
    }
}
