#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

struct Rect {
  double x, y;
  double width;
  double length;
};

bool checkCollision(
    Rect truck, vector<Rect>& obstacles) {  // check for a collision in general
  for (const auto& obs : obstacles) {
    if (abs(truck.x - obs.x) <= (truck.width + obs.width) / 2 &&
        abs(truck.y - obs.y) <= (truck.length + obs.length) / 2) {
      return true;
    }
  }
  return false;
}

int main() {
  vector<Rect> obstacles = {
      {2.0, 5.0, 2.0, 2.0}, {6.0, 5.0, 2.0, 2.0}, {10.0, 5.0, 2.0, 2.0}};
  Rect truck = {5.0, 5.0, 2.0, 4.0};
  cout << checkCollision(truck, obstacles);

  return 0;
}