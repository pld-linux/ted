Summary:	An easy Rich Text Processor
Summary(pl):	£atwy w obs³udze procesor RTF
Name:		ted
Version:	2.10
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.nluug.nl/pub/editors/ted/%{name}-%{version}.src.tar.gz
Source1:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_en_GB.tar.gz
Source2:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_pl_PL.tar.gz
Patch0:		ftp://ftp.debian.org/debian/pool/main/t/ted/%{name}_2.10-3.diff.gz
URL:		http://www.nllgg.nl/Ted/
BuildRequires:	motif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libpng-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11

%description
Ted is an easy rich text processor. It can edit RTF files in a wysiwyg
manner. It supports multiple fonts and can print to PostScript
printers.

Ted consists of a general part: The program, something.afm files and
an American spelling checker. Additional packages with spell checking
dictionaries for different languages exist.

%description -l pl
Ten jest ³atwym procesorem tekstu (RTF). Mo¿e on edytowaæ pliki RTF w
sposób wysiwyg. Wspiera wiele fontów oraz mo¿e drukowaæ na drukarkach
PostScriptowych.

%prep
%setup -q -n Ted-%{version} -a1 -a2
%patch0 -p1

%build
CC="%{__cc}"; export CC
CFLAGS="%{rpmcflags}"; export CFLAGS

%{__make} \
	CONFIGURE_OPTIONS="--prefix=%{_prefix} --with-MOTIF" \
	compile.shared

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/%{name}}

install Ted/Ted $RPM_BUILD_ROOT%{_bindir}/%{name}
install ind/*.ind $RPM_BUILD_ROOT%{_libdir}/%{name}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
