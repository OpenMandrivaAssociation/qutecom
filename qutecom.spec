%define oversion RC3
%define mercurial 20090825

Name:		qutecom
Version:	2.2
Release:	%mkrel 0.%oversion.4
Summary:	Internet phone software
License:	GPLv2+
Group:		Networking/Instant messaging
URL:		http://www.qutecom.com
Source:		http://www.qutecom.com/downloads/qutecom-%version.%mercurial.tar.bz2
Patch1:		qutecom_googlebreakpad_64.patch
Patch2:     qutecom_pixertool_ffmpeg.patch 
Patch3:     qutecom_presentation_install.patch 
Patch4:     qutecom_wifo_phapi.patch 
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
BuildRequires:  libuuid-devel
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
%{_libdir}/%name
%{_datadir}/applications/%{name}.desktop
%{_libdir}/pm-utils/sleep.d/70QuteCom
%{_iconsdir}/hicolor/*/apps/*.png

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version

#%patch1 -p1
#%patch2 -p1
#%patch3 -p1
#%patch4 -p1

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
rm -rf %{buildroot}
cd build_openwengo
%makeinstall_std

%clean
rm -rf %{buildroot}
