Summary:	Ted - easy rich text processor
Summary(pl):	Ted - prosty procesor tekstu
Name:		ted
Version:	2.12
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	ftp://ftp.nluug.nl/pub/editors/%{name}/%{name}-%{version}.src.tar.gz
Source1:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_cs_CZ.tar.gz
Source2:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_da_DK.tar.gz
Source3:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_de_DE.tar.gz
Source4:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_en_GB.tar.gz
Source5:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_es_ES.tar.gz
Source6:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_fr_FR.tar.gz
Source7:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_hu_HU.tar.gz
Source8:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_it_IT.tar.gz
Source9:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_nl_NL.tar.gz
Source10:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_no_NO.tar.gz
Source11:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_pl_PL.tar.gz
Source12:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_pt_PT.tar.gz
Source13:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_ru_RU.tar.gz
Source14:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_sk_SK.tar.gz
Source15:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_sl_SI.tar.gz
Source16:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_sv_SE.tar.gz
Source17:	Ted.ad.pl_PL
Patch0:		%{name}-paths.patch
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

%package spelling-cs
Summary:	Czech spelling dictionary for Ted
Summary(pl):	Czeski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}

%description spelling-cs
Czech (cs_CZ) spelling dictionary for Ted.

%description spelling-cs -l pl
Czeski (cs_CZ) s³ownik ortograficzny dla Teda.

%package spelling-da
Summary:	Danish spelling dictionary for Ted
Summary(pl):	Duñski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}

%description spelling-da
Danish (da_DK) spelling dictionary for Ted.

%description spelling-da -l pl
Duñski (da_DK) s³ownik ortograficzny dla Teda.

%package spelling-de
Summary:	German spelling dictionary for Ted
Summary(pl):	Niemiecki s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}

%description spelling-de
German (de_DE) spelling dictionary for Ted.

%description spelling-da -l pl
Niemiecki (de_DE) s³ownik ortograficzny dla Teda.

%package spelling-en_GB
Summary:	English (UK) spelling dictionary for Ted
Summary(pl):	Angielski (brytyjski) s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}

%description spelling-en_GB
English (UK - en_GB) spelling dictionary for Ted.

%description spelling-en_GB -l pl
Angielski (brytyjski - en_GB) s³ownik ortograficzny dla Teda.

%package spelling-en_US
Summary:	English (US) spelling dictionary for Ted
Summary(pl):	Angielski (amerykañski) s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}

%description spelling-en_US
English (en_US) spelling dictionary for Ted.

%description spelling-en_US -l pl
Angielski (amerykañski - en_US) s³ownik ortograficzny dla Teda.

%package spelling-es
Summary:	Spanish spelling dictionary for Ted
Summary(pl):	Hiszpañski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}

%description spelling-es
Spanish (es_ES) spelling dictionary for Ted.

%description spelling-es -l pl
Hiszpañski (es_ES) s³ownik ortograficzny dla Teda.

%package spelling-fr
Summary:	French spelling dictionary for Ted
Summary(pl):	Francuski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}

%description spelling-fr
French (fr_FR) spelling dictionary for Ted.

%description spelling-fr -l pl
Francuski (fr_FR) s³ownik ortograficzny dla Teda.

%package spelling-it
Summary:	Italian spelling dictionary for Ted
Summary(pl):	W³oski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}

%description spelling-it
Italian (it_IT) spelling dictionary for Ted.

%description spelling-it -l pl
W³oski (it_IT) s³ownik ortograficzny dla Teda.

%package spelling-nl
Summary:	Dutch spelling dictionary for Ted
Summary(pl):	Holenderski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}

%description spelling-nl
Dutch (nl_NL) spelling dictionary for Ted.

%description spelling-nl -l pl
Holenderski (nl_NL) s³ownik ortograficzny dla Teda.

%package spelling-no
Summary:	Norwegian spelling dictionary for Ted
Summary(pl):	Norweski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}

%description spelling-no
Norwegian (no_NO) spelling dictionary for Ted.

%description spelling-no -l pl
Norweski (no_NO) s³ownik ortograficzny dla Teda.

%package spelling-pl
Summary:	Polish spelling dictionary for Ted
Summary(pl):	Polski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}

%description spelling-pl
Polish (pl_PL) spelling dictionary for Ted.

%description spelling-pl -l pl
Polski (pl_PL) s³ownik ortograficzny dla Teda.

%package spelling-pt
Summary:	Portuguese spelling dictionary for Ted
Summary(pl):	Portugalski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}

%description spelling-pt
Portuguese (pt_PT) spelling dictionary for Ted.

%description spelling-pt -l pl
Portugalski (pt_PT) s³ownik ortograficzny dla Teda.

%package spelling-ru
Summary:	Russian spelling dictionary for Ted
Summary(pl):	Rosyjski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}

%description spelling-ru
Russian (ru_RU) spelling dictionary for Ted.

