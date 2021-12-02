#include <iostream>
#include <string>
#include <fstream>
#include <sstream>


using namespace std;

int main() {
	ifstream inp("inputs/02");

	string dir;
	int cnt;
	int pos[4] = {0, 0, 0, 0};
	int aim = 0;
	while (inp >> dir >> cnt){
		if (dir[0] == 'f'){
			pos[0] += cnt;
			pos[2] += cnt;
			pos[3] += aim * cnt;
		} else if (dir[0] == 'd'){
			pos[1] += cnt;
			aim += cnt;
		} else {
			pos[1] -= cnt;
			aim -= cnt;
		}
	}
	cout << pos[0] * pos[1] << endl;
	cout << pos[2] * pos[3] << endl;

	return 0;
}