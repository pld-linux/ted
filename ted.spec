# NOTE: remember to update i18n resources on each Source0 update!
#       (tars are not versioned, but updated together with new ted version)
#
# TODO: fix locales in GTK+2 version (strings are encoded in legacy/mixed,
#       gtk+2 expects utf-8)
#
Summary:	Ted - easy rich text processor
Summary(pl.UTF-8):	Ted - prosty procesor tekstu
Name:		ted
Version:	2.17
Release:	9
License:	GPL
Group:		X11/Applications/Editors
Source0:	ftp://ftp.nluug.nl/pub/editors/ted/%{name}-%{version}.src.tar.gz
# Source0-md5:	8adc2ab0a67954b2b5068c9be243c82d
Source1:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_cs_CZ.tar.gz
# Source1-md5:	d0e5bb73ceda6398ff76e44893e15437
Source2:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_da_DK.tar.gz
# Source2-md5:	710cbd18fca03b29cdeb0d7ed15480ee
Source3:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_de_DE.tar.gz
# Source3-md5:	896b464240f2a02128f92a7f652ec1c8
Source4:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_en_GB.tar.gz
# Source4-md5:	104408a5d5a515b6238a52a87c01d31f
Source5:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_es_AR.tar.gz
# Source5-md5:	8cb7ba7ad35d48bb5a1315bc75b0685d
Source6:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_es_ES.tar.gz
# Source6-md5:	37153f84ae05d25d418521a5f9650ef7
Source7:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_eu_FR.tar.gz
# Source7-md5:	6c23467ea1e6953f627d3ed8a78e7c15
Source8:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_fr_FR.tar.gz
# Source8-md5:	45b8e048b1bcf55766ecf6e8852b153d
Source9:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_hu_HU.tar.gz
# Source9-md5:	75686a70dc892e68f554cbd0045cbc72
Source10:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_it_IT.tar.gz
# Source10-md5:	7596605fc2986191c1bf2f0f35556d49
Source11:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_mg_MG.tar.gz
# Source11-md5:	2f42eed6105a6ba42b09efbb84686be8
Source12:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_nl_NL.tar.gz
# Source12-md5:	4a2a707581b8c5589b0df2840f528595
Source13:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_no_NO.tar.gz
# Source13-md5:	1fc60a90e5d4a68a4e2db335b0e5e500
Source14:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_oc_FR.tar.gz
# Source14-md5:	4149bcf3f56d03b7dfee724444da93e1
Source15:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_pl_PL.tar.gz
# Source15-md5:	56dae2bd3c9d99a280c12bfeab1e4bd7
Source16:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_pt_BR.tar.gz
# Source16-md5:	6068db5077102768b6351ba24707ea59
Source17:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_pt_PT.tar.gz
# Source17-md5:	c56b9ca9e6b9d8849ced5b2de3872e65
Source18:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_ru_RU.tar.gz
# Source18-md5:	6677c6d7ed4d7a511b7cdd02df52dc9c
Source19:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_sk_SK.tar.gz
# Source19-md5:	c001543f5b6822b527e54435c97c14c4
Source20:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_sl_SI.tar.gz
# Source20-md5:	884c40f7eddab26d6b878521fb55b03d
Source21:	ftp://ftp.nluug.nl/pub/editors/ted/Ted_sv_SE.tar.gz
# Source21-md5:	1a61f9dccd1682581c33e8f99a66ba01
Patch0:		%{name}-paths.patch
Patch1:		%{name}-gtklocale.patch
Patch2:		%{name}-gtk.patch
Patch3:		%{name}-pl.patch
Patch4:		%{name}-libpng15.patch
URL:		http://www.nllgg.nl/Ted/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	motif-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXmu-devel
Requires:	%{name}-common = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ted is a text processor running under X Window on Unix/Linux systems.
It was made to edit rich text documents on Unix/Linux in a WYSIWYG
way. It can edit MS RTF files and print to PostScript.

%description -l pl.UTF-8
Ted jest procesorem tekstu działającym pod X Window pod unices. Służy
do edycji dokumentów tekstowych w stylu WYSIWYG. Może obrabiać pliki w
formacie MS RTF i drukować w PostScripcie.

%package gtk
Summary:	Ted with GTK+-based interface
Summary(pl.UTF-8):	Ted z interfejsem opartym na GTK+
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description gtk
Ted with interface based on GTK+ instead of Motif.

%description gtk -l pl.UTF-8
Ted z interfejsem opartym na GTK+, a nie na Motifie.

%package common
Summary:	Common package for both Ted interfaces
Summary(pl.UTF-8):	Wspólny pakiet dla obu interfejsów Teda
Group:		X11/Applications/Editors
Requires:	xorg-lib-libXt-devel >= 1.0.0

