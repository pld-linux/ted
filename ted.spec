# NOTE: remember to update i18n resources on each Source0 update!
#       (tars are not versioned, but updated together with new ted version)
#
# TODO: fix locales in GTK+2 version (strings are encoded in legacy/mixed,
#       gtk+2 expects utf-8)
#
Summary:	Ted - easy rich text processor
Summary(pl):	Ted - prosty procesor tekstu
Name:		ted
Version:	2.16
Release:	0.1
License:	GPL
Group:		X11/Applications/Editors
Source0:	ftp://ftp.nluug.nl/pub/editors/ted/%{name}-%{version}.src.tar.gz
# Source0-md5:	51f90201dbc117906a7c4cde691d4606
Source1:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_cs_CZ.tar.gz
# Source1-md5:	5d654419e3466450e7b73ffd05efebbf
Source2:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_da_DK.tar.gz
# Source2-md5:	7e0730dee0caf533b5cbe3627a459939
Source3:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_de_DE.tar.gz
# Source3-md5:	ced06a498be16d7bb4148b7ae96500a4
Source4:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_en_GB.tar.gz
# Source4-md5:	104408a5d5a515b6238a52a87c01d31f
Source5:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_es_AR.tar.gz
# Source5-md5:	546f412c0b9500559d5e815947aeb1f0
Source6:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_es_ES.tar.gz
# Source6-md5:	3c47ab39d07174f218a2c5945b8ea72f
Source7:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_eu_FR.tar.gz
# Source7-md5:	cfdcbaca8df70fb59cda4bfa56713b79
Source8:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_fr_FR.tar.gz
# Source8-md5:	ce75da9caacd300c558b009223399363
Source9:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_hu_HU.tar.gz
# Source9-md5:	9985453ce1b3170f8f04ee9f291a7476
Source10:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_it_IT.tar.gz
# Source10-md5:	688d5df679d69a99e85d30b6a5c06e0d
Source11:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_mg_MG.tar.gz
# Source11-md5:	2393e69231e0d973dbbbacf5a294ad59
Source12:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_nl_NL.tar.gz
# Source12-md5:	7db18dd2ae84fd7caf260119819d3b6b
Source13:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_no_NO.tar.gz
# Source13-md5:	328346a213fa14e4fbd8039b7c51afdb
Source14:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_oc_FR.tar.gz
# Source14-md5:	33eb4842034fb39cc7940cd5fd308ae9
Source15:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_pl_PL.tar.gz
# Source15-md5:	daff2d8acc935f98935603168e55a038
Source16:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_pt_BR.tar.gz
# Source16-md5:	a3a37037d043a130071ed6e83a81a63d
Source17:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_pt_PT.tar.gz
# Source17-md5:	c56b9ca9e6b9d8849ced5b2de3872e65
Source18:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_ru_RU.tar.gz
# Source18-md5:	6677c6d7ed4d7a511b7cdd02df52dc9c
Source19:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_sk_SK.tar.gz
# Source19-md5:	443fb81c1de3109cae6239812aa2b933
Source20:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_sl_SI.tar.gz
# Source20-md5:	884c40f7eddab26d6b878521fb55b03d
Source21:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_sv_SE.tar.gz
Patch0:		%{name}-paths.patch
Patch1:		%{name}-gtklocale.patch
URL:		http://www.nllgg.nl/Ted/
BuildRequires:	XFree86-devel >= 4.0
BuildRequires:	autoconf
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	motif-devel
BuildRequires:	pkgconfig
Requires:	%{name}-common = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

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
Requires:	%{name}-common = %{version}-%{release}

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
Requires:	%{name}-common = %{version}-%{release}

%description spelling-cs
Czech (cs_CZ) spelling dictionary for Ted.

%description spelling-cs -l pl
Czeski (cs_CZ) s³ownik ortograficzny dla Teda.

%package spelling-da
Summary:	Danish spelling dictionary for Ted
Summary(pl):	Duñski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-da
Danish (da_DK) spelling dictionary for Ted.

%description spelling-da -l pl
Duñski (da_DK) s³ownik ortograficzny dla Teda.

%package spelling-de
Summary:	German spelling dictionary for Ted
Summary(pl):	Niemiecki s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-de
German (de_DE) spelling dictionary for Ted.

%description spelling-da -l pl
Niemiecki (de_DE) s³ownik ortograficzny dla Teda.

%package spelling-en_GB
Summary:	English (UK) spelling dictionary for Ted
Summary(pl):	Angielski (brytyjski) s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-en_GB
English (UK - en_GB) spelling dictionary for Ted.

%description spelling-en_GB -l pl
Angielski (brytyjski - en_GB) s³ownik ortograficzny dla Teda.

%package spelling-en_US
Summary:	English (US) spelling dictionary for Ted
Summary(pl):	Angielski (amerykañski) s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-en_US
English (en_US) spelling dictionary for Ted.

%description spelling-en_US -l pl
Angielski (amerykañski - en_US) s³ownik ortograficzny dla Teda.

%package spelling-es
Summary:	Spanish spelling dictionary for Ted
Summary(pl):	Hiszpañski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-es
Spanish (es_ES) spelling dictionary for Ted.

%description spelling-es -l pl
Hiszpañski (es_ES) s³ownik ortograficzny dla Teda.

%package spelling-fr
Summary:	French spelling dictionary for Ted
Summary(pl):	Francuski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-fr
French (fr_FR) spelling dictionary for Ted.

%description spelling-fr -l pl
Francuski (fr_FR) s³ownik ortograficzny dla Teda.

