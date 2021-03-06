Name:		xorg-launch-helper
Version:	4
Release:	0
Summary:	Xorg service helper

Group:		Graphics/X Window System
License:	GPL-2.0
URL:		http://foo-projects.org/~sofar/%{name}
#X-Vc-Url:	https://github.com/sofar/xorg-launch-helper.git
Source0:	http://foo-projects.org/~sofar/%{name}/%{name}-%{version}.tar.gz
Source1:	xorg.conf
Source2:	xorg_done.service
Source1001: 	xorg-launch-helper.manifest

BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(libsystemd-daemon)
Requires:	/usr/bin/Xorg

%description
A wrapper to launch Xorg as a service in systemd environments.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%reconfigure
%__make %{?_smp_mflags}


%install
%make_install

# temoprary HW configuration. it should be seperated.
mkdir -p %{buildroot}/etc/sysconfig
install -m 644 %{SOURCE1} %{buildroot}/etc/sysconfig/xorg
install -m 0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/systemd/user/
ln -sf ../xorg_done.service %{buildroot}%{_prefix}/lib/systemd/user/xorg.target.wants

# "-sharevt" option will be removed (only) for Tizen Emulator temporarily
# by the request from Tizen SDK (kernel) team.
%if 0%{?simulator}
sed -i 's/-sharevts//g' %{buildroot}/etc/sysconfig/xorg
%endif

%files
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root,-)
%{_bindir}/xorg-launch-helper
%{_prefix}/lib/systemd/user/xorg.service
%{_prefix}/lib/systemd/user/xorg_done.service
%{_prefix}/lib/systemd/user/xorg.target
%{_prefix}/lib/systemd/user/xorg.target.wants/xorg.service
%{_prefix}/lib/systemd/user/xorg.target.wants/xorg_done.service
/etc/sysconfig/xorg
