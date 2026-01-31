#include <iostream>
#include <gtsam/base/Vector.h>
#include <Eigen/Core>

int main() {
#ifdef GTSAM_EIGEN_VERSION_WORLD
  std::cout << "GTSAM_EIGEN_VERSION_WORLD = " << GTSAM_EIGEN_VERSION_WORLD << std::endl;
  std::cout << "GTSAM_EIGEN_VERSION_MAJOR = " << GTSAM_EIGEN_VERSION_MAJOR << std::endl;
#else
  std::cout << "GTSAM_EIGEN_VERSION_* not defined\n";
#endif

  std::cout << "EIGEN_WORLD_VERSION = " << EIGEN_WORLD_VERSION << std::endl;
  std::cout << "EIGEN_MAJOR_VERSION = " << EIGEN_MAJOR_VERSION << std::endl;
  std::cout << "EIGEN_MINOR_VERSION = " << EIGEN_MINOR_VERSION << std::endl;
}
