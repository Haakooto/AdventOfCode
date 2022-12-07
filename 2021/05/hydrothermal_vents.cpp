#include <iostream>
#include <cmath>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

int main() {
	ifstream inp("05");

	int extent = 1000;
	int danger = 0;

	int **field = new int *[extent];
	for (int i=0; i<extent; i++){
		field[i] = new int [extent];
		for (int j=0; j<extent; j++){
			field[i][j] = 0;
		}
	}

	string p1, p2, arrow;
	size_t c;
	int x1, x2, y1, y2, dx, dy;
	while(inp >> p1 >> arrow >> p2){
		c = p1.find(',');
		x1 = stoi(p1.substr(0, c));
		y1 = stoi(p1.substr(c+1));
		c = p2.find(',');
		x2 = stoi(p2.substr(0, c));
		y2 = stoi(p2.substr(c+1));

		if (x1 == x2 || y1 == y2){
			for (int x = min(x1, x2); x <= max(x1, x2); x++){
				for (int y = min(y1, y2); y <= max(y1, y2); y++){
					field[x][y]++;
					if (field[x][y] == 2){danger++;}
				}
			}
		} else {  // comment out this else block to get part1 solution
			dx = abs(x2 - x1) / (x2 - x1);
			dy = abs(y2 - y1) / (y2 - y1);
			int x = x1 - dx;
			int y = y1 - dy;
			for (int k=0; k < abs(x2 - x1) + 1; k++){
				x += dx;
				y += dy;
				field[x][y]++;
				if (field[x][y]==2){danger++;}
			}
		}
	}
	cout << danger << endl;

	return 0;
}