package leetcode.SocialNetwork;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;

public class SocialNetwork {

    public LinkedList<Person> findPathBiBFS(HashMap<Integer, Person> people, int source, int destination){
        BFSData primary = new BFSData(people.get(source));
        BFSData secondary = new BFSData(people.get(destination));

        while(!primary.toVisit.isEmpty() && !secondary.toVisit.isEmpty()){
            Person collision = searchLevel(people, primary, secondary);
            if (collision != null){

            }
            collision = searchLevel(people, secondary, primary);
            if (collision != null){

            }
        }

        return null;
    }

    //Search each level of friends
    public Person searchLevel(HashMap<Integer,Person> people, BFSData primary, BFSData secondary){
        int count = primary.toVisit.size();
        for (int i = 0; i < count; i ++){
            PathNode pathNode = primary.toVisit.poll();
            int personId = pathNode.getPerson().getID();
            //If the personId is visited by secondary, then this node is the intersection
            if (secondary.visited.containsKey(personId)){
                return pathNode.getPerson();
            }

            List<Integer> friends = pathNode.getPerson().getFriends();
            for (Integer friend: friends) {
                if(!primary.visited.containsKey(friend)){
                    Person found = people.get(friend);
                    PathNode newNode = new PathNode(found, pathNode);
                    primary.visited.put(friend, newNode);
                    primary.toVisit.add(newNode);
                }
            }
        }
        return null;
    }

    public LinkedList<Person> mergePaths(BFSData bfs1, BFSData bfs2, int connection){
        PathNode end1 = bfs1.visited.get(connection);
        PathNode end2 = bfs2.visited.get(connection);

        LinkedList<Person> pathOne = end1.collapse(false);
        LinkedList<Person> pathTwo = end2.collapse(true);
        pathTwo.removeFirst();
        pathOne.addAll(pathTwo);
        return pathOne;
    }
}
