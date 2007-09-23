%define name	gcompris
%define version 8.4
%define release %mkrel 2

Summary: An educational game for children starting at 2.
Name: 	%name
Version: %version
Release: %release
License: GPL
Group: Games/Other
Source: http://prdownloads.sourceforge.net/gcompris/%name-%{version}.tar.bz2
BuildRoot: %_tmppath/%name-%version-buildroot
Buildrequires: gnuchess libogg-devel
Buildrequires: libxml2-devel libgnomeui2-devel
Buildrequires: libvorbis-devel libao-devel 
Buildrequires: ImageMagick
BuildRequires: desktop-file-utils
# (misc) needed for python support
Buildrequires: gnome-python python-devel pygtk2.0-devel
Buildrequires: texinfo tetex-texi2html libassetml-devel
# (misc) for the need of a display for pygtk
BuildRequires: x11-server-xvfb xauth
BuildRequires: perl-XML-Parser
BuildRequires: sqlite3-devel
BuildRequires: python-pyxml
BuildRequires: python-sqlite2
BuildRequires: libgtk+2-devel
# (misc) for fullscreen support, now it is done with xvidmode instead of xrandr
BuildRequires: libxxf86vm-devel
BuildRequires: gstreamer-devel
Requires:      %{name}-sound = %{version}
# (misc) gnuchess for the chees activitie, gnome-python-canvas for python board
Requires:      gnuchess >= 5.02 
Requires:      python gnome-python gnome-python-canvas pygtk2.0 python-sqlite2
Requires:      librsvg  tuxpaint
Requires:      gnucap gstreamer
# until 8.3 version, gcompris came with libraries
Obsoletes:     libgcompris1.0
URL: http://www.gcompris.net

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
Summary:        Background music for GCompris
Group:          Games/Other
Provides:       %{name}-music = %{version}

%description music
Background music for gcompris.

%package sounds-ar
Summary:        Arabic (Tunisia) sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:	locales-cs

%description sounds-ar
Arabic (Tunisia) sounds for gcompris.

%package sounds-cs
Summary:        Czech sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:	locales-cs

%description sounds-cs
Czech sounds for gcompris.

%package sounds-de
Summary:        German sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:	locales-de

%description sounds-de
German sounds for gcompris.

%package sounds-da
Summary:        Danish sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:       locales-da

%description sounds-da
Danish sounds for gcompris.

%package sounds-es
Summary:        Spanish sounds for GCompris
Group: 		Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:	locales-es

%description sounds-es
Spanish sounds for gcompris.

%package sounds-el
Summary:        Greek sounds for GCompris
Group: 		Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:	locales-el

%description sounds-el
Greek sounds for gcompris.

%package sounds-en
Summary:        English sounds for GCompris
Group: 		Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:	locales-en

%description sounds-en
English sounds for gcompris.

%package sounds-eu
Summary:        Basque sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:       locales-eu

%description sounds-eu
Basque sounds for gcompris.

%package sounds-fi
Summary:        Finnish sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:       locales-fi

%description sounds-fi
Finnish sounds for gcompris.

%package sounds-fr
Summary:        French sounds for GCompris
Group: 		Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:	locales-fr

%description sounds-fr
French sounds for gcompris.

