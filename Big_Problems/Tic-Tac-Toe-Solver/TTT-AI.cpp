//============================================================================
// Name        : TicTacTron.cpp
// Author      : Jack Lu
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int AIMoveRow = -1, AIMoveCol = -1;
int depth = 9;

void displayBoard(char state[3][3]) {
	for (int i = 0; i < 3; i++) {
		cout << "         " << " |     |" << endl;
		cout << "       " << state[i][0] << "  |  " << state[i][1] << "  |  "
				<< state[i][2] << endl;
		cout << "         " << " |     |" << endl;
		if (i != 2)
			cout << "     -----------------" << endl;
	}
	cout << endl;
}

int evaluate(char state[3][3]) {

	for (int i = 0; i < 3; i++) {
		if (state[i][0] == state[i][1] && state[i][0] == state[i][2]) {
			if (state[i][0] == 'O')
				return 1;
			else if (state[i][0] == 'X')
				return -1;

		}
	}
	for (int j = 0; j < 3; j++) {
		if (state[0][j] == state[1][j] && state[0][j] == state[2][j]) {
			if (state[0][j] == 'O')
				return 1;
			else if (state[0][j] == 'X')
				return -1;
		}
	}

	if ((state[0][0] == state[1][1] && state[0][0] == state[2][2])
			|| (state[0][2] == state[1][1] && state[0][2] == state[2][0])) {
		if (state[1][1] == 'O')
			return 1;
		else if (state[1][1] == 'X')
			return -1;
	}
	return 0;
}

int isFull(char state[3][3]) {
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			if (state[i][j] == ' ')
				return false;
		}
	}
	return true;
}

int minimax(char state[3][3], int depth, int alpha, int beta, bool isAI) {
	if (evaluate(state) != 0 || depth == 0)
		return evaluate(state);
	if (isFull(state))
		return 0;
	if (isAI) {
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (state[i][j] == ' ') {
					state[i][j] = 'O';
					alpha = max(alpha, minimax(state, depth - 1, alpha, beta, false));
					state[i][j] = ' ';
					if (alpha >= beta)
						break;
				}
			}
		}
		return alpha;
	}
	else {
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (state[i][j] == ' ') {
					state[i][j] = 'X';
					beta = min(beta, minimax(state, depth - 1, alpha, beta, true));
					state[i][j] = ' ';
					if (alpha >= beta)
						break;
				}
			}
		}
		return beta;
	}
}

void findAIMove(char state[3][3]) {
	int maxEval = INT_MIN;
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			if (state[i][j] == ' ') {
				state[i][j] = 'O';
				int eval = minimax(state, depth, INT_MIN, INT_MAX, false);
				state[i][j] = ' ';
				if (eval > maxEval) {
					AIMoveRow = i;
					AIMoveCol = j;
					maxEval = eval;
				}
			}
		}
	}
}

void humanMove(char state[3][3]) {
	int position;
	cout << "Enter the position of your next move (1-9): ";
	againInput: cin >> position;

	int rowPosition = (position - 1) / 3;
	int colPosition = (position - 1) % 3;

	if (state[rowPosition][colPosition] != ' ') {
		cout << "Invalid input, enter again: ";
		goto againInput;
	}
	state[rowPosition][colPosition] = 'X';
}

void AIMove(char state[3][3]) {

	findAIMove(state);
	state[AIMoveRow][AIMoveCol] = 'O';

	displayBoard(state);

	int position = 3 * AIMoveRow + AIMoveCol + 1;
	cout << "The AI has chosen position " << position << "." << endl;
}

int main() {
	restart: char board[3][3] = { { ' ', ' ', ' ' }, { ' ', ' ', ' ' }, { ' ',
			' ', ' ' } };

	cout << "--------------------------" << endl;
	cout << "The Impossible Tic Tac Toe" << endl;
	cout << "--------------------------" << endl << endl;

	displayBoard(board);
	while (evaluate(board) == 0 && !isFull(board)) {
		humanMove(board);
		AIMove(board);
		depth--;
	}

	if (evaluate(board) == 1)
		cout << "The AI win." << endl;
	else if (evaluate(board) == -1)
		cout << "You win. The AI needs some fixing." << endl;
	else
		cout << "Tie game. You must be a careful player." << endl;

	char again;
	cout << endl << "Type Y to play again or anything else to stop playing: ";
	cin >> again;
	cout << endl;
	if (again != 'Y' && again != 'y') {
		cout << "Goodbye. Hope you had fun.";
	} else {
		goto restart;
	}

	return 0;
}