%description spelling-ru -l pl
Rosyjski (ru_RU) s³ownik ortograficzny dla Teda.

%package spelling-sk
Summary:	Slovak spelling dictionary for Ted
Summary(pl):	S³owacki s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}

%description spelling-sk
Slovak (sk_SK) spelling dictionary for Ted.

%description spelling-sk -l pl
S³owacki (sk_SK) s³ownik ortograficzny dla Teda.

%package spelling-sl
Summary:	Slovene spelling dictionary for Ted
Summary(pl):	S³oweñski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}

%description spelling-sl
Slovene (sl_SI) spelling dictionary for Ted.

%description spelling-sl -l pl
S³oweñski (sl_SI) s³ownik ortograficzny dla Teda.

%package spelling-sv
Summary:	Swedish spelling dictionary for Ted
Summary(pl):	Szwedzki s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}

%description spelling-sv
Swedish (sv_SE) spelling dictionary for Ted.

%description spelling-sv -l pl
Szwedzki (sv_SE) s³ownik ortograficzny dla Teda.

%prep
%setup -q -n Ted-%{version} -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16
%patch -p1

%build
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
	CFLAGS="%{rpmcflags} `pkg-config libpng12 --cflags`"
fi
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

cd tedPackage
tar xf TedBindist.tar
cd ..

##install Ted.motif $RPM_BUILD_ROOT%{_bindir}
##install Ted/Ted $RPM_BUILD_ROOT%{_bindir}/Ted.gtk
install Ted/Ted $RPM_BUILD_ROOT%{_bindir}
install tedPackage/afm/* $RPM_BUILD_ROOT%{_datadir}/Ted/afm
install tedPackage/ind/* ind/*.ind $RPM_BUILD_ROOT%{_datadir}/Ted/ind
install tedPackage/Ted/TedDocument-en_US.rtf $RPM_BUILD_ROOT%{_datadir}/Ted

cd Ted/ad
for f in cs da de fr hu it nl sk ; do
	tar xf Ted_${f}_*.tar
	install -d $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/${f}
	# comment out evil paths
	sed -e 's@^\(Ted.*/usr\)@!\1@' usr/lib/X11/${f}_*/app-defaults/Ted \
		> $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/${f}/Ted
done
cd ../..
install -d $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/pl
install %{SOURCE17} $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/pl/Ted

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README 
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/Ted
%{_datadir}/Ted/afm
%dir %{_datadir}/Ted/ind
%{_datadir}/Ted/TedDocument*
%lang(cs) %{_libdir}/X11/app-defaults/cs/Ted
%lang(da) %{_libdir}/X11/app-defaults/da/Ted
%lang(de) %{_libdir}/X11/app-defaults/de/Ted
%lang(fr) %{_libdir}/X11/app-defaults/fr/Ted
%lang(hu) %{_libdir}/X11/app-defaults/hu/Ted
%lang(it) %{_libdir}/X11/app-defaults/it/Ted
%lang(nl) %{_libdir}/X11/app-defaults/nl/Ted
%lang(pl) %{_libdir}/X11/app-defaults/pl/Ted
%lang(sk) %{_libdir}/X11/app-defaults/sk/Ted

%files spelling-cs
%defattr(644,root,root,755)
%{_datadir}/Ted/ind/Czech.ind

%files spelling-da
%defattr(644,root,root,755)
%{_datadir}/Ted/ind/Danish.ind

%files spelling-de
%defattr(644,root,root,755)
%{_datadir}/Ted/ind/German.ind

%files spelling-en_GB
%defattr(644,root,root,755)
%{_datadir}/Ted/ind/UK_English.ind

%files spelling-en_US
%defattr(644,root,root,755)
%{_datadir}/Ted/ind/US_English.ind

%files spelling-es
%defattr(644,root,root,755)
%{_datadir}/Ted/ind/Spanish.ind

%files spelling-fr
%defattr(644,root,root,755)
%{_datadir}/Ted/ind/French.ind

%files spelling-it
%defattr(644,root,root,755)
%{_datadir}/Ted/ind/Italian.ind

%files spelling-nl
%defattr(644,root,root,755)
%{_datadir}/Ted/ind/Dutch.ind

%files spelling-no
%defattr(644,root,root,755)
%{_datadir}/Ted/ind/Norwegian.ind

%files spelling-pl
%defattr(644,root,root,755)
%{_datadir}/Ted/ind/Polish.ind

%files spelling-pt
%defattr(644,root,root,755)
%{_datadir}/Ted/ind/Portuguese.ind

%files spelling-ru
%defattr(644,root,root,755)
%{_datadir}/Ted/ind/Russian.ind

%files spelling-sk
%defattr(644,root,root,755)
%{_datadir}/Ted/ind/Slovak.ind

%files spelling-sl
%defattr(644,root,root,755)
%{_datadir}/Ted/ind/Slovene.ind

%files spelling-sv
%defattr(644,root,root,755)
%{_datadir}/Ted/ind/Swedish.ind
