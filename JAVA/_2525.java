package JAVA;
import java.io.*;
import java.util.StringTokenizer;

public class _2525 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(br.readLine());

        int min = B + C;

        int new_hour = (A + min / 60) % 24;
        int new_min = min % 60;

        bw.write(Integer.toString(new_hour) + " ");
        bw.write(Integer.toString(new_min));

        br.close();
        bw.close();
    }
}
