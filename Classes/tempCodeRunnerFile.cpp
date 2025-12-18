#include <iostream>
#include <vector>
using namespace std;

struct Command {
  double acceleration;  // m/s^2
  double duration;      // seconds
};

std::pair<double, double> simulate(const std::vector<Command>& commands);

int main() {
  std::vector<Command> commands = {
      {2.0, 3.0},  // accelerate 2 m/s^2 for 3 seconds
      {0.0, 2.0},  // coast for 2 seconds
      {-1.0, 4.0}  // decelerate -1 m/s^2 for 4 seconds
  };
  cout << "Hello, World ass!" << endl;
  return 0;
}