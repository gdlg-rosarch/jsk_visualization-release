Name:           ros-hydro-jsk-interactive-marker
Version:        1.0.18
Release:        0%{?dist}
Summary:        ROS jsk_interactive_marker package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/interactive_marker
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-actionlib
Requires:       ros-hydro-dynamic-reconfigure
Requires:       ros-hydro-dynamic-tf-publisher
Requires:       ros-hydro-eigen-conversions
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-interactive-markers
Requires:       ros-hydro-jsk-footstep-msgs
Requires:       ros-hydro-jsk-pcl-ros
Requires:       ros-hydro-jsk-recognition-msgs
Requires:       ros-hydro-jsk-rviz-plugins
Requires:       ros-hydro-jsk-topic-tools
Requires:       ros-hydro-message-filters
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-roseus
Requires:       ros-hydro-roslib
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-tf
Requires:       ros-hydro-tf-conversions
Requires:       ros-hydro-urdf
Requires:       ros-hydro-visualization-msgs
Requires:       tinyxml-devel
BuildRequires:  ros-hydro-actionlib
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-dynamic-tf-publisher
BuildRequires:  ros-hydro-eigen-conversions
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-interactive-markers
BuildRequires:  ros-hydro-jsk-footstep-msgs
BuildRequires:  ros-hydro-jsk-pcl-ros
BuildRequires:  ros-hydro-jsk-recognition-msgs
BuildRequires:  ros-hydro-jsk-rviz-plugins
BuildRequires:  ros-hydro-jsk-topic-tools
BuildRequires:  ros-hydro-message-filters
BuildRequires:  ros-hydro-mk
BuildRequires:  ros-hydro-rosbuild
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-roseus
BuildRequires:  ros-hydro-roslib
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-tf
BuildRequires:  ros-hydro-tf-conversions
BuildRequires:  ros-hydro-urdf
BuildRequires:  ros-hydro-visualization-msgs
BuildRequires:  tinyxml-devel

%description
jsk interactive markers

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Jan 30 2015 furuta <furuta@jsk.t.u-tokyo.ac.jp> - 1.0.18-0
- Autogenerated by Bloom

* Thu Jan 29 2015 furuta <furuta@jsk.t.u-tokyo.ac.jp> - 1.0.17-0
- Autogenerated by Bloom

* Sun Jan 04 2015 furuta <furuta@jsk.t.u-tokyo.ac.jp> - 1.0.16-0
- Autogenerated by Bloom

* Sun Dec 21 2014 furuta <furuta@jsk.t.u-tokyo.ac.jp> - 1.0.15-0
- Autogenerated by Bloom

* Wed Dec 10 2014 furuta <furuta@jsk.t.u-tokyo.ac.jp> - 1.0.14-0
- Autogenerated by Bloom

