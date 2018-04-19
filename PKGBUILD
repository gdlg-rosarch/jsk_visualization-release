# Script generated with Bloom
pkgdesc="ROS - <p>Metapackage that contains visualization package for jsk-ros-pkg</p>"
url='http://ros.org/wiki/jsk_visualization'

pkgname='ros-kinetic-jsk-visualization'
pkgver='2.1.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-jsk-interactive'
'ros-kinetic-jsk-interactive-marker'
'ros-kinetic-jsk-interactive-test'
'ros-kinetic-jsk-rqt-plugins'
'ros-kinetic-jsk-rviz-plugins'
)

conflicts=()
replaces=()

_dir=jsk_visualization
source=()
md5sums=()

prepare() {
    cp -R $startdir/jsk_visualization $srcdir/jsk_visualization
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

