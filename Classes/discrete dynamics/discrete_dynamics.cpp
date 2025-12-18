#include <iostream>
#include <vector>

using namespace std;

struct Command {
  double acceleration;
  double duration;
};

std::pair<double, double> simulate(std::vector<Command>& commands) {
  double dt = 0.1;
  double position = 0.0;
  double velocity = 0.0;

  for (auto& cmd : commands) {
    int steps = cmd.duration / dt;
    for (int i = 0; i < steps; i++) {
      velocity += cmd.acceleration * dt;
      position += velocity * dt;
    }
  }

  return {position, velocity};
}

int main() {
  std::vector<Command> commands = {{2.0, 3.0},
                                   {0.0, 2.0},  // coast for 2 seconds
                                   {-1.0, 4.0}};

  std::pair<double, double> result = simulate(commands);
  cout << result.first << " : " << result.second;

  return 0;
}