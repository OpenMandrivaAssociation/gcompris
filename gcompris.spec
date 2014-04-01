%define _disable_ld_no_undefined 1

Name:		gcompris
Version:	12.11
Release:	1
Summary:	An educational game for children starting at 2
License:	GPLv2+
Group:		Education
URL:		http://www.gcompris.net
Source0:	http://prdownloads.sourceforge.net/gcompris/%{name}-%{version}.tar.bz2
Source100:	gcompris.rpmlintrc
#We don't want all warnings to be treated as errors
Patch1:		gcompris-11.09-werror.patch

BuildRequires:	gnome-common
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool-base
BuildRequires:	gnuchess
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(ao)
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(gnet-2.0)
# (misc) needed for python support
BuildRequires:	gnome-python
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(pycairo)
BuildRequires:	texinfo
BuildRequires:	texi2html >= 1.82
BuildRequires:	pkgconfig(libassetml)
# (misc) for the need of a display for pygtk
BuildRequires:	x11-server-xvfb
BuildRequires:	xauth
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	python-pyxml
BuildRequires:	python-sqlite2
BuildRequires:	pkgconfig(gtk+-2.0)
# (misc) for fullscreen support, now it is done with xvidmode instead of xrandr
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	intltool
BuildRequires:	pkgconfig(librsvg-2.0)

Requires:	%{name}-sound = %{version}-%{release}
# (misc) gnuchess for the chees activitie, gnome-python-canvas for python board
Requires:	gnuchess >= 5.02
Requires:	python
Requires:	gnome-python
Requires:	gnome-python-canvas
Requires:	pygtk2.0
Requires:	python-sqlite2
Requires:	python-cairo
Requires:	librsvg
Requires:	tuxpaint
Requires:	gnucap
Requires:	gstreamer0.10-plugins-good

%description
An educational game for children starting at 2.
More than 100 different activities are proposed:
* Click on the animals => learn the mouse/click usage
* Type the falling letters => learn the keyboard usage
* Falling Dices
* Falling words
* Basic algebra
* Time learning with an analog clock
* Puzzle game with famous paintings
* Drive Plane to catch clouds in increasing number
* Balance the scales
* And much more ...

The Game is included in the Main desktop menu in 'Games'.

You should install it only if you have children using this computer.

%package music
Summary:	Background music for GCompris
Group:		Education
Provides:	%{name}-music = %{version}
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description music
Background music for gcompris.

%package sounds-af
Summary:	Afrikaans sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-af
BuildArch:	noarch

%description sounds-af
Afrikaans sounds for gcompris.

%package sounds-ast
Summary:	Asturian sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-ast
BuildArch:	noarch

%description sounds-ast
Asturian sounds for gcompris.

%package sounds-ar
Summary:	Arabic (Tunisia) sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-ar
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-ar
Arabic (Tunisia) sounds for gcompris.

%package sounds-bg
Summary:	Bulgarian sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-bg
Conflicts:	%{name} < 8.4.4-2
BuildArch:	noarch

%description sounds-bg
Bulgarian sounds for gcompris.

%package sounds-br
Summary:	Breton sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-br
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-br
Breton sounds for gcompris.

%package sounds-cs
Summary:	Czech sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-cs
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-cs
Czech sounds for gcompris.

%package sounds-de
Summary:	German sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-de
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-de
German sounds for gcompris.

%package sounds-da
Summary:	Danish sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-da
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-da
Danish sounds for gcompris.

%package sounds-eo
Summary:	Esperanto sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-eo
Conflicts:	%{name} < 9.0-2
BuildArch:	noarch

%description sounds-eo
Esperanto sounds for gcompris.

%package sounds-es
Summary:	Spanish sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-es
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-es
Spanish sounds for gcompris.

%package sounds-el
Summary:	Greek sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-el
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-el
Greek sounds for gcompris.

%package sounds-en
Summary:	English sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-en
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-en
English sounds for gcompris.

%package sounds-eu
Summary:	Basque sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-eu
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-eu
Basque sounds for gcompris.

%package sounds-fi
Summary:	Finnish sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-fi
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-fi
Finnish sounds for gcompris.

%package sounds-fr
Summary:	French sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-fr
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-fr
French sounds for gcompris.

%package sounds-he
Summary:	Hebrew soundsfor GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-he
Conflicts:	%{name} < 8.4.6-2
BuildArch:	noarch

%description sounds-he
Hebrew sounds for gcompris.

