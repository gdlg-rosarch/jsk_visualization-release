Name:           ros-indigo-jsk-visualization
Version:        1.0.24
Release:        0%{?dist}
Summary:        ROS jsk_visualization package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_visualization
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-jsk-interactive
Requires:       ros-indigo-jsk-interactive-marker
Requires:       ros-indigo-jsk-interactive-test
Requires:       ros-indigo-jsk-rqt-plugins
Requires:       ros-indigo-jsk-rviz-plugins
BuildRequires:  ros-indigo-catkin

%description
Metapackage that contains visualization package for jsk-ros-pkg

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Sep 08 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.24-0
- Autogenerated by Bloom

* Wed Jul 15 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.23-0
- Autogenerated by Bloom

* Wed Jun 24 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.22-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.21-1
- Autogenerated by Bloom

* Fri Jun 19 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.21-0
- Autogenerated by Bloom

* Mon May 04 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.20-0
- Autogenerated by Bloom

