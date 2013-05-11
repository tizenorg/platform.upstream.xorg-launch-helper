Name:		xorg-launch-helper
Version:	4
Release:	1
Summary:	Xorg service helper

Group:		Graphics/X Window System
License:	GPL-2.0
URL:		http://foo-projects.org/~sofar/%{name}
Source0:	http://foo-projects.org/~sofar/%{name}/%{name}-%{version}.tar.gz
Source1:	xorg.conf
Source2:	xorg_done.service

BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(libsystemd-daemon)
Requires:	/usr/bin/Xorg

%description
A wrapper to launch Xorg as a service in systemd environments.

%prep
%setup -q

%build
%reconfigure
make %{?_smp_mflags}


%install
%make_install

# temoprary HW configuration. it should be seperated.
mkdir -p %{buildroot}/etc/sysconfig
install -m 644 %{SOURCE1} %{buildroot}/etc/sysconfig/xorg
install -m 0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/systemd/user/
ln -sf ../xorg_done.service %{buildroot}%{_prefix}/lib/systemd/user/xorg.target.wants

%files
%license COPYING
%defattr(-,root,root,-)
%{_bindir}/xorg-launch-helper
%{_prefix}/lib/systemd/user/xorg.service
%{_prefix}/lib/systemd/user/xorg_done.service
%{_prefix}/lib/systemd/user/xorg.target
%{_prefix}/lib/systemd/user/xorg.target.wants/xorg.service
%{_prefix}/lib/systemd/user/xorg.target.wants/xorg_done.service
/etc/sysconfig/xorg
