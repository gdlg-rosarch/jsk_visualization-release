# Script generated with Bloom
pkgdesc="ROS - jsk interactive markers"
url='http://ros.org/wiki/interactive_marker'

pkgname='ros-kinetic-jsk-interactive-marker'
pkgver='2.1.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-actionlib'
'ros-kinetic-catkin'
'ros-kinetic-cmake-modules'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-dynamic-tf-publisher'
'ros-kinetic-eigen-conversions'
'ros-kinetic-geometry-msgs'
'ros-kinetic-interactive-markers'
'ros-kinetic-jsk-footstep-msgs'
'ros-kinetic-jsk-recognition-msgs>=1.0.0'
'ros-kinetic-jsk-rviz-plugins'
'ros-kinetic-jsk-topic-tools'
'ros-kinetic-message-filters'
'ros-kinetic-message-generation'
'ros-kinetic-mk'
'ros-kinetic-moveit-msgs'
'ros-kinetic-rosbuild'
'ros-kinetic-roscpp'
'ros-kinetic-roseus'
'ros-kinetic-roslib'
'ros-kinetic-rviz'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
'ros-kinetic-tf-conversions'
'ros-kinetic-urdf'
'ros-kinetic-visualization-msgs'
'tinyxml'
'yaml-cpp'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-dynamic-tf-publisher'
'ros-kinetic-eigen-conversions'
'ros-kinetic-geometry-msgs'
'ros-kinetic-interactive-markers'
'ros-kinetic-jsk-footstep-msgs'
'ros-kinetic-jsk-recognition-msgs>=1.0.0'
'ros-kinetic-jsk-rviz-plugins'
'ros-kinetic-jsk-topic-tools'
'ros-kinetic-message-filters'
'ros-kinetic-message-runtime'
'ros-kinetic-moveit-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-roseus'
'ros-kinetic-roslib'
'ros-kinetic-rviz'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
'ros-kinetic-tf-conversions'
'ros-kinetic-urdf'
'ros-kinetic-visualization-msgs'
'tinyxml'
'yaml-cpp'
)

conflicts=()
replaces=()

_dir=jsk_interactive_marker
source=()
md5sums=()

prepare() {
    cp -R $startdir/jsk_interactive_marker $srcdir/jsk_interactive_marker
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

