package 백준.문자열;

import java.io.*;
import java.util.*;

public class _19948 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String poem = br.readLine();

        int space =  Integer.parseInt(br.readLine());

        int[] counts = new int[26];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 26; i++) {
            counts[i] = Integer.parseInt(st.nextToken());
        }

        char temp = poem.charAt(0);
        if (Character.isUpperCase(temp)) {
            if (counts[(byte) temp - 65] == 0) {
                System.out.println(-1);
                return;
            }
            counts[(byte) temp - 65]--;
        } else {
            if (counts[(byte) temp - 97] == 0) {
                System.out.println(-1);
                return;
            }
            counts[(byte) temp - 97]--;
        }

        for (int i = 1; i < poem.length(); i++) {
            char p = poem.charAt(i);
            if (p != poem.charAt(i - 1)) {
                if (p == ' ') {
                    if (space == 0) {
                        System.out.println(-1);
                        return;
                    }
                    space--;
                } else if (Character.isUpperCase(p)) {
                    if (counts[(byte) p - 65] == 0) {
                        System.out.println(-1);
                        return;
                    }
                    counts[(byte) p - 65]--;
                } else {
                    if (counts[(byte) p - 97] == 0) {
                        System.out.println(-1);
                        return;
                    }
                    counts[(byte) p - 97]--;
                }
            }
        }

        StringBuilder title = new StringBuilder();
        StringTokenizer poemToken = new StringTokenizer(poem);
        while (poemToken.hasMoreTokens()) {
            String word = poemToken.nextToken();
            title.append(Character.toUpperCase(word.charAt(0)));
        }

        char te = title.charAt(0);
        if (counts[(byte) te - 65] == 0) {
            System.out.println(-1);
            return;
        }
        counts[(byte) te - 65]--;

        for (int i = 1; i < title.length(); i++) {
            char t = title.charAt(i);
            if (t != title.charAt(i - 1)) {
                if (counts[(byte) t - 65] == 0) {
                    System.out.println(-1);
                    return;
                }
                counts[(byte) t - 65]--;
            }
        }

        System.out.println(title);
        br.close();
    }
}