%description common
Common package for both Ted interfaces.

%description common -l pl.UTF-8
Wspólny pakiet dla obu interfejsów Teda.

%package spelling-cs
Summary:	Czech spelling dictionary for Ted
Summary(pl.UTF-8):	Czeski słownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-cs
Czech (cs_CZ) spelling dictionary for Ted.

%description spelling-cs -l pl.UTF-8
Czeski (cs_CZ) słownik ortograficzny dla Teda.

%package spelling-da
Summary:	Danish spelling dictionary for Ted
Summary(pl.UTF-8):	Duński słownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-da
Danish (da_DK) spelling dictionary for Ted.

%description spelling-da -l pl.UTF-8
Duński (da_DK) słownik ortograficzny dla Teda.

%package spelling-de
Summary:	German spelling dictionary for Ted
Summary(pl.UTF-8):	Niemiecki słownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-de
German (de_DE) spelling dictionary for Ted.

%description spelling-de -l pl.UTF-8
Niemiecki (de_DE) słownik ortograficzny dla Teda.

%package spelling-en_GB
Summary:	English (UK) spelling dictionary for Ted
Summary(pl.UTF-8):	Angielski (brytyjski) słownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-en_GB
English (UK - en_GB) spelling dictionary for Ted.

%description spelling-en_GB -l pl.UTF-8
Angielski (brytyjski - en_GB) słownik ortograficzny dla Teda.

%package spelling-en_US
Summary:	English (US) spelling dictionary for Ted
Summary(pl.UTF-8):	Angielski (amerykański) słownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-en_US
English (en_US) spelling dictionary for Ted.

%description spelling-en_US -l pl.UTF-8
Angielski (amerykański - en_US) słownik ortograficzny dla Teda.

%package spelling-es
Summary:	Spanish spelling dictionary for Ted
Summary(pl.UTF-8):	Hiszpański słownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-es
Spanish (es_ES) spelling dictionary for Ted.

%description spelling-es -l pl.UTF-8
Hiszpański (es_ES) słownik ortograficzny dla Teda.

%package spelling-fr
Summary:	French spelling dictionary for Ted
Summary(pl.UTF-8):	Francuski słownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-fr
French (fr_FR) spelling dictionary for Ted.

%description spelling-fr -l pl.UTF-8
Francuski (fr_FR) słownik ortograficzny dla Teda.

%package spelling-it
Summary:	Italian spelling dictionary for Ted
Summary(pl.UTF-8):	Włoski słownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-it
Italian (it_IT) spelling dictionary for Ted.

%description spelling-it -l pl.UTF-8
Włoski (it_IT) słownik ortograficzny dla Teda.

%package spelling-nb
Summary:	Norwegian spelling dictionary for Ted
Summary(pl.UTF-8):	Norweski słownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	ted-spelling-no

%description spelling-nb
Norwegian (nb_NO) spelling dictionary for Ted.

%description spelling-nb -l pl.UTF-8
Norweski (nb_NO) słownik ortograficzny dla Teda.

%package spelling-nl
Summary:	Dutch spelling dictionary for Ted
Summary(pl.UTF-8):	Holenderski słownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-nl
Dutch (nl_NL) spelling dictionary for Ted.

%description spelling-nl -l pl.UTF-8
Holenderski (nl_NL) słownik ortograficzny dla Teda.

%package spelling-pl
Summary:	Polish spelling dictionary for Ted
Summary(pl.UTF-8):	Polski słownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-pl
Polish (pl_PL) spelling dictionary for Ted.

%description spelling-pl -l pl.UTF-8
Polski (pl_PL) słownik ortograficzny dla Teda.

%package spelling-pt
Summary:	Portuguese spelling dictionary for Ted
Summary(pl.UTF-8):	Portugalski słownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-pt
Portuguese (pt_PT) spelling dictionary for Ted.

%description spelling-pt -l pl.UTF-8
Portugalski (pt_PT) słownik ortograficzny dla Teda.

%package spelling-ru
Summary:	Russian spelling dictionary for Ted
Summary(pl.UTF-8):	Rosyjski słownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-ru
Russian (ru_RU) spelling dictionary for Ted.

%description spelling-ru -l pl.UTF-8
Rosyjski (ru_RU) słownik ortograficzny dla Teda.

%package spelling-sk
Summary:	Slovak spelling dictionary for Ted
Summary(pl.UTF-8):	Słowacki słownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-sk
Slovak (sk_SK) spelling dictionary for Ted.

%description spelling-sk -l pl.UTF-8
Słowacki (sk_SK) słownik ortograficzny dla Teda.

