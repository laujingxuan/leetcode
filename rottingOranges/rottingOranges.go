package main

func orangesRotting(grid [][]int) int {
	if len(grid) == 0 {
		return 0
	}
	queue := [][]int{}
	numberOfFresh := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 2 {
				queue = append(queue, []int{i - 1, j})
				queue = append(queue, []int{i + 1, j})
				queue = append(queue, []int{i, j - 1})
				queue = append(queue, []int{i, j + 1})
			} else if grid[i][j] == 1 {
				numberOfFresh++
			}
		}
	}

	if numberOfFresh == 0 {
		return 0
	}
	totalMinutes := 0
	for len(queue) != 0 {
		for i := len(queue); i > 0; i-- {
			current := queue[0]
			queue = queue[1:]
			if current[0] < 0 || current[1] < 0 || current[0] > len(grid)-1 || current[1] > len(grid[0])-1 || grid[current[0]][current[1]] == 0 || grid[current[0]][current[1]] == 2 {
				continue
			}
			grid[current[0]][current[1]] = 2
			numberOfFresh--
			queue = append(queue, []int{current[0] - 1, current[1]})
			queue = append(queue, []int{current[0] + 1, current[1]})
			queue = append(queue, []int{current[0], current[1] - 1})
			queue = append(queue, []int{current[0], current[1] + 1})
		}
		totalMinutes++
	}
	if numberOfFresh != 0 {
		return -1
	}
	return totalMinutes - 1
}
