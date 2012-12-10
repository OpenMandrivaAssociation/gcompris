Name:		gcompris
Version:	12.01
Release:	2
Summary:	An educational game for children starting at 2
License:	GPLv2+
Group:		Education
URL:		http://www.gcompris.net
Source:		http://prdownloads.sourceforge.net/gcompris/%{name}-%{version}.tar.gz
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
Requires:	locales-zh_CN
Conflicts:	%{name} < 9.1-2
BuildArch:	noarch

%description sounds-zh_CN
Simplified Chinese sounds for gcompris.

%prep
%setup -q
%patch1 -p1 -b .werror

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
%{_infodir}/*
%{_datadir}/%{name}
%{_datadir}/gnome/help/%{name}/eu/*
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


%changelog
* Tue Mar 20 2012 Andrey Bondrov <abondrov@mandriva.org> 12.01-1mdv2012.0
+ Revision: 785853
- Update Requires and BuildRequires
- New version 12.01

* Fri Nov 04 2011 Andrey Bondrov <abondrov@mandriva.org> 11.09-1
+ Revision: 717610
- Add patch0 to fix deprecated glib stuff and patch1 to fix build
- New version 11.09, make music and sounds noarch, spec cleanup

* Sun Jun 19 2011 Angelo Naselli <anaselli@mandriva.org> 9.6.1-2
+ Revision: 686071
- added Italian provinces

* Thu Apr 28 2011 Angelo Naselli <anaselli@mandriva.org> 9.6.1-1
+ Revision: 659849
- removed Werror to allow building
- new version 9.6.1
- added Italy map, thanks to ALID (www.alid.it)

* Sat Jan 01 2011 John Balcaen <mikala@mandriva.org> 9.5-2mdv2011.0
+ Revision: 626930
- fix provides for gcompris-sound (main package requires version-release)

* Sat Dec 25 2010 Funda Wang <fwang@mandriva.org> 9.5-1mdv2011.0
+ Revision: 624812
- new version 9.5

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

* Sat Jul 17 2010 Funda Wang <fwang@mandriva.org> 9.3-1mdv2011.0
+ Revision: 554688
- new version 9.3

* Wed Apr 28 2010 Frederic Crozat <fcrozat@mandriva.com> 9.2-2mdv2010.1
+ Revision: 540205
- Patch3 (Luis Medinas): fix build with latest gtk (Mdv bug #58875)

* Sun Feb 14 2010 Funda Wang <fwang@mandriva.org> 9.2-1mdv2010.1
+ Revision: 505839
- new version 9.2
- fix conflict version

* Mon Feb 01 2010 Funda Wang <fwang@mandriva.org> 9.1-2mdv2010.1
+ Revision: 498954
- split out zh_CN sound

* Mon Jan 25 2010 Erwan Velu <erwan@mandriva.org> 9.1-1mdv2010.1
+ Revision: 495696
- 9.1

* Thu Jan 07 2010 Funda Wang <fwang@mandriva.org> 9.0-2mdv2010.1
+ Revision: 487017
- split out sounds-eo

* Tue Jan 05 2010 trem <trem@mandriva.org> 9.0-1mdv2010.1
+ Revision: 486506
- update to new release 9.0

* Sun Nov 22 2009 Funda Wang <fwang@mandriva.org> 8.4.13-1mdv2010.1
+ Revision: 468686
- rediff patches
- New version 8.4.13

* Sat May 02 2009 Funda Wang <fwang@mandriva.org> 8.4.12-1mdv2010.0
+ Revision: 370476
- New version 8.4.12

* Fri Apr 03 2009 Funda Wang <fwang@mandriva.org> 8.4.9-3mdv2009.1
+ Revision: 363647
- rebuild for missing packages

* Wed Apr 01 2009 Funda Wang <fwang@mandriva.org> 8.4.9-2mdv2009.1
+ Revision: 363346
- fix rpm group

* Tue Mar 10 2009 Funda Wang <fwang@mandriva.org> 8.4.9-1mdv2009.1
+ Revision: 353362
- New version 8.4.9

* Wed Dec 24 2008 Michael Scherer <misc@mandriva.org> 8.4.8-2mdv2009.1
+ Revision: 318446
- rebuild for new python

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Nov 27 2008 Funda Wang <fwang@mandriva.org> 8.4.8-1mdv2009.1
+ Revision: 307231
- fix file list
- BR intltool
- New version 8.4.8

* Sat Nov 08 2008 Anne Nicolas <ennael@mandriva.org> 8.4.6-4mdv2009.1
+ Revision: 300912
- Fix menus, new release

* Tue Sep 09 2008 Funda Wang <fwang@mandriva.org> 8.4.6-3mdv2009.0
+ Revision: 282900
- rebuild for gnet

* Mon Sep 08 2008 Funda Wang <fwang@mandriva.org> 8.4.6-2mdv2009.0
+ Revision: 282480
- singled out he voice

* Mon Sep 08 2008 Funda Wang <fwang@mandriva.org> 8.4.6-1mdv2009.0
+ Revision: 282471
- New version 8.4.6
- merge fedora patches

* Sun Jun 15 2008 Funda Wang <fwang@mandriva.org> 8.4.5-3mdv2009.0
+ Revision: 219269
- fix startup failur (bug#41084)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jun 11 2008 Funda Wang <fwang@mandriva.org> 8.4.5-2mdv2009.0
+ Revision: 217838
- rebuild for new rpm binary payload
- split out nn
- New version 8.4.5

* Sat Mar 15 2008 Funda Wang <fwang@mandriva.org> 8.4.4-2mdv2008.1
+ Revision: 188035
- BR libgstreamer-devel > 0.10.0
- requires devel(libgstreamer-0.10) for backporting
- split out bg and ur voices

* Thu Feb 14 2008 Erwan Velu <erwan@mandriva.org> 8.4.4-1mdv2008.1
+ Revision: 168614
- 8.4.4

  + Thierry Vignaud <tv@mandriva.org>
    - fix gstreamer0.10-devel BR for x86_64
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Dec 16 2007 Funda Wang <fwang@mandriva.org> 8.4.2-3mdv2008.1
+ Revision: 120528
- requires gstreamer-good

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 8.4.2-2mdv2008.1
+ Revision: 109180
- fix bug#35566: Bad package splitting
- cleanup file list

* Tue Oct 30 2007 Funda Wang <fwang@mandriva.org> 8.4.2-1mdv2008.1
+ Revision: 103953
- New version 8.4.2

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-ended-with-dot

* Sun Sep 23 2007 Funda Wang <fwang@mandriva.org> 8.4-2mdv2008.0
+ Revision: 92356
- Really requires gstreamer0.10
- should BR gstreamer0.10
- fix menu category

  + Erwan Velu <erwan@mandriva.org>
    - 8.4
    - Rebuild

* Fri Aug 17 2007 Funda Wang <fwang@mandriva.org> 8.3.3-1mdv2008.0
+ Revision: 65025
- New version 8.3.3

* Tue Aug 07 2007 Erwan Velu <erwan@mandriva.org> 8.3.2-1mdv2008.0
+ Revision: 59827
- 8.3.2
-Adding sr and el languages

  + Funda Wang <fwang@mandriva.org>
    - New version 8.3.2

  + Michael Scherer <misc@mandriva.org>
    - improve summary

  + Herton Ronaldo Krzesinski <herton@mandriva.com.br>
    - Removed old menu, placed icons in directories following
      freedesktop.org standard.

* Thu May 10 2007 Lenny Cartier <lenny@mandriva.org> 8.3.1-2mdv2008.0
+ Revision: 25948
- Fix xdg section

* Wed May 02 2007 Erwan Velu <erwan@mandriva.org> 8.3.1-1mdv2008.0
+ Revision: 20520
- Missing buildrequires
-Fixing typo
-Fixing category for gcompris
- Fixing XDG Menu
- Adding Hindi language
- oups typo
- Fixing buildrequires
- 8.3.1
- Fixing build for older python


* Sun Feb 18 2007 Erwan Velu <erwan@mandriva.org> 8.2.2-3mdv2007.0
+ Revision: 122560
- Adding missing requires

* Wed Jan 10 2007 Lenny Cartier <lenny@mandriva.com> 8.2.2-2mdv2007.1
+ Revision: 107062
- Fix menu & patch is for x86_64 only (thx JORGE Jose)

* Tue Dec 19 2006 Crispin Boylan <crisb@mandriva.org> 8.2.2-1mdv2007.1
+ Revision: 99892
- 8.2.2, fix x86_64 build
-Add xauth to buildreqs
- Update URL, xgvf reqs
- Remove unneeded gnome 1.x deps

* Wed Nov 15 2006 Lenny Cartier <lenny@mandriva.com> 8.2.1-1mdv2007.1
+ Revision: 84298
- Update to 8.2.1

* Mon Nov 06 2006 Erwan Velu <erwan@mandriva.org> 8.2-1mdv2007.1
+ Revision: 76870
- New version 8.2

  + Lenny Cartier <lenny@mandriva.com>
    - Update to 8.1
    - Import gcompris

* Fri Aug 11 2006 Lenny Cartier <lenny@mandriva.com> 7.4-2mdv2007.0
- rebuild

* Wed Apr 05 2006 Erwan Velu <erwan@seanodes.com> 7.4-1mdk
- 7.4

* Mon Feb 27 2006 Erwan Velu <erwan@seanodes.com> 7.3.2-1mdk
- 7.3.2

* Fri Feb 24 2006 Erwan Velu <erwan@seanodes.com> 7.3.1-1mdk
- Using official 7.3.1
- Fixing buildrequirres

* Mon Feb 20 2006 Erwan Velu <erwan@seanodes.com> 7.3-2mdk
- dapper.patch
- This is the same as 7.3.1

* Mon Feb 20 2006 Erwan Velu <erwan@seanodes.com> 7.3-1mdk
- 7.3

* Mon Dec 12 2005 Erwan Velu <erwan@seanodes.com> 7.2-1mdk
- 7.2
- Remove patch0 (merged upstream)

* Wed Nov 23 2005 Erwan Velu <erwan@seanodes.com> 7.1-2mdk
- Fixing some python troubles (thx to misc & yvesC)

* Sat Nov 19 2005 Erwan Velu <erwan@seanodes.com> 7.1-1mdk
- 7.1 final

* Sun Oct 30 2005 Erwan Velu <erwan@seanodes.com> 7.1-0.1mdk
- 7.1PRE1
- Adding Icons
- Renabling Configurator

* Tue Oct 11 2005 Erwan Velu <erwan@seanodes.com> 7.0.3-4mdk
- Fix BuildRequires

* Thu Oct 06 2005 Nicolas Lécureuil <neoclust@mandriva.org> 7.0.3-3mdk
- Fix BuildRequires

* Wed Oct 05 2005 Nicolas Lécureuil <neoclust@mandriva.org> 7.0.3-2mdk
- Fix BuildRequires

* Wed Oct 05 2005 Erwan Velu <erwan@seanodes.com> 7.0.3-1mdk
- 7.0.3

* Fri Sep 23 2005 Erwan Velu <erwan@seanodes.com> 7.0.2-1mdk
- 7.0.2

* Mon Sep 19 2005 Michael Scherer <misc@mandriva.org> 7.0.1-1mdk
- New release 7.0.1
- fix pygtk building ( Xvfb trick )
- remove gcompris_edit from the menu, use -a option
- remove redondant requires

* Wed Sep 14 2005 Erwan Velu <erwan@seanodes.com> 7.0.0-0.2mdk
- Fixing deps (thx to aginies)
- Adding mkrel (thx misc)

* Mon Sep 12 2005 Erwan Velu <erwan@seanodes.com> 7.0.0-0.1mdk
- 7.0.0PRE1
- Adding sv
- Moving assetml files to their respectives languages

* Tue Jun 21 2005 Erwan Velu <erwan@seanodes.com> 6.5.3-1mdk
- 6.5.3
- Adding "--without-editor" as bruno coudoin said

* Wed Apr 13 2005 Erwan Velu <erwan@seanodes.com> 6.5.2-1mdk
- 6.5.2

* Tue Mar 22 2005 Erwan Velu <erwan@seanodes.com> 6.5.1-1mdk
- 6.5.1

* Mon Mar 21 2005 Erwan Velu <erwan@seanodes.com> 6.5-1mdk
- 6.5.0

* Wed Mar 09 2005 Lenny Cartier <lenny@mandrakesoft.com> 6.5-0.pre2.2mdk
- requires librsvg

* Mon Feb 21 2005 Lenny Cartier <lenny@mandrakesoft.com> 6.5-0.pre2.1mdk
- 6.5PRE2

* Thu Jan 06 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 6.4-2mdk 
- Rebuild with latest howl

* Sun Dec 12 2004 Lenny Cartier <lenny@mandrakesoft.com> 6.4-1mdk
- 6.4

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 6.3-2mdk
- Rebuild for new python

* Wed Nov 10 2004 Lenny Cartier <lenny@mandrakesoft.com> 6.3-1mdk
- 6.3
- add ru and da subpackages

* Sun Jul 04 2004 Michael Scherer <misc@mandrake.org> 6.1-2mdk 
- fix Requires ( thanks José JORGE <jjorge@free.fr> )

* Mon Jun 21 2004 Michael Scherer <misc@mandrake.org> 6.1-1mdk
- New release 6.1

* Fri Jun 11 2004 Olivier Blin <blino@mandrake.org> 6.0-3mdk
- BuildRequires SDL_mixer-devel

* Sat May 29 2004 Michael Scherer <misc@mandrake.org> 6.0-2mdk 
- [DIRM]

* Thu May 27 2004 Michael Scherer <misc@mandrake.org> 6.0-1mdk
- New release 6.0
- split in library

* Tue Apr 13 2004 Michael Scherer <misc@mandrake.org> 5.2-1mdk
- New release 5.2
- rpmbuildupdate aware

