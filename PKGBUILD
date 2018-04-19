# Script generated with Bloom
pkgdesc="ROS - The jsk_rqt_plugins package"


pkgname='ros-kinetic-jsk-rqt-plugins'
pkgver='2.1.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-image-view2'
'ros-kinetic-message-generation'
'ros-kinetic-mk'
'ros-kinetic-rosbuild'
)

depends=('ros-kinetic-cv-bridge'
'ros-kinetic-image-view2'
'ros-kinetic-message-runtime'
'ros-kinetic-qt-gui-py-common'
'ros-kinetic-resource-retriever'
'ros-kinetic-rqt-gui'
'ros-kinetic-rqt-gui-py'
'ros-kinetic-rqt-image-view'
'ros-kinetic-rqt-plot'
'urlgrabber'
)

conflicts=()
replaces=()

_dir=jsk_rqt_plugins
source=()
md5sums=()

prepare() {
    cp -R $startdir/jsk_rqt_plugins $srcdir/jsk_rqt_plugins
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