%package sounds-hi
Summary:	Hindi soundsfor GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-hi
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-hi
Hindi sounds for gcompris.

%package sounds-hu
Summary:	Hungarian sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-hu
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-hu
Hungarian sounds for gcompris.

%package sounds-id
Summary:	Indonesian sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-id
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-id
Indonesian sounds for gcompris.

%package sounds-it
Summary:	Italian sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-it
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-it
Italian sounds for gcompris.

%package sounds-mr
Summary:	Marathi sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-mr
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-mr
Marathi sounds for gcompris.

%package sounds-nb
Summary:	Norvegian Bokmal sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-no
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-nb
Norvegian BÃ¶kmal sounds for gcompris.

%package sounds-nl
Summary:	Nederland sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-nl
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-nl
Nederland sounds for gcompris.

%package sounds-nn
Summary:	Norvegian sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-nn
BuildArch:	noarch

%description sounds-nn
Norvegian sounds for gcompris.

%package sounds-pa
Summary:	Punjabi sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-pa
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-pa
Punjabi sounds for gcompris.

%package sounds-pt
Summary:	Portuguese sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-pt
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-pt
Portuguese sounds for gcompris.

%package sounds-pt_BR
Summary:	Brasilian Portuguese sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-pt
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-pt_BR
Brasilian Portuguese sounds for gcompris.

%package sounds-ru
Summary:	Russian sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-ru
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-ru
Russian sounds for gcompris.

%package sounds-sl
Summary:	Slovenian sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-sl
BuildArch:	noarch

%description sounds-sl
Slovenian sounds for gcompris.

%package sounds-so
Summary:	Somalian sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-so
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-so
Somalian sounds for gcompris.

%package sounds-sr
Summary:	Serbian sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-sr
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-sr
Serbian sounds for gcompris.

%package sounds-sv
Summary:	Swedish sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-sv
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-sv
Swedish sounds for gcompris.

%package sounds-tr
Summary:	Turkish sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-tr
Conflicts:	%{name} < 8.4.2-2
BuildArch:	noarch

%description sounds-tr
Turkish sounds for gcompris.

%package sounds-ur
Summary:	Urdu sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-ur
Conflicts:	%{name} < 8.4.4-1
BuildArch:	noarch

%description sounds-ur
Urdu sounds for gcompris.

%package sounds-zh_CN
Summary:	Simplified Chinese sounds for GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound = %{version}-%{release}
Requires:	locales-zh
Conflicts:	%{name} < 9.1-2
BuildArch:	noarch

%description sounds-zh_CN
Simplified Chinese sounds for gcompris.

%prep
%setup -q

%build
# anaselli: added due to a patched Makefile.am needed to add Italy map
autoreconf
%configure2_5x --enable-py-build-only --enable-gnet

%make

%install
%makeinstall_std

#Fixing desktop file to match spec
perl -pi -e "s/Icon=.*/Icon=gcompris/g" %{buildroot}%{_datadir}/applications/%{name}.desktop
perl -pi -e "s/(Categories=).*/$1/" %{buildroot}%{_datadir}/applications/%{name}.desktop
perl -pi -e "s/Icon=.*/Icon=gcompris-edit/g" %{buildroot}%{_datadir}/applications/%{name}-edit.desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Education" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Education" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{name}-edit.desktop

# install icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
install -m 644 gcompris{,-edit}.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/
for size in 16x16 32x32; do
	convert -scale $size gcompris.png \
		%{buildroot}%{_iconsdir}/hicolor/$size/apps/gcompris.png
	convert -scale $size gcompris-edit.png \
		%{buildroot}%{_iconsdir}/hicolor/$size/apps/gcompris-edit.png
done

# remove unwanted files
rm -f %{buildroot}%{_menudir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man6/*
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/boards/music
%exclude %{_datadir}/%{name}/boards/voices/af
%exclude %{_datadir}/%{name}/boards/voices/ar
%exclude %{_datadir}/%{name}/boards/voices/ast
%exclude %{_datadir}/%{name}/boards/voices/bg
%exclude %{_datadir}/%{name}/boards/voices/br
%exclude %{_datadir}/%{name}/boards/voices/cs
%exclude %{_datadir}/%{name}/boards/voices/da
%exclude %{_datadir}/%{name}/boards/voices/de
%exclude %{_datadir}/%{name}/boards/voices/el
%exclude %{_datadir}/%{name}/boards/voices/en
%exclude %{_datadir}/%{name}/boards/voices/eo
%exclude %{_datadir}/%{name}/boards/voices/es
%exclude %{_datadir}/%{name}/boards/voices/eu
%exclude %{_datadir}/%{name}/boards/voices/fi
%exclude %{_datadir}/%{name}/boards/voices/fr
%exclude %{_datadir}/%{name}/boards/voices/he
%exclude %{_datadir}/%{name}/boards/voices/hi
%exclude %{_datadir}/%{name}/boards/voices/hu
%exclude %{_datadir}/%{name}/boards/voices/id
%exclude %{_datadir}/%{name}/boards/voices/it
%exclude %{_datadir}/%{name}/boards/voices/mr
%exclude %{_datadir}/%{name}/boards/voices/nb
%exclude %{_datadir}/%{name}/boards/voices/nn
%exclude %{_datadir}/%{name}/boards/voices/nl
%exclude %{_datadir}/%{name}/boards/voices/pa
%exclude %{_datadir}/%{name}/boards/voices/pt
%exclude %{_datadir}/%{name}/boards/voices/pt_BR
%exclude %{_datadir}/%{name}/boards/voices/ru
%exclude %{_datadir}/%{name}/boards/voices/sl
%exclude %{_datadir}/%{name}/boards/voices/so
%exclude %{_datadir}/%{name}/boards/voices/sr
%exclude %{_datadir}/%{name}/boards/voices/sv
%exclude %{_datadir}/%{name}/boards/voices/tr
%exclude %{_datadir}/%{name}/boards/voices/ur
%exclude %{_datadir}/%{name}/boards/voices/zh_CN

%files music
%{_datadir}/%{name}/boards/music

%files sounds-af
%{_datadir}/%{name}/boards/voices/af

%files sounds-ar
%{_datadir}/%{name}/boards/voices/ar

%files sounds-ast
%{_datadir}/%{name}/boards/voices/ast

%files sounds-bg
%{_datadir}/%{name}/boards/voices/bg

%files sounds-br
%{_datadir}/%{name}/boards/voices/br

%files sounds-cs
%{_datadir}/%{name}/boards/voices/cs

%files sounds-da
%{_datadir}/%{name}/boards/voices/da

%files sounds-de
%{_datadir}/%{name}/boards/voices/de

%files sounds-el
%{_datadir}/%{name}/boards/voices/el

%files sounds-en
%{_datadir}/%{name}/boards/voices/en

%files sounds-eo
%{_datadir}/%{name}/boards/voices/eo

%files sounds-eu
%{_datadir}/%{name}/boards/voices/eu

%files sounds-es
%{_datadir}/%{name}/boards/voices/es

%files sounds-fi
%{_datadir}/%{name}/boards/voices/fi

%files sounds-fr
%{_datadir}/%{name}/boards/voices/fr

%files sounds-he
%{_datadir}/%{name}/boards/voices/he

%files sounds-hi
%{_datadir}/%{name}/boards/voices/hi

%files sounds-hu
%{_datadir}/%{name}/boards/voices/hu

%files sounds-id
%{_datadir}/%{name}/boards/voices/id

%files sounds-it
%{_datadir}/%{name}/boards/voices/it

%files sounds-mr
%{_datadir}/%{name}/boards/voices/mr

%files sounds-nb
%{_datadir}/%{name}/boards/voices/nb

%files sounds-nl
%{_datadir}/%{name}/boards/voices/nl

%files sounds-nn
%{_datadir}/%{name}/boards/voices/nn

%files sounds-pa
%{_datadir}/%{name}/boards/voices/pa

%files sounds-pt
%{_datadir}/%{name}/boards/voices/pt

%files sounds-pt_BR
%{_datadir}/%{name}/boards/voices/pt_BR

%files sounds-ru
%{_datadir}/%{name}/boards/voices/ru

%files sounds-sl
%{_datadir}/%{name}/boards/voices/sl

%files sounds-so
%{_datadir}/%{name}/boards/voices/so

%files sounds-sr
%{_datadir}/%{name}/boards/voices/sr

%files sounds-sv
%{_datadir}/%{name}/boards/voices/sv

%files sounds-tr
%{_datadir}/%{name}/boards/voices/tr

%files sounds-ur
%{_datadir}/%{name}/boards/voices/ur

%files sounds-zh_CN
%{_datadir}/%{name}/boards/voices/zh_CN

