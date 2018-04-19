# Script generated with Bloom
pkgdesc="ROS - The jsk_rviz_plugins package"


pkgname='ros-kinetic-jsk-rviz-plugins'
pkgver='2.1.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-cv-bridge'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-geometry'
'ros-kinetic-jsk-footstep-msgs'
'ros-kinetic-jsk-gui-msgs'
'ros-kinetic-jsk-hark-msgs'
'ros-kinetic-jsk-recognition-msgs'
'ros-kinetic-jsk-recognition-utils'
'ros-kinetic-jsk-topic-tools'
'ros-kinetic-message-generation'
'ros-kinetic-mk'
'ros-kinetic-people-msgs'
'ros-kinetic-rosbuild'
'ros-kinetic-rviz'
'ros-kinetic-std-msgs'
'ros-kinetic-urdfdom-py'
'ros-kinetic-view-controller-msgs'
)

depends=('ros-kinetic-cv-bridge'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-geometry'
'ros-kinetic-jsk-footstep-msgs'
'ros-kinetic-jsk-gui-msgs'
'ros-kinetic-jsk-hark-msgs'
'ros-kinetic-jsk-recognition-msgs'
'ros-kinetic-jsk-recognition-utils'
'ros-kinetic-jsk-topic-tools'
'ros-kinetic-message-generation'
'ros-kinetic-people-msgs'
'ros-kinetic-rviz'
'ros-kinetic-std-msgs'
'ros-kinetic-urdfdom-py'
'ros-kinetic-view-controller-msgs'
)

conflicts=()
replaces=()

_dir=jsk_rviz_plugins
source=()
md5sums=()

prepare() {
    cp -R $startdir/jsk_rviz_plugins $srcdir/jsk_rviz_plugins
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

