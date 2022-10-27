package main

import "fmt"

func main() {
	grid := [][]int{
		{0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0}, {0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0}, {0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0},
	}
	fmt.Println(maxAreaOfIsland(grid))
}

func maxAreaOfIsland(grid [][]int) int {
	maxArea := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if grid[i][j] == 1 {
				islandSize := findIslandArea(grid, i, j)
				if islandSize > maxArea {
					maxArea = islandSize
				}
			}
		}
	}
	return maxArea
}

func findIslandArea(grid [][]int, first, second int) int {
	if first < 0 || second < 0 || first >= len(grid) || second >= len(grid[first]) || grid[first][second] != 1 {
		return 0
	}

	grid[first][second] = 0

	topArea := findIslandArea(grid, first-1, second)
	bottomArea := findIslandArea(grid, first+1, second)
	leftArea := findIslandArea(grid, first, second-1)
	rightArea := findIslandArea(grid, first, second+1)

	return 1 + topArea + bottomArea + leftArea + rightArea
}
