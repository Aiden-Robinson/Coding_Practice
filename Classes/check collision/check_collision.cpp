#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

bool checkCollision(
    double truckPosition, double truckLength,
    vector<double>& obstacles) {  // check for a collision in general

  for (const auto& ob : obstacles) {
    if (abs(ob - truckPosition) <= truckLength / 2) {
      return true;
    }
  }
  return false;
}

int main() {
  vector<double> obstacles = {2.0, 6.0, 10.0};
  cout << checkCollision(5.0, 4.0, obstacles);

  return 0;
}