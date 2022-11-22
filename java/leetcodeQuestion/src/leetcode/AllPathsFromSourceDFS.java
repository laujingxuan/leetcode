package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class AllPathsFromSourceDFS {

    public static void main(String[] args) {
        int[][] graph = new int[][] { { 1, 2 }, { 3 }, { 3 }, {} };
        System.out.println(Arrays.deepToString(allPathsSourceTarget(graph).toArray()));
    }

    // Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find
    // all possible paths from node 0 to node n - 1 and return them in any order.
    // The graph is given as follows: graph[i] is a list of all nodes you can visit
    // from node i (i.e., there is a directed edge from node i to node graph[i][j]).
    public static List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        if (graph.length == 0) {
            return new ArrayList<>();
        }
        List<List<Integer>> foundPaths = new ArrayList<>();
        findPathHelper(foundPaths, graph, new ArrayList<>(), 0);
        return foundPaths;
    }

    public static void findPathHelper(List<List<Integer>> foundPaths, int[][] graph, List<Integer> currentPath,
            int index) {
        currentPath.add(index);
        if (index == graph.length - 1) {
            foundPaths.add(currentPath);
            return;
        }

        for (int i : graph[index]) {
            List<Integer> newSet = new ArrayList<>(currentPath);
            findPathHelper(foundPaths, graph, newSet, i);
        }
        return;
    }
}
