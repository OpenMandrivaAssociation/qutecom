%define oversion RC2
%define mercurial 20081207

Name:		qutecom
Version:	2.2
Release:	%mkrel 0.%oversion.%mercurial.3
Summary:	Internet phone software
License:	GPLv2+
Group:		Networking/Instant messaging
URL:		http://www.qutecom.com
Source:		http://www.qutecom.com/downloads/qutecom-%version-hg%mercurial.tar.bz2
Patch1:		%name-2.2-fix-desktopfile.patch
Patch2:     %name-2.2-fix-build.patch
Patch3:     qutecom-2.2-fix-build-x86-64.patch
Patch4:     qutecom-2.2-fix-install.patch
Patch5:     qutecom-2.2-fix-quotes.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	speex-devel
BuildRequires:	boost-devel
BuildRequires:	portaudio-devel >= 19
BuildRequires:	openssl-devel
BuildRequires:	glib2-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	e2fsprogs-devel
BuildRequires:	gnutls-devel
BuildRequires:	qt4-linguist
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	curl-devel
BuildRequires:	desktop-file-utils
BuildRequires:	python-devel
Obsoletes:	openwengo
Obsoletes:	wengophone
Provides:	wengophone
Obsoletes:	%mklibname %{name} 0

%description
QuteCom is a SIP softphone which allows you to make free PC to PC
video and voice calls, and to integrate all your IM contacts in one
place.

%files
%doc wengophone/AUTHORS
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libdir}/wengophone
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*.png

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p1

%build
mkdir build_openwengo
cd build_openwengo
  /usr/bin/cmake .. \
  %if "%_lib" != "lib"
    -DLIB_SUFFIX=64 \
  %endif
  -DCMAKE_INSTALL_PREFIX=/usr \
  -DDBUS_SERVICES_DIR=/usr/share/dbus-1/services \
  -DDBUS_INTERFACES_DIR=/usr/share/dbus-1/interfaces

%make

%install
rm -rf $RPM_BUILD_ROOT
cd build_openwengo
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT
