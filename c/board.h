#ifndef BOARD_H
#DEFINE BOARD_H
#include <stdbool.h>
#DEFINE PLAYER1PIECE 1
#DEFINE PLAYER2PIECE 2
struct board_t {
	int rows;
	int cols;
	int* board[];
	bool player1win;
	bool haswon;
}
#endif
