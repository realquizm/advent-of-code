#include <iostream>
#include "pong.hpp"
#include <chrono>

using std::chrono::duration_cast;
using std::chrono::milliseconds;
using std::chrono::steady_clock;

int main() {

  // Part one
  auto begin = steady_clock::now();

  Pong pong = Pong(std::string(SOURCE_DIR)+"/data/input.csv");
  int part_one = pong.render_map();

  auto end = steady_clock::now();
  std::cout << "Solution to part one: " << part_one << " ";
  std::cout << "(time taken " << 
      duration_cast<milliseconds>(end - begin).count() << "[ms])\n";

  // Part two
  begin = steady_clock::now();

  Pong playPong = Pong(std::string(SOURCE_DIR) + "/data/input.csv", true);
  int part_two = playPong.play();
  
  end = steady_clock::now();
  std::cout << "Solution to part two: " << part_two << " ";
  std::cout << "(time taken " << 
      duration_cast<milliseconds>(end - begin).count() << "[ms])\n";

  return 0;
}