# NOTE: remember to update i18n resources on each Source0 update!
#       (tars are not versioned, but updated together with new ted version)
#
Summary:	Ted - easy rich text processor
Summary(pl):	Ted - prosty procesor tekstu
Name:		ted
Version:	2.14
Release:	2
License:	GPL
Group:		X11/Applications/Editors
Source0:	ftp://ftp.nluug.nl/pub/editors/%{name}/%{name}-%{version}.src.tar.gz
# Source0-md5:	7ed8207cdc925ee7f8b8770ca0af3e52
Source1:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_cs_CZ.tar.gz
# Source1-md5:	7942ed59a701c20056fc86b3384fb638
Source2:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_da_DK.tar.gz
# Source2-md5:	9ab8e7495e8cbf4e7d5dc57f6007b08a
Source3:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_de_DE.tar.gz
# Source3-md5:	c283b5c1c70bec15149ba3ffbf271535
Source4:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_en_GB.tar.gz
# Source4-md5:	1c7a8fb09070aedf3c75d99f36632919
Source5:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_es_ES.tar.gz
# Source5-md5:	0b64b1251593736f36109ecce7e7dc74
Source6:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_eu_FR.tar.gz
# Source6-md5:	3d9a5b5f094e36e35ae9b7e25918cafd
Source7:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_fr_FR.tar.gz
# Source7-md5:	a8d2c8029de15a4136d9a155666e5c79
Source8:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_hu_HU.tar.gz
# Source8-md5:	12c10b461ca40b3ce0dcf82926c311ed
Source9:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_it_IT.tar.gz
# Source9-md5:	f175c23ecdae4f32656a49566af36b42
Source10:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_mg_MG.tar.gz
# Source10-md5:	04d34808a6b6613a3773ee9bd3b49c90
Source11:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_nl_NL.tar.gz
# Source11-md5:	98e71c2e7ff909417b9e316882bbc73e
Source12:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_no_NO.tar.gz
# Source12-md5:	40b35fe137d0618fb1b197ccdcbf0d9f
Source13:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_oc_FR.tar.gz
# Source13-md5:	d7a0d3d410dfe73ec48f050eb33c7d0d
Source14:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_pl_PL.tar.gz
# Source14-md5:	532ce1d54259d2057f0e97a3efaf7866
Source15:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_pt_BR.tar.gz
# Source15-md5:	e26bda0ab2219a1235c57b9b74215165
Source16:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_pt_PT.tar.gz
# Source16-md5:	c56b9ca9e6b9d8849ced5b2de3872e65
Source17:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_ru_RU.tar.gz
# Source17-md5:	6677c6d7ed4d7a511b7cdd02df52dc9c
Source18:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_sk_SK.tar.gz
# Source18-md5:	1118b80cd609dc8115f512302a571fd4
Source19:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_sl_SI.tar.gz
# Source19-md5:	884c40f7eddab26d6b878521fb55b03d
Source20:	ftp://ftp.nluug.nl/pub/editors/%{name}/Ted_sv_SE.tar.gz
# Source20-md5:	1a61f9dccd1682581c33e8f99a66ba01
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
%setup -q -n Ted-%{version} -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20
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
# pt is pt_BR here, but there is no pt_PT translation
for f in cs da de eu fr hu it mg nl no oc pl pt sk ; do
	tar xf Ted_${f}_*.tar
	install -d $RPM_BUILD_ROOT%{_appdefsdir}/${f}
	# comment out evil paths
	sed -e 's@^\(Ted.*/usr\)@!\1@' usr/lib/X11/${f}_*/app-defaults/Ted \
		> $RPM_BUILD_ROOT%{_appdefsdir}/${f}/Ted
done

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
