%define oversion RC1
Name:		qutecom
Version:	2.2
Release:	%mkrel 0.%oversion.1
Summary:	Internet phone software
License:	GPLv2+
Group:		Networking/Instant messaging
URL:		http://www.qutecom.com
Source:		http://www.qutecom.com/downloads/qutecom-%version-%oversion.tar.gz
Patch1:		wengophone-2.1.99.1-fix-desktopfile.patch
Patch2:         wengophone-2.2-fix-ffmpeg-cmake.patch
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
Obsoletes:	%mklibname %{name} 0

%description
Wengophone is a SIP softphone which allows you to make free PC to PC
video and voice calls, and to integrate all your IM contacts in one
place.

%files
%doc wengophone/AUTHORS
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*.png

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version-%oversion
%patch2 -p0

%build
%cmake_qt4 

%make VERBOSE=1
make lupdate VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT
cd build
%makeinstall_std

rm -f %{buildroot}%{_datadir}/wengophone/COPYING %{buildroot}%{_datadir}/wengophone/AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT
