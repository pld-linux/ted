Summary:	Ted - easy rich text processor
Summary(pl):	Ted - prosty procesor tekstu
Name:		ted
Version:	2.14
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	ftp://ftp.nluug.nl/pub/editors/%{name}/%{name}-%{version}.src.tar.gz
Source1:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_cs_CZ.tar.gz
Source2:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_da_DK.tar.gz
Source3:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_de_DE.tar.gz
Source4:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_en_GB.tar.gz
Source5:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_es_ES.tar.gz
Source6:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_eu_FR.tar.gz
Source7:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_fr_FR.tar.gz
Source8:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_hu_HU.tar.gz
Source9:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_it_IT.tar.gz
Source10:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_mg_MG.tar.gz
Source11:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_nl_NL.tar.gz
Source12:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_no_NO.tar.gz
Source13:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_oc_FR.tar.gz
Source14:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_pl_PL.tar.gz
Source15:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_pt_PT.tar.gz
Source16:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_ru_RU.tar.gz
Source17:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_sk_SK.tar.gz
Source18:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_sl_SI.tar.gz
Source19:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_sv_SE.tar.gz
# included in Source14 now, but not updated for 2.13
Source20:	Ted.ad.pl_PL
Patch0:		%{name}-paths.patch
Patch1:		%{name}-gtklocale.patch
URL:		http://www.nllgg.nl/Ted/
BuildRequires:	XFree86-devel >= 4.0
BuildRequires:	autoconf
BuildRequires:	gtk+-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	motif-devel
Requires:	%{name}-common = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		addir	/usr/X11R6/lib/X11/app-defaults

%description
Ted is a text processor running under X Window on Unix/Linux systems.
It was made to edit rich text documents on Unix/Linux in a WYSIWYG
way. It can edit MS RTF files and print to PostScript.

%description -l pl
Ted jest procesorem tekstu dzia³aj±cym pod X Window pod unices. S³u¿y
do edycji dokumentów tekstowych w stylu WYSIWYG. Mo¿e obrabiaæ pliki w
formacie MS RTF i drukowaæ w PostScripcie.

%package gtk
Summary:	Ted with GTK+-based interface
Summary(pl):	Ted z interfejsem opartym na GTK+
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}

%description gtk
Ted with interface based on GTK+ instead of Motif.

%description gtk -l pl
Ted z interfejsem opartym na GTK+, a nie na Motifie.

%package common
Summary:	Common package for both Ted interfaces
Summary(pl):	Wspólny pakiet dla obu interfejsów Teda
Group:		X11/Applications/Editors

%description common
Common package for both Ted interfaces.

%description common -l pl
Wspólny pakiet dla obu interfejsów Teda.

%package spelling-cs
Summary:	Czech spelling dictionary for Ted
Summary(pl):	Czeski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}

%description spelling-cs
Czech (cs_CZ) spelling dictionary for Ted.

%description spelling-cs -l pl
Czeski (cs_CZ) s³ownik ortograficzny dla Teda.

%package spelling-da
Summary:	Danish spelling dictionary for Ted
Summary(pl):	Duñski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}

%description spelling-da
Danish (da_DK) spelling dictionary for Ted.

%description spelling-da -l pl
Duñski (da_DK) s³ownik ortograficzny dla Teda.

%package spelling-de
Summary:	German spelling dictionary for Ted
Summary(pl):	Niemiecki s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}

%description spelling-de
German (de_DE) spelling dictionary for Ted.

%description spelling-da -l pl
Niemiecki (de_DE) s³ownik ortograficzny dla Teda.

%package spelling-en_GB
Summary:	English (UK) spelling dictionary for Ted
Summary(pl):	Angielski (brytyjski) s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}

%description spelling-en_GB
English (UK - en_GB) spelling dictionary for Ted.

%description spelling-en_GB -l pl
Angielski (brytyjski - en_GB) s³ownik ortograficzny dla Teda.

%package spelling-en_US
Summary:	English (US) spelling dictionary for Ted
Summary(pl):	Angielski (amerykañski) s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}

%description spelling-en_US
English (en_US) spelling dictionary for Ted.

%description spelling-en_US -l pl
Angielski (amerykañski - en_US) s³ownik ortograficzny dla Teda.

%package spelling-es
Summary:	Spanish spelling dictionary for Ted
Summary(pl):	Hiszpañski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}

%description spelling-es
Spanish (es_ES) spelling dictionary for Ted.

%description spelling-es -l pl
Hiszpañski (es_ES) s³ownik ortograficzny dla Teda.

%package spelling-fr
Summary:	French spelling dictionary for Ted
Summary(pl):	Francuski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}

%description spelling-fr
French (fr_FR) spelling dictionary for Ted.

%description spelling-fr -l pl
Francuski (fr_FR) s³ownik ortograficzny dla Teda.

%package spelling-it
Summary:	Italian spelling dictionary for Ted
Summary(pl):	W³oski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}

%description spelling-it
Italian (it_IT) spelling dictionary for Ted.

%description spelling-it -l pl
W³oski (it_IT) s³ownik ortograficzny dla Teda.

%package spelling-nl
Summary:	Dutch spelling dictionary for Ted
Summary(pl):	Holenderski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}

