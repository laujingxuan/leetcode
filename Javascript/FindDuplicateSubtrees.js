/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode[]}
 */
//Time limit exceeded as with time complexity of O(N^3) since potentially we will need to for every element, compare with the whole tree (number of elements times)
var findDuplicateSubtreesNonIdeal = function (root) {
  //of value as key and nodes list as value
  let trackMap = new Map();
  addAllNodesToMap(trackMap, root);
  console.log(trackMap);
  output = [];
  // console.log(trackMap.keys())
  for (const x of trackMap.keys()) {
    // console.log("test")
    nodesList = trackMap.get(x);
    addedIndex = new Set();
    for (let i = 0; i < nodesList.length - 1; i++) {
      if (addedIndex.has(i)) {
        continue;
      }
      for (let j = i + 1; j < nodesList.length; j++) {
        if (checkIfTwoNodesAreSame(nodesList[i], nodesList[j])) {
          if (!addedIndex.has(i)) {
            output.push(nodesList[i]);
          }
          addedIndex.add(i);
          addedIndex.add(j);
        }
      }
    }
  }

  return output;
};

const checkIfTwoNodesAreSame = (nodeOne, nodeTwo) => {
  if (nodeOne === null && nodeTwo === null) {
    return true;
  }
  if (nodeOne === null || nodeTwo === null || nodeOne.val != nodeTwo.val) {
    return false;
  }
  return (
    checkIfTwoNodesAreSame(nodeOne.left, nodeTwo.left) &&
    checkIfTwoNodesAreSame(nodeOne.right, nodeTwo.right)
  );
};

const addAllNodesToMap = (trackMap, root) => {
  if (root === null) {
    return;
  }
  // console.log(root.val)
  if (trackMap.has(root.val)) {
    foundList = trackMap.get(root.val);
    foundList.push(root);
  } else {
    newList = [root];
    trackMap.set(root.val, newList);
  }
  addAllNodesToMap(trackMap, root.left);
  addAllNodesToMap(trackMap, root.right);
  return;
};
