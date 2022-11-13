package leetcode;

import java.util.PriorityQueue;

public class TestConcept {
    public static void main(String[] args) {
//        String test1 = new String("test");
//        String test2 = new String("test");
//        System.out.println(test1==test2);
//        System.out.println(test1.substring(0,4));
          PriorityQueue<Integer> pQueue = new PriorityQueue<Integer>();
          pQueue.add(10);
          pQueue.add(8);
          pQueue.add(9);
          pQueue.add(7);
          while(pQueue.size() != 0){
              System.out.println(pQueue.poll());
          }
    }
}
