import java.util.Scanner;
import java.util.Arrays;

public class CountingRhyme {
    public static void main(String[] args) {
        boolean safe;
        Scanner stdIn = new Scanner(System.in);
        int repeat = stdIn.nextInt();
        for (int i = 0; i < repeat; i++) {
            int groupSize = stdIn.nextInt();
            int wordCount = stdIn.nextInt();
            Boolean[] group = new Boolean[groupSize];
            Boolean[] comparisonBool = new Boolean[groupSize];
            for(int h = 0; h < groupSize; h++) {
                    group[h] = false;
                    comparisonBool[h] = true;
            }
            int startingMember = 0;
            do {
            
                comparisonBool[0] = false;
                for (int j = startingMember; j < wordCount + startingMember; j++) {
                    if (group[0] == true) {
                        break;
                    }
                    if (group[j % groupSize] == true) {
                        j--;
                    } else {
                        group[j % groupSize] = true;
                    }
                }
                safe = Arrays.equals(group, comparisonBool);
                for(Boolean member : group) {
                    if(member == true) {
                        out++;
                    }
                }
                if(out == groupSize - 1) {
                    
                }
                startingMember++;
            } while (safe);
            System.out.println(startingMember);
        }
    }
}