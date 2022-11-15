package leetcode;

public class CountAndSayBacktrack {
    public static void main(String[] args) {
        System.out.println(countAndSay(4));
    }

    public static String countAndSay(int n) {
        if (n <= 1) {
            return Integer.toString(n);
        }

        String previousInt = countAndSay(n - 1);
        System.out.println("check: " + previousInt);
        char beforeChar = previousInt.charAt(0);
        System.out.println("beforeChar: " + beforeChar);
        int count = 0;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < previousInt.length(); i++) {
            if (previousInt.charAt(i) == beforeChar) {
                count++;
                continue;
            }
            sb.append(count);
            sb.append(beforeChar);
            beforeChar = previousInt.charAt(i);
            count = 1;
        }
        sb.append(count);
        sb.append(beforeChar);
        String currentIntString = sb.toString();
        System.out.println("currentIntString: " + currentIntString);
        return currentIntString;
    }
}