%description spelling-nl
Dutch (nl_NL) spelling dictionary for Ted.

%description spelling-nl -l pl
Holenderski (nl_NL) s³ownik ortograficzny dla Teda.

%package spelling-no
Summary:	Norwegian spelling dictionary for Ted
Summary(pl):	Norweski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}

%description spelling-no
Norwegian (no_NO) spelling dictionary for Ted.

%description spelling-no -l pl
Norweski (no_NO) s³ownik ortograficzny dla Teda.

%package spelling-pl
Summary:	Polish spelling dictionary for Ted
Summary(pl):	Polski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}

%description spelling-pl
Polish (pl_PL) spelling dictionary for Ted.

%description spelling-pl -l pl
Polski (pl_PL) s³ownik ortograficzny dla Teda.

%package spelling-pt
Summary:	Portuguese spelling dictionary for Ted
Summary(pl):	Portugalski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}

%description spelling-pt
Portuguese (pt_PT) spelling dictionary for Ted.

%description spelling-pt -l pl
Portugalski (pt_PT) s³ownik ortograficzny dla Teda.

%package spelling-ru
Summary:	Russian spelling dictionary for Ted
Summary(pl):	Rosyjski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}

%description spelling-ru
Russian (ru_RU) spelling dictionary for Ted.

%description spelling-ru -l pl
Rosyjski (ru_RU) s³ownik ortograficzny dla Teda.

%package spelling-sk
Summary:	Slovak spelling dictionary for Ted
Summary(pl):	S³owacki s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}

%description spelling-sk
Slovak (sk_SK) spelling dictionary for Ted.

%description spelling-sk -l pl
S³owacki (sk_SK) s³ownik ortograficzny dla Teda.

%package spelling-sl
Summary:	Slovene spelling dictionary for Ted
Summary(pl):	S³oweñski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}

%description spelling-sl
Slovene (sl_SI) spelling dictionary for Ted.

%description spelling-sl -l pl
S³oweñski (sl_SI) s³ownik ortograficzny dla Teda.

%package spelling-sv
Summary:	Swedish spelling dictionary for Ted
Summary(pl):	Szwedzki s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}

%description spelling-sv
Swedish (sv_SE) spelling dictionary for Ted.

%description spelling-sv -l pl
Szwedzki (sv_SE) s³ownik ortograficzny dla Teda.

%prep
%setup -q -n Ted-%{version} -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19
%patch0 -p1
%patch1 -p1

%build
for d in bitmap ind libreg appUtil appFrame Ted; do
	cd $d
	autoconf
	%configure --with-MOTIF
	cd ..
done
%{__make} compile.shared
mv -f Ted/Ted Ted.motif

for d in appFrame Ted; do
	cd $d
	rm -f *.o
	%configure --with-GTK
	cd ..
done
%{__make} compile.shared

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/Ted/{afm,ind}}

cd tedPackage
tar xf TedBindist.tar
cd ..

install Ted.motif $RPM_BUILD_ROOT%{_bindir}/Ted
install Ted/Ted $RPM_BUILD_ROOT%{_bindir}/Ted.gtk
install tedPackage/afm/* $RPM_BUILD_ROOT%{_datadir}/Ted/afm
install tedPackage/ind/* ind/*.ind $RPM_BUILD_ROOT%{_datadir}/Ted/ind
install tedPackage/Ted/TedDocument-en_US.rtf $RPM_BUILD_ROOT%{_datadir}/Ted

cd Ted
install TedDocument-*.rtf $RPM_BUILD_ROOT%{_datadir}/Ted
cd ad
for f in cs da de eu fr hu it mg nl oc pl sk ; do
	tar xf Ted_${f}_*.tar
	install -d $RPM_BUILD_ROOT%{addir}/${f}
	# comment out evil paths
	sed -e 's@^\(Ted.*/usr\)@!\1@' usr/lib/X11/${f}_*/app-defaults/Ted \
		> $RPM_BUILD_ROOT%{addir}/${f}/Ted
done
# overwrite pl_PL with updated version
install %{SOURCE20} $RPM_BUILD_ROOT%{addir}/pl/Ted

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Ted

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Ted.gtk

%files common
%defattr(644,root,root,755)
%doc README 
%dir %{_datadir}/Ted
%{_datadir}/Ted/afm
%dir %{_datadir}/Ted/ind
%lang(de) %{_datadir}/Ted/TedDocument-de_DE.rtf
%{_datadir}/Ted/TedDocument-en_US.rtf
%lang(fr) %{_datadir}/Ted/TedDocument-fr_FR.rtf
%lang(mg) %{_datadir}/Ted/TedDocument-mg_MG.rtf
%lang(cs) %{addir}/cs/Ted
%lang(da) %{addir}/da/Ted
%lang(de) %{addir}/de/Ted
%lang(eu) %{addir}/eu/Ted
%lang(fr) %{addir}/fr/Ted
%lang(hu) %{addir}/hu/Ted
%lang(it) %{addir}/it/Ted
%lang(mg) %{addir}/mg/Ted
%lang(nl) %{addir}/nl/Ted
%lang(oc) %{addir}/oc/Ted
%lang(pl) %{addir}/pl/Ted
%lang(sk) %{addir}/sk/Ted

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
