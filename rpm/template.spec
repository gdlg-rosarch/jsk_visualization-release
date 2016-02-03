Name:           ros-indigo-jsk-rviz-plugins
Version:        1.0.28
Release:        0%{?dist}
Summary:        ROS jsk_rviz_plugins package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-image-geometry
Requires:       ros-indigo-jsk-footstep-msgs
Requires:       ros-indigo-jsk-gui-msgs
Requires:       ros-indigo-jsk-hark-msgs
Requires:       ros-indigo-jsk-recognition-msgs
Requires:       ros-indigo-jsk-recognition-utils
Requires:       ros-indigo-jsk-topic-tools
Requires:       ros-indigo-message-generation
Requires:       ros-indigo-people-msgs
Requires:       ros-indigo-roseus
Requires:       ros-indigo-rviz
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-urdfdom-py
Requires:       ros-indigo-view-controller-msgs
Requires:       wxGTK-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-image-geometry
BuildRequires:  ros-indigo-jsk-footstep-msgs
BuildRequires:  ros-indigo-jsk-gui-msgs
BuildRequires:  ros-indigo-jsk-hark-msgs
BuildRequires:  ros-indigo-jsk-recognition-msgs
BuildRequires:  ros-indigo-jsk-recognition-utils
BuildRequires:  ros-indigo-jsk-topic-tools
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-mk
BuildRequires:  ros-indigo-people-msgs
BuildRequires:  ros-indigo-rosbuild
BuildRequires:  ros-indigo-roseus
BuildRequires:  ros-indigo-rviz
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-urdfdom-py
BuildRequires:  ros-indigo-view-controller-msgs
BuildRequires:  wxGTK-devel

%description
The jsk_rviz_plugins package

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
* Wed Feb 03 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.28-0
- Autogenerated by Bloom

* Tue Dec 08 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.27-0
- Autogenerated by Bloom

* Mon Dec 07 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.26-0
- Autogenerated by Bloom

* Tue Oct 13 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.25-0
- Autogenerated by Bloom

* Tue Sep 08 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.24-0
- Autogenerated by Bloom

* Wed Jul 15 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.23-0
- Autogenerated by Bloom

* Wed Jun 24 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.22-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.21-1
- Autogenerated by Bloom

* Fri Jun 19 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.21-0
- Autogenerated by Bloom

* Mon May 04 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.20-0
- Autogenerated by Bloom

* Thu Apr 09 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.19-0
- Autogenerated by Bloom

* Fri Jan 30 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.18-1
- Autogenerated by Bloom

* Fri Jan 30 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.18-0
- Autogenerated by Bloom

