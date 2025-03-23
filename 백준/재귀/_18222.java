package 백준.재귀;
import java.io.*;

public class _18222 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        long k = Long.parseLong(br.readLine());
        System.out.println(getNumber(k - 1));
    }

    private static int getNumber(long idx) {
        if (idx == 0) {
            return 0;
        } else if (idx == 1) {
            return 1;
        } else if (idx % 2 == 0) {
            return getNumber(idx / 2);
        } else {
            return 1 - getNumber(idx / 2);
        }
    }
}