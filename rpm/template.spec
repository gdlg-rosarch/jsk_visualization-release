Name:           ros-jade-jsk-visualization
Version:        2.1.0
Release:        0%{?dist}
Summary:        ROS jsk_visualization package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_visualization
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-jsk-interactive
Requires:       ros-jade-jsk-interactive-marker
Requires:       ros-jade-jsk-interactive-test
Requires:       ros-jade-jsk-rqt-plugins
Requires:       ros-jade-jsk-rviz-plugins
BuildRequires:  ros-jade-catkin

%description
Metapackage that contains visualization package for jsk-ros-pkg

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon Feb 13 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.1.0-0
- Autogenerated by Bloom

* Thu Dec 15 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

* Wed Dec 14 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.0-0
- Autogenerated by Bloom

* Thu Sep 29 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.34-0
- Autogenerated by Bloom

* Wed Sep 21 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.33-0
- Autogenerated by Bloom

