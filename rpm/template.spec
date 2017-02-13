Name:           ros-kinetic-jsk-rviz-plugins
Version:        2.1.0
Release:        3%{?dist}
Summary:        ROS jsk_rviz_plugins package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-diagnostic-msgs
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-image-geometry
Requires:       ros-kinetic-jsk-footstep-msgs
Requires:       ros-kinetic-jsk-gui-msgs
Requires:       ros-kinetic-jsk-hark-msgs
Requires:       ros-kinetic-jsk-recognition-msgs
Requires:       ros-kinetic-jsk-recognition-utils
Requires:       ros-kinetic-jsk-topic-tools
Requires:       ros-kinetic-message-generation
Requires:       ros-kinetic-people-msgs
Requires:       ros-kinetic-rviz
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-urdfdom-py
Requires:       ros-kinetic-view-controller-msgs
Requires:       wxGTK-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cv-bridge
BuildRequires:  ros-kinetic-diagnostic-msgs
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-image-geometry
BuildRequires:  ros-kinetic-jsk-footstep-msgs
BuildRequires:  ros-kinetic-jsk-gui-msgs
BuildRequires:  ros-kinetic-jsk-hark-msgs
BuildRequires:  ros-kinetic-jsk-recognition-msgs
BuildRequires:  ros-kinetic-jsk-recognition-utils
BuildRequires:  ros-kinetic-jsk-topic-tools
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-mk
BuildRequires:  ros-kinetic-people-msgs
BuildRequires:  ros-kinetic-rosbuild
BuildRequires:  ros-kinetic-rviz
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-urdfdom-py
BuildRequires:  ros-kinetic-view-controller-msgs
BuildRequires:  wxGTK-devel

%description
The jsk_rviz_plugins package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Feb 13 2017 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.1.0-3
- Autogenerated by Bloom

