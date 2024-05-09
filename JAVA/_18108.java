package JAVA;
import java.io.*;


public class _18108 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int y = Integer.parseInt(br.readLine());
        int result = y - 543;
        
        bw.write(Integer.toString(result));
        bw.newLine();
        bw.flush();

        br.close();
        bw.close();
    }
}