%package sounds-hi
Summary:	Hindi soundsfor GCompris
Group:		Games/Other
Requires:	%{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:	locales-hi

%description sounds-hi
Hindi sounds for gcompris.

%package sounds-hu
Summary:        Hungarian sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:       locales-hu

%description sounds-hu
Hungarian sounds for gcompris.

%package sounds-id
Summary:        Indonesian sounds for GCompris
Group: 		Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:	locales-id

%description sounds-id
Indonesian sounds for gcompris.

%package sounds-it
Summary:        Italian sounds for GCompris
Group: 		Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:	locales-it

%description sounds-it
Italian sounds for gcompris.

%package sounds-mr
Summary:        Marathi sounds for GCompris
Group: 		Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:	locales-mr

%description sounds-mr
Marathi sounds for gcompris.

%package sounds-nb
Summary:        Norvegian Bokmal sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:       locales-no

%description sounds-nb
Norvegian Bökmal sounds for gcompris.

%package sounds-nl
Summary:        Nederland sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:       locales-nl

%description sounds-nl
Nederland sounds for gcompris.

%package sounds-pt
Summary:        Portuguese sounds for GCompris
Group: 		Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:	locales-pt

%description sounds-pt
Portuguese sounds for gcompris.

%package sounds-pt_BR
Summary:        Brasilian Portuguese sounds for GCompris
Group: 		Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:	locales-pt

%description sounds-pt_BR
Brasilian Portuguese sounds for gcompris.

%package sounds-ru
Summary:        Russian sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:       locales-ru

%description sounds-ru
Russian sounds for gcompris.

%package sounds-so
Summary:        Somalian sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:       locales-so

%description sounds-so
Somalian sounds for gcompris.

%package sounds-sr
Summary:        Serbian sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:       locales-sr

%description sounds-sr
Serbian sounds for gcompris.

%package sounds-sv
Summary:        Swedish sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:       locales-sv

%description sounds-sv
Swedish sounds for gcompris.

%package sounds-tr
Summary:        Turkish sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:       locales-tr

%description sounds-tr
Turkish sounds for gcompris.

%prep
%setup -q -n %name-%{version}

rm -rf boards/*.rej

%build
%ifarch alpha
  MYARCH_FLAGS="--host=alpha-redhat-linux"
%endif
XDISPLAY=$(i=2; while [ -f /tmp/.X$i-lock ]; do i=$(($i+1)); done; echo $i)
%{_prefix}/bin/Xvfb :$XDISPLAY &
export DISPLAY=:$XDISPLAY
xauth add $DISPLAY . EE

%configure

# 6.0-1mdk, (misc)
# paralel build is broken
make
#kill $(cat /tmp/.X$XDISPLAY-lock)

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#Fixing desktop file to match spec
perl -pi -e "s/Icon=.*/Icon=gcompris/g" $RPM_BUILD_ROOT%{_datadir}/applications/gcompris.desktop
perl -pi -e "s/Icon=.*/Icon=gcompris-edit/g" $RPM_BUILD_ROOT%{_datadir}/applications/gcompris-edit.desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Game" \
  --add-category="KidsGame" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/gcompris.desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Game" \
  --add-category="KidsGame" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/gcompris-edit.desktop

# install icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
install -m 644 gcompris{,-edit}.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/
for size in 16x16 32x32; do
	convert -scale $size gcompris.png \
		$RPM_BUILD_ROOT%{_iconsdir}/hicolor/$size/apps/gcompris.png
	convert -scale $size gcompris-edit.png \
		$RPM_BUILD_ROOT%{_iconsdir}/hicolor/$size/apps/gcompris-edit.png
done

# remove unwanted files
rm -f $RPM_BUILD_ROOT/%{_menudir}/gcompris

%find_lang %name
find $RPM_BUILD_ROOT/%_datadir/%{name}/ -type d | grep -v sounds | grep -v music/background | sed 's|'$RPM_BUILD_ROOT'\(.*\)|%dir "\1" |' > %{name}.dir
find $RPM_BUILD_ROOT/%_datadir/%{name}/ -type f | grep -v sounds | grep -v music/background | sed 's|'$RPM_BUILD_ROOT'\(.*\)|"\1"|' > %{name}.files
find $RPM_BUILD_ROOT/%_datadir/%{name}/boards/voices/ -type f -maxdepth 1 | sed 's|'$RPM_BUILD_ROOT'||' >> %{name}.files

perl -pi -e 's|#searace1player.xml#||g' %{name}.files
cat  %{name}.files %{name}.lang > %{name}.all
rm -rf $RPM_BUILD_ROOT/%_datadir/locale/*/LC_MESSAGES/*GETTEXT*

%clean
rm -rf $RPM_BUILD_ROOT

%post 
%update_menus
%_install_info %{name}.info

%postun 
%clean_menus

%preun
%_remove_install_info %{name}.info

%files -f  %{name}.all
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%_bindir/*
%_libdir/%{name}/
%_datadir/applications/*
%_datadir/gnome/help/%{name}/*
%_datadir/%name/boards/sounds/*
%_datadir/%name/boards/sounds/chronos
%_datadir/%name/boards/sounds/melody/
%_datadir/%name/boards/sounds/LuneRouge/
%_datadir/%name/boards/sounds/memory/
%_datadir/pixmaps/*
%_infodir/*
%{_iconsdir}/hicolor/*/apps/gcompris.png
%{_iconsdir}/hicolor/*/apps/gcompris-edit.png
%_mandir/man6/*

%files music
%defattr(-, root, root)
%_datadir/%{name}/boards/music/*
%dir %_datadir/%{name}/boards/music/background

%files sounds-ar
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/ar/*
%dir %_datadir/%{name}/boards/voices/ar

%files sounds-cs
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/cs/*
%dir %_datadir/%{name}/boards/voices/cs

%files sounds-da
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/da/*
%dir %_datadir/%{name}/boards/voices/da

%files sounds-de
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/de/*
%dir %_datadir/%{name}/boards/voices/de

%files sounds-el
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/el/*
%dir %_datadir/%{name}/boards/voices/el

%files sounds-en
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/en/*
%dir %_datadir/%{name}/boards/voices/en

%files sounds-eu
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/eu/*
%dir %_datadir/%{name}/boards/voices/eu

%files sounds-es
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/es/*
%dir %_datadir/%{name}/boards/voices/es

%files sounds-fi
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/fi/*
%dir %_datadir/%{name}/boards/voices/fi

%files sounds-fr
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/fr/*
%dir %_datadir/%{name}/boards/voices/fr

%files sounds-hi
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/hi/*
%dir %_datadir/%{name}/boards/voices/hi

%files sounds-hu
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/hu/*
%dir %_datadir/%{name}/boards/voices/hu

%files sounds-id
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/id/*
%dir %_datadir/%{name}/boards/voices/id

%files sounds-it
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/it/*
%dir %_datadir/%{name}/boards/voices/it

%files sounds-mr
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/mr/*
%dir %_datadir/%{name}/boards/voices/mr

%files sounds-nb
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/nb/*
%dir %_datadir/%{name}/boards/voices/nb

%files sounds-nl
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/nl/*
%dir %_datadir/%{name}/boards/voices/nl

%files sounds-pt
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/pt/*
%dir %_datadir/%{name}/boards/voices/pt

%files sounds-pt_BR
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/pt_BR/*
%dir %_datadir/%{name}/boards/voices/pt_BR

%files sounds-ru
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/ru/*
%dir %_datadir/%{name}/boards/voices/ru

%files sounds-so
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/so/*
%dir %_datadir/%{name}/boards/voices/so

%files sounds-sr
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/sr/*
%dir %_datadir/%{name}/boards/voices/sr

%files sounds-sv
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/sv/*
%dir %_datadir/%{name}/boards/voices/sv

%files sounds-tr
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/tr/*
%dir %_datadir/%{name}/boards/voices/tr

