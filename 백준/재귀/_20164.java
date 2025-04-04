package 백준.재귀;

import java.io.*;

public class _20164 {
    private static int maxValue = -Integer.MAX_VALUE;
    private static int minValue = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int number = Integer.parseInt(br.readLine());
        recurs(number, 0);

        System.out.println(minValue + " " + maxValue);
        
        br.close();
    }

    private static void recurs(int number, int oddCount) {
        oddCount += countOddNumber(number);

        if (number / 10 == 0) {
            maxValue = Math.max(maxValue, oddCount);
            minValue = Math.min(minValue, oddCount);
        } else if (number / 100 == 0) {
            int newNumber = number / 10;
            newNumber += number % 10;
            recurs(newNumber, oddCount);
        } else {
            String numberStr = String.valueOf(number);

            for (int i = 0; i < numberStr.length() - 2; i++) {
                for (int j = i + 1; j < numberStr.length() - 1; j++) {
                    int newNumber = Integer.parseInt(numberStr.substring(0, i + 1));
                    newNumber += Integer.parseInt(numberStr.substring(i + 1, j + 1));
                    newNumber += Integer.parseInt(numberStr.substring(j + 1));
                    recurs(newNumber, oddCount);
                }
            }
        }
    }

    private static int countOddNumber(int number) {
        int oddCount = 0;

        while (number > 0) {
            int temp = number % 10;
            if (temp % 2 == 1) {
                oddCount++;
            }
            
            number /= 10;
        }

        return oddCount;
    }
}