Summary:	Ted - easy rich text processor
Summary(pl):	Ted - prosty procesor tekstu
Name:		ted
Version:	2.10
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Group(de):	X11/Applikationen/Editors
Group(pl):	X11/Aplikacje/Edytory
Group(pt):	X11/Aplicações/Editores
Source0:	ftp://ftp.nluug.nl/pub/editors/%{name}/%{name}-%{version}.src.tar.gz
Patch0:		%{name}-libpng.patch
Patch1:		%{name}-paths.patch
Patch2:		%{name}-print-segv.patch
URL:		http://www.nllgg.nl/Ted/
BuildRequires:	autoconf
BuildRequires:	XFree86-devel >= 4.0
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	motif-devel
#BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Ted is a text processor running under X Window on Unix/Linux systems.
It was made to edit rich text documents on Unix/Linux in a WYSIWYG
way. It can edit MS RTF files and print to PostScript.

%description -l pl
Ted jest procesorem tekstu dzia³aj±cym pod X Window pod unices. S³u¿y
do edycji dokumentów tekstowych w stylu WYSIWYG. Mo¿e obrabiaæ pliki w
formacie MS RTF i drukowaæ w PostScripcie.

%prep
%setup -q -n Ted-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
for d in bitmap ind libreg appUtil appFrame Ted; do
	cd $d
	autoconf
	%configure --with-MOTIF
	cd ..
done
%{__make} compile.shared
##mv -f Ted/Ted Ted.motif

# gtk part commented out - gtk port is not complete!
##for d in appFrame Ted; do
##	cd $d
##	rm -f *.o
##	%%configure --with-GTK
##	cd ..
##done
##%{__make} compile.shared

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/Ted/{afm,ind}}

(cd tedPackage ; tar xf TedBindist.tar)

##install Ted.motif $RPM_BUILD_ROOT%{_bindir}
##install Ted/Ted $RPM_BUILD_ROOT%{_bindir}/Ted.gtk
install Ted/Ted $RPM_BUILD_ROOT%{_bindir}
install tedPackage/afm/* $RPM_BUILD_ROOT%{_datadir}/Ted/afm
install tedPackage/ind/* $RPM_BUILD_ROOT%{_datadir}/Ted/ind
install tedPackage/info/TedDocument.rtf $RPM_BUILD_ROOT%{_datadir}/Ted

gzip -9nf README tedPackage/rdm.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz tedPackage/rdm.txt.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/Ted