%package spelling-it
Summary:	Italian spelling dictionary for Ted
Summary(pl):	W³oski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-it
Italian (it_IT) spelling dictionary for Ted.

%description spelling-it -l pl
W³oski (it_IT) s³ownik ortograficzny dla Teda.

%package spelling-nl
Summary:	Dutch spelling dictionary for Ted
Summary(pl):	Holenderski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-nl
Dutch (nl_NL) spelling dictionary for Ted.

%description spelling-nl -l pl
Holenderski (nl_NL) s³ownik ortograficzny dla Teda.

%package spelling-no
Summary:	Norwegian spelling dictionary for Ted
Summary(pl):	Norweski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-no
Norwegian (no_NO) spelling dictionary for Ted.

%description spelling-no -l pl
Norweski (no_NO) s³ownik ortograficzny dla Teda.

%package spelling-pl
Summary:	Polish spelling dictionary for Ted
Summary(pl):	Polski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-pl
Polish (pl_PL) spelling dictionary for Ted.

%description spelling-pl -l pl
Polski (pl_PL) s³ownik ortograficzny dla Teda.

%package spelling-pt
Summary:	Portuguese spelling dictionary for Ted
Summary(pl):	Portugalski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-pt
Portuguese (pt_PT) spelling dictionary for Ted.

%description spelling-pt -l pl
Portugalski (pt_PT) s³ownik ortograficzny dla Teda.

%package spelling-ru
Summary:	Russian spelling dictionary for Ted
Summary(pl):	Rosyjski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-ru
Russian (ru_RU) spelling dictionary for Ted.

%description spelling-ru -l pl
Rosyjski (ru_RU) s³ownik ortograficzny dla Teda.

%package spelling-sk
Summary:	Slovak spelling dictionary for Ted
Summary(pl):	S³owacki s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-sk
Slovak (sk_SK) spelling dictionary for Ted.

%description spelling-sk -l pl
S³owacki (sk_SK) s³ownik ortograficzny dla Teda.

%package spelling-sl
Summary:	Slovene spelling dictionary for Ted
Summary(pl):	S³oweñski s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-sl
Slovene (sl_SI) spelling dictionary for Ted.

%description spelling-sl -l pl
S³oweñski (sl_SI) s³ownik ortograficzny dla Teda.

%package spelling-sv
Summary:	Swedish spelling dictionary for Ted
Summary(pl):	Szwedzki s³ownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-sv
Swedish (sv_SE) spelling dictionary for Ted.

%description spelling-sv -l pl
Szwedzki (sv_SE) s³ownik ortograficzny dla Teda.

%prep
%setup -q -n Ted-%{version} -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21
%patch0 -p1
%patch1 -p1

%build
for d in bitmap ind libreg appUtil appFrame Ted; do
	cd $d
	autoconf
	%configure \
		--with-MOTIF
	cd ..
done
%{__make} compile.shared
mv -f Ted/Ted Ted.motif

for d in appFrame Ted; do
	cd $d
	rm -f *.o
	%configure \
		--with-GTK
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
# pt is pt_BR here, but there is no pt_PT translation
for f in cs da de eu fr hu it mg nl no oc pl pt sk ; do
	tar xf Ted_${f}_*.tar
	install -d $RPM_BUILD_ROOT%{_appdefsdir}/${f}
	# comment out evil paths
	sed -e 's@^\(Ted.*/usr\)@!\1@' usr/lib/X11/${f}_*/app-defaults/Ted \
		> $RPM_BUILD_ROOT%{_appdefsdir}/${f}/Ted
done
# special case
tar xf Ted_es_AR.ad.tar
install -d $RPM_BUILD_ROOT%{_appdefsdir}/es_AR
sed -e 's@^\(Ted.*/usr\)@!\1@' usr/lib/X11/es_AR/app-defaults/Ted \
	> $RPM_BUILD_ROOT%{_appdefsdir}/es_AR/Ted
tar xf Ted_es_ES.ad.tar
install -d $RPM_BUILD_ROOT%{_appdefsdir}/es
sed -e 's@^\(Ted.*/usr\)@!\1@' usr/lib/X11/es_AR/app-defaults/Ted \
	> $RPM_BUILD_ROOT%{_appdefsdir}/es/Ted

# use latin2 font for pl_PL messages
echo 'Ted*fontList:	-adobe-helvetica-medium-r-*-*-*-100-*-*-*-*-iso8859-2' \
	>> $RPM_BUILD_ROOT%{_appdefsdir}/pl/Ted

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
%lang(cs) %{_appdefsdir}/cs/Ted
%lang(da) %{_appdefsdir}/da/Ted
%lang(de) %{_appdefsdir}/de/Ted
%lang(es) %{_appdefsdir}/es/Ted
%lang(es_AR) %{_appdefsdir}/es_AR/Ted
%lang(eu) %{_appdefsdir}/eu/Ted
%lang(fr) %{_appdefsdir}/fr/Ted
%lang(hu) %{_appdefsdir}/hu/Ted
%lang(it) %{_appdefsdir}/it/Ted
%lang(mg) %{_appdefsdir}/mg/Ted
%lang(nl) %{_appdefsdir}/nl/Ted
%lang(nb) %{_appdefsdir}/no/Ted
%lang(oc) %{_appdefsdir}/oc/Ted
%lang(pl) %{_appdefsdir}/pl/Ted
%lang(pt) %{_appdefsdir}/pt/Ted
%lang(sk) %{_appdefsdir}/sk/Ted

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
