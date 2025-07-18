Summary:	TRM id generator
Summary(pl.UTF-8):	Generator identyfikatorów TRM
Name:		trm
Version:	0.2.1
Release:	2
License:	GPL
Group:		Applications/Sound
Source0:	ftp://ftp.musicbrainz.org/pub/musicbrainz/%{name}-%{version}.tar.gz
# Source0-md5:	3f7e6c30cb91429313ca1a27df47e8bc
Patch0:		%{name}-gcc4.patch
URL:		http://www.musicbrainz.org/products/trmgen/download.html
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libmusicbrainz-devel >= 2.1.0
BuildRequires:	libvorbis-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The trm program will decode the first 30 seconds of audio file and
then spit out a TRM id (see http://www.relatable.com/ for details) on
stdout.

%description -l pl.UTF-8
Program trm dekoduje pierwsze 30 sekund pliku dźwiękowego i wypisuje
jego identyfikator TRM (opisany na http://www.relatable.com/).

%prep
%setup -q
%patch -P0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install trm $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