%package spelling-sl
Summary:	Slovene spelling dictionary for Ted
Summary(pl.UTF-8):	Słoweński słownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-sl
Slovene (sl_SI) spelling dictionary for Ted.

%description spelling-sl -l pl.UTF-8
Słoweński (sl_SI) słownik ortograficzny dla Teda.

%package spelling-sv
Summary:	Swedish spelling dictionary for Ted
Summary(pl.UTF-8):	Szwedzki słownik ortograficzny dla Teda
Group:		X11/Applications/Editors
Requires:	%{name}-common = %{version}-%{release}

%description spelling-sv
Swedish (sv_SE) spelling dictionary for Ted.

%description spelling-sv -l pl.UTF-8
Szwedzki (sv_SE) słownik ortograficzny dla Teda.

%prep
%setup -q -n Ted-%{version} -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

cd tedPackage
tar xf TedBindist.tar
cd ../Ted/ad
for f in *.tar ; do
	tar xf "$f"
done
mv -f usr/lib/X11/{no_NO,nb_NO}
cd ../..
%patch -P3 -p1
%patch -P4 -p0


%build
for d in bitmap ind libreg appUtil appFrame Ted; do
	cd $d
	%{__autoconf}
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

install Ted.motif $RPM_BUILD_ROOT%{_bindir}/Ted
install Ted/Ted $RPM_BUILD_ROOT%{_bindir}/Ted.gtk
install tedPackage/afm/* $RPM_BUILD_ROOT%{_datadir}/Ted/afm
install tedPackage/ind/* ind/*.ind $RPM_BUILD_ROOT%{_datadir}/Ted/ind
install tedPackage/Ted/TedDocument-en_US.rtf $RPM_BUILD_ROOT%{_datadir}/Ted

cd Ted
install TedDocument-*.rtf $RPM_BUILD_ROOT%{_datadir}/Ted
cd ad
# pt is pt_BR here, but there is no pt_PT translation
for f in cs da de eu fr hu it mg nb nl oc pl pt sk ; do
	install -d $RPM_BUILD_ROOT%{_datadir}/X11/${f}/app-defaults
	# comment out evil paths
	sed -e 's@^\(Ted.*/usr\)@!\1@' usr/lib/X11/${f}_*/app-defaults/Ted \
		> $RPM_BUILD_ROOT%{_datadir}/X11/${f}/app-defaults/Ted
done
# special case
install -d $RPM_BUILD_ROOT%{_datadir}/X11/es_AR/app-defaults
sed -e 's@^\(Ted.*/usr\)@!\1@' usr/lib/X11/es_AR/app-defaults/Ted \
	> $RPM_BUILD_ROOT%{_datadir}/X11/es_AR/app-defaults/Ted
install -d $RPM_BUILD_ROOT%{_datadir}/X11/es/app-defaults
sed -e 's@^\(Ted.*/usr\)@!\1@' usr/lib/X11/es_AR/app-defaults/Ted \
	> $RPM_BUILD_ROOT%{_datadir}/X11/es/app-defaults/Ted

# use latin2 font for pl_PL messages
echo 'Ted*fontList:	-adobe-helvetica-medium-r-*-*-*-100-*-*-*-*-iso8859-2' \
	>> $RPM_BUILD_ROOT%{_datadir}/X11/pl/app-defaults/Ted

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
%lang(cs) %{_datadir}/X11/cs/app-defaults/Ted
%lang(da) %{_datadir}/X11/da/app-defaults/Ted
%lang(de) %{_datadir}/X11/de/app-defaults/Ted
%lang(es) %{_datadir}/X11/es/app-defaults/Ted
%lang(es_AR) %{_datadir}/X11/es_AR/app-defaults/Ted
%lang(eu) %{_datadir}/X11/eu/app-defaults/Ted
%lang(fr) %{_datadir}/X11/fr/app-defaults/Ted
%lang(hu) %{_datadir}/X11/hu/app-defaults/Ted
%lang(it) %{_datadir}/X11/it/app-defaults/Ted
%lang(mg) %{_datadir}/X11/mg/app-defaults/Ted
%lang(nb) %{_datadir}/X11/nb/app-defaults/Ted
%lang(nl) %{_datadir}/X11/nl/app-defaults/Ted
%lang(oc) %{_datadir}/X11/oc/app-defaults/Ted
%lang(pl) %{_datadir}/X11/pl/app-defaults/Ted
%lang(pt) %{_datadir}/X11/pt/app-defaults/Ted
%lang(sk) %{_datadir}/X11/sk/app-defaults/Ted

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

%files spelling-nb
%defattr(644,root,root,755)
%{_datadir}/Ted/ind/Norwegian.ind

%files spelling-nl
%defattr(644,root,root,755)
%{_datadir}/Ted/ind/Dutch.ind

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
