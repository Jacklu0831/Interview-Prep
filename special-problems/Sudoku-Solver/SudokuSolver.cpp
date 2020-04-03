//============================================================================
// Name        : SudokuSolver.cpp
// Author      : Jack Lu
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

// This program uses the recursive backtracking method to solve a 9*9 sudoku

#include <iostream>
#include <fstream>
// #include <chrono>
using namespace std;
// using namespace chrono;

const int size = 9;

void getSud(int[][size], const int);
void showSud(const int[][size], const int);
bool solveSud(int[][size], const int, int, int);
bool checkSud(const int[][size], const int, int, int, int);

int main() {
	cout << "This program lets the user input the content of an ";
	cout << "unsolved Sudoku and provides a solution\n";

	// initialize the 2D array with an unsolved Sudoku
	int sud[size][size];
	getSud(sud, size);

	cout << endl << "Here is the entered Sudoku:";
	showSud(sud, size);

 //    const time_point<high_resolution_clock> startTime = high_resolution_clock::now();
	// solveSud(sud, size, 0, 0);
 //    const time_point<high_resolution_clock> endTime = high_resolution_clock::now();
 //    duration<double> elapsed_seconds = endTime - startTime; 
 //    cout << "Elapsed time: " << elapsed_seconds.count() << " seconds\n";

	if (solveSud(sud, size, 0, 0)){
		showSud(sud, size);
		cout << "Solved!" << endl;
	}
	else
		cout << "Error cannot solve Sudoku\n";
	return 0;
}

void getSud(int sud[][size], int size) {
	// read the file that was just written in
	ifstream inputFile("Sudoku.txt");
	if (!inputFile) {
		cout << "Cannot find file";
		exit(0);
	}
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			inputFile >> sud[i][j];
		}
	}
	inputFile.close();
}

void showSud(const int sud[][size], const int size) {
	for (int i = 0; i < size; i++) {
		if (i % 3 == 0)
			cout << endl << endl;
		else
			cout << endl;
		for (int j = 0; j < size; j++) {
			// the if-else if statements are for formatting
			if (j == size - 1 && (j + 1) % 3 == 0)
				cout << sud[i][j];
			else if (j != size - 1 && (j + 1) % 3 == 0)
				cout << sud[i][j] << "  ";
			else if (j != size - 1 && (j + 1) % 3 != 0)
				cout << sud[i][j] << " ";
		}
	}
	cout << endl << endl;
}

// start solving the Sudoku with recursive function
bool solveSud(int sud[][size], const int size, int row, int col) {
	// increment row and column each time called
	int rowNew = (col == size - 1) ? row + 1 : row;
	int colNew = (col == size - 1) ? 0 : col + 1;

	// indefinitely true when reach there
	if (row == size)
		return 1;
	// if the position already contains a value then re-increment row and column
	if (sud[row][col] != 0)
		return solveSud(sud, size, rowNew, colNew);
	// recursion: keep returning true to the last position, if failed then false to the beginning
	for (int i = 0; i < size; i++) {
		if (checkSud(sud, size, row, col, i + 1)) {
			sud[row][col] = i + 1;

			if (solveSud(sud, size, rowNew, colNew))
				return 1;
			else
				sud[row][col] = 0;
		}
	}
	return 0;
}

// use this function to test if the value input in the Sudoku is valid
bool checkSud(const int sud[][size], const int size, int row, int col,
		int ans) {
	bool rowCheck = true, colCheck = true, squCheck = true;
	// test row
	for (int i = 0; i < size; i++) {
		if (i != col && sud[row][i] == ans)
			rowCheck = 0;
	}
	// test column
	for (int i = 0; i < size; i++) {
		if (i != row && sud[i][col] == ans)
			colCheck = 0;
	}
	// test square
	for (int i = row / 3 * 3; i < row / 3 * 3 + 3; i++) {
		for (int j = col / 3 * 3; j < col / 3 * 3 + 3; j++) {
			if (sud[i][j] == ans && (i != row || j != col))
				squCheck = 0;
		}
	}

	// showSud(sud, size);
	// system("clear");

	// test all
	if (rowCheck && colCheck && squCheck)
		return 1;
	else
		return 0;
}

