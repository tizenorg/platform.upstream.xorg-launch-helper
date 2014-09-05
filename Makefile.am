
EXTRA_DIST = AUTHORS COPYING INSTALL

systemdsystemunitdir = @SYSTEMD_SYSTEMUNITDIR@
systemdsystemunit_DATA = display-manager.service display-manager-run.service

systemdsystemunit-install-hook:
	mkdir -p $(DESTDIR)$(systemdsystemunitdir)/graphical.target.wants
#	ln -sf ../xorg.service $(DESTDIR)$(systemduserunitdir)/xorg.target.wants/xorg.service

install-data-hook: systemdsystemunit-install-hook

AM_CFLAGS = $(LIBSYSTEMD_DAEMON_CFLAGS) -Wall -Wno-uninitialized

bin_PROGRAMS = xorg-launch-helper
xorg_launch_helper_SOURCES = src/main.c
xorg_launch_helper_LDADD = $(LIBSYSTEMD_DAEMON_LIBS)

