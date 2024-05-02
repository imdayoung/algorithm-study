package JAVA;

import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;


public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        Stack<Integer> stackInt = new Stack<>();

        int N = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N; i++) {
            
            int cmd = Integer.parseInt(br.readLine());
            

            switch (cmd) {
                case 1:
                    
                    break;

                case 2:

                    break;

                case 3:

                    break;

                case 4:
                
                    break;
            
                default:
                    break;
            }
        }
    }
}
