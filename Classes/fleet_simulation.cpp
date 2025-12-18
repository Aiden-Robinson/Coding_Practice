#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

// Classes for 1D collision of trucks
class Truck {
 private:
  double position, velocity, length;

 public:
  Truck(double length) {
    this->length = length;
    position = 0.0;
    velocity = 0.0;
  }

  double getPosition() const {
    return position;
  }  // const means the function promises not to modify the val

  double getVelocity() const { return velocity; }
  double getLength() const { return length; }

  void applyCommand(double acceleration, double duration) {
    double v0 = velocity;  // save velocity at the start of the command
    velocity = velocity + acceleration * duration;
    position = position + v0 * duration;
  }
};

class Fleet {
 private:
  vector<Truck> trucks;

 public:
  void addTruck(const Truck& truck) {  // adds to our class list of trucks
    trucks.push_back(truck);
  }

  void simulateStep(double acceleration, double dt) {
    for (int i = 0; i < trucks.size(); i++) {
      trucks[i].applyCommand(acceleration, dt);
    }
  }

  bool checkCollision() const {
    for (int i = 0; i < trucks.size(); i++) {
      for (int j = i + 1; j < trucks.size(); j++) {
        double pos1 = trucks[i].getPosition();
        double pos2 = trucks[j].getPosition();
        double len1 = trucks[i].getLength();
        double len2 = trucks[j].getLength();
        if (abs(pos1 - pos2) <= (len1 + len2) / 2.0) {
          return true;  // Collision detected!
        }
      }
    }
    return false;
  }
};

int main() {
  Truck t1(4.0);
  Truck t2(4.0);

  Fleet fleet;
  fleet.addTruck(t1);
  fleet.addTruck(t2);

  for (double t = 0.0; t < 3.0; t += 0.1) {
    fleet.simulateStep(2, 0.1);  // time step it with 0.1
    if (fleet.checkCollision()) {
      cout << "there is a collision";
      break;
    }
  }

  return 0;
}
