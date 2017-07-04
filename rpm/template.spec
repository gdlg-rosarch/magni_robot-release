Name:           ros-kinetic-magni-demos
Version:        0.1.1
Release:        0%{?dist}
Summary:        ROS magni_demos package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-magni-bringup
Requires:       ros-kinetic-magni-nav
Requires:       ros-kinetic-magni-teleop
Requires:       ros-kinetic-rosbridge-server
Requires:       ros-kinetic-tf2-web-republisher
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-magni-bringup
BuildRequires:  ros-kinetic-magni-nav
BuildRequires:  ros-kinetic-magni-teleop
BuildRequires:  ros-kinetic-rosbridge-server
BuildRequires:  ros-kinetic-tf2-web-republisher

%description
The magni_demos package

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
* Tue Jul 04 2017 Rohan Agrawal <send2arohan@gmail.com> - 0.1.1-0
- Autogenerated by Bloom

* Sat Jun 17 2017 Rohan Agrawal <send2arohan@gmail.com> - 0.1.0-0
- Autogenerated by Bloom

