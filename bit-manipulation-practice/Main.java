public class Main {

  //Given two 32 bits numbers N and M, and two bits positions, i and j. Insert M into N such that M starts at bit i and ends at bit j
  static int updateBits(int n, int m, int i, int j) {
    int allOnes = ~0;
    int left = allOnes << (j + 1);
    int right = ((1 << i) - 1);

    int mask = left | right;

    int n_cleared = n & mask;
    int m_shifted = m << i;

    return n_cleared | m_shifted;
  }

  //given a real number between 0 and 1 (eg 0.72) that is passed in as a double, print the binary representation. Return error if the number cannot be represented accurately in binary with at most 32 chars
  static String binaryToString(double input) {
    if (input > 1 || input < 0) {
      return "error";
    }

    StringBuilder str = new StringBuilder("0.");
    while (input > 0) {
      if (str.length() > 32) {
        return "error";
      }
      double r = input * 2;
      System.out.println(r);
      if (r >= 1) {
        str.append(1);
        input = r - 1;
      } else {
        str.append(0);
        input = r;
      }
    }
    return str.toString();
  }

  //You can flip exactly one bit. Write code to find the length of the longest sequence of 1s you could create
  static int flipBitToWin(int input) {
    //means every bit
    if (~input == 0) {
      return Integer.BYTES * 8;
    }
    // String binaryString = Integer.toBinaryString(input);
    // System.out.println(binaryString);
    int currentLongest = 0;
    int previousLongest = 0;
    int maxLength = 1;
    while (input > 0) {
      int rightestValue = input & 1;
      if (rightestValue == 1) {
        currentLongest += 1;
      } else if (rightestValue == 0) {
        //check length of 1s (+1 is the bit of 0 change to 1)
        int tempLength = previousLongest + currentLongest + 1;
        if (tempLength > maxLength) {
          maxLength = tempLength;
        }
        if ((input & 2) == 0) {
          previousLongest = 0;
        } else {
          previousLongest = currentLongest;
        }
        currentLongest = 0;
      }
      input = input >>> 1;
      String binaryString = Integer.toBinaryString(input);
      System.out.println(binaryString);
    }
    return maxLength;
  }

  public static void main(String[] args) {
    // String binaryString = Integer.toBinaryString(updateBits(1024,19,2,6));
    // String binaryString = binaryToString(0.75);
    // System.out.println(binaryString);
    System.out.println(flipBitToWin(1775));
  }
}
