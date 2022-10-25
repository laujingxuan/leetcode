package leetcode;

public class IsPalindrome {
    public static void main(String[] args) {
        System.out.println("isPalindrome: " + isPalindrome("A man, a plan, a canal: Panama"));
    }

    public static boolean isPalindrome(String s){
        int firstIndex = 0;
        int lastIndex = s.length() - 1;
        while (lastIndex > firstIndex){
            char front = s.charAt(firstIndex);
            if (!Character.isLetterOrDigit(front)){
                firstIndex ++;
                continue;
            }
            char end = s.charAt(lastIndex);
            if (!Character.isLetterOrDigit(end)){
                lastIndex --;
                continue;
            }
            if (Character.toLowerCase(front) != Character.toLowerCase(end)){
                return false;
            }
            firstIndex ++;
            lastIndex --;
        }
        return true;
    }
}
