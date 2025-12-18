#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

struct Command {
  double acceleration;  // m/s^2
  double duration;      // seconds
};

std::pair<double, double> simulate(const std::vector<Command>& commands) {
  double position = 0.0;
  double velocity = 0.0;

  for (const auto& cmd : commands) {
    double v0 = velocity;  // save velocity at the start of the command
    velocity = velocity + cmd.acceleration * cmd.duration;
    position = position + v0 * cmd.duration +
               0.5 * cmd.acceleration * (std::pow(cmd.duration, 2));
  }

  return {position, velocity};
}

int main() {
  std::vector<Command> commands = {
      // vector of command
      {2.0, 3.0},  // accelerate 2 m/s^2 for 3 seconds
      {0.0, 2.0},  // coast for 2 seconds
      {-1.0, 4.0}  // decelerate -1 m/s^2 for 4 seconds
  };
  std::pair<double, double> result = simulate(commands);
  cout << "position: " << result.first << " velocity: " << result.second;

  return 0;
}
