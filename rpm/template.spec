Name:           ros-jade-jsk-rviz-plugins
Version:        2.0.0
Release:        0%{?dist}
Summary:        ROS jsk_rviz_plugins package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-cv-bridge
Requires:       ros-jade-diagnostic-msgs
Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-image-geometry
Requires:       ros-jade-jsk-footstep-msgs
Requires:       ros-jade-jsk-gui-msgs
Requires:       ros-jade-jsk-hark-msgs
Requires:       ros-jade-jsk-recognition-msgs
Requires:       ros-jade-jsk-recognition-utils
Requires:       ros-jade-jsk-topic-tools
Requires:       ros-jade-message-generation
Requires:       ros-jade-people-msgs
Requires:       ros-jade-rviz
Requires:       ros-jade-std-msgs
Requires:       ros-jade-urdfdom-py
Requires:       ros-jade-view-controller-msgs
Requires:       wxGTK-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cv-bridge
BuildRequires:  ros-jade-diagnostic-msgs
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-image-geometry
BuildRequires:  ros-jade-jsk-footstep-msgs
BuildRequires:  ros-jade-jsk-gui-msgs
BuildRequires:  ros-jade-jsk-hark-msgs
BuildRequires:  ros-jade-jsk-recognition-msgs
BuildRequires:  ros-jade-jsk-recognition-utils
BuildRequires:  ros-jade-jsk-topic-tools
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-mk
BuildRequires:  ros-jade-people-msgs
BuildRequires:  ros-jade-rosbuild
BuildRequires:  ros-jade-rviz
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-urdfdom-py
BuildRequires:  ros-jade-view-controller-msgs
BuildRequires:  wxGTK-devel

%description
The jsk_rviz_plugins package

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
* Wed Dec 14 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.0-0
- Autogenerated by Bloom

* Thu Sep 29 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.34-0
- Autogenerated by Bloom

* Wed Sep 21 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.33-0
- Autogenerated by Bloom

