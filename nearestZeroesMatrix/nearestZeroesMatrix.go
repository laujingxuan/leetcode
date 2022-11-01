package main

//Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
func updateMatrixOwnTry(mat [][]int) [][]int {
	if len(mat) == 0 {
		return mat
	}
	output := make([][]int, len(mat))
	for i := range output {
		output[i] = make([]int, len(mat[0]))
	}
	for i := 0; i < len(mat); i++ {
		for j := 0; j < len(mat[0]); j++ {
			value := checkNearestZeroOwnTry(i, j, mat)
			output[i][j] = value
		}
	}
	return output
}

func checkNearestZeroOwnTry(i, j int, mat [][]int) int {
	queue := [][]int{}
	queue = append(queue, []int{i, j})
	n := 0
	duplicated := make([][]int, len(mat))
	for i := range duplicated {
		duplicated[i] = make([]int, len(mat[0]))
		copy(duplicated[i], mat[i])
	}
	for len(queue) != 0 {
		queueLen := len(queue)
		for x := 0; x < queueLen; x++ {
			current := queue[x]
			if current[0] < 0 || current[1] < 0 || current[0] > len(duplicated)-1 || current[1] > len(duplicated[0])-1 {
				continue
			}
			if duplicated[current[0]][current[1]] == 0 {
				return n
			} else if duplicated[current[0]][current[1]] == -1 {
				continue
			}
			duplicated[current[0]][current[1]] = -1
			queue = append(queue, []int{current[0] - 1, current[1]})
			queue = append(queue, []int{current[0] + 1, current[1]})
			queue = append(queue, []int{current[0], current[1] - 1})
			queue = append(queue, []int{current[0], current[1] + 1})
		}
		n++
	}
	return -1
}

//Instead of calculate and find the 0 for each cell, we flip it with starting from zero, and set cell around 0 to 1 and +1 +1...
func updateMatrixIdeal(mat [][]int) [][]int {
	if len(mat) == 0 {
		return mat
	}
	queue := [][]int{}
	for i := 0; i < len(mat); i++ {
		for j := 0; j < len(mat[0]); j++ {
			if mat[i][j] == 0 {
				queue = append(queue, []int{i, j})
				mat[i][j] = 0
			} else {
				mat[i][j] = -1
			}
		}
	}

	for len(queue) != 0 {
		current := queue[0]
		queue = queue[1:]
		looping := [][]int{{current[0] - 1, current[1]}, {current[0] + 1, current[1]}, {current[0], current[1] - 1}, {current[0], current[1] + 1}}

		for _, surrounding := range looping {
			if surrounding[0] < 0 || surrounding[1] < 0 || surrounding[0] > len(mat)-1 || surrounding[1] > len(mat[0])-1 || mat[surrounding[0]][surrounding[1]] >= 0 {
				continue
			}
			mat[surrounding[0]][surrounding[1]] = mat[current[0]][current[1]] + 1
			queue = append(queue, []int{surrounding[0], surrounding[1]})
		}
	}
	return mat
}
