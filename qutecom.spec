Name:		qutecom
Version:	2.2
Release:	%mkrel 3
Summary:	Internet phone software
License:	GPLv2+
Group:		Networking/Instant messaging
URL:		http://www.qutecom.com
Source:		http://www.qutecom.com/downloads/qutecom-%version.tar.xz
Patch0:		qutecom-2.2-fix-link.patch
Patch1:		qutecom-2.2-fix-str-fmt.patch
Patch2:		qutecom-2.2-fix-install-perm.patch
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
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libdir}/%name
%{_datadir}/applications/%{name}.desktop
%attr(0755,root,root) %{_libdir}/pm-utils/sleep.d/70QuteCom
%{_iconsdir}/hicolor/*/apps/*.png
#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
cd build
cmake .. \
        -DCMAKE_INSTALL_PREFIX:PATH=/usr \
        -DCMAKE_INSTALL_LIBDIR:PATH=/usr/lib \
        -DLIB_INSTALL_DIR:PATH=/usr/lib \
        -DENABLE_CRASHREPORT=OFF \
        -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
        -DCMAKE_INSTALL_RPATH=%{_libdir}/qutecom
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %{buildroot}
