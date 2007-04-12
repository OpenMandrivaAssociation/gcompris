%define name	gcompris
%define version 8.2.2
%define release %mkrel 3
%define libname %mklibname gcompris 1.0

Summary: GCompris
Name: 	%name
Version: %version
Release: %release
License: GPL
Group: Games/Other
Source: http://prdownloads.sourceforge.net/gcompris/%name-%{version}.tar.bz2
Patch1: gcompris-8.2.2.x86_64.patch
BuildRoot: %_tmppath/%name-%version-buildroot
Buildrequires: gnuchess libogg-devel
Buildrequires: libxml2-devel 
Buildrequires: libvorbis-devel libao-devel 
Buildrequires: ImageMagick
#Buildrequires: liblinc-devel 
# (misc) needed for python support
Buildrequires: gnome-python python-devel pygtk2.0-devel
Buildrequires: texinfo tetex-texi2html libassetml-devel
Buildrequires: SDL_mixer-devel 
# (misc) for the need of a display for pygtk
BuildRequires: x11-server-xvfb xauth
BuildRequires: perl-XML-Parser
BuildRequires: sqlite3-devel
BuildRequires: python-pyxml
BuildRequires: python-sqlite2
BuildRequires: libpopt-devel libgnomecanvas2-devel libgtk+2-devel
Requires:      %{name}-sound = %{version}
# (misc) gnuchess for the chees activitie, gnome-python-canvas for python board
Requires:      gnuchess >= 5.02 
Requires:      python gnome-python gnome-python-canvas pygtk2.0 python-sqlite2
Requires:      librsvg  tuxpaint
Requires:      %libname = %version
Requires:      gnucap
URL: http://www.gcompris.net

%description
An educationnal game for children starting at 2.
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

%package -n %{libname}
Summary:        GCompris library
Group: 		Games/Other
%description -n %{libname}
This is a library used by GCompris.

%package -n %{libname}-devel
Summary:        Development files for GCompris
Group: 		Games/Other
Requires:    %{libname} = %{version}
Provides:    libgcompris-devel
%description -n  %{libname}-devel
Development file for GCompris.

%package sounds-fr
Summary:        French sounds for GCompris
Group: 		Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:	locales-fr

%description sounds-fr
French sounds for gcompris.

%package sounds-es
Summary:        Spanish sounds for GCompris
Group: 		Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:	locales-es

%description sounds-es
Spanish sounds for gcompris.

%package sounds-de
Summary:        German sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:	locales-de

%description sounds-de
German sounds for gcompris.

%package sounds-en
Summary:        English sounds for GCompris
Group: 		Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:	locales-en

%description sounds-en
English sounds for gcompris.

%package sounds-it
Summary:        Italian sounds for GCompris
Group: 		Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:	locales-it

%description sounds-it
Italian sounds for gcompris.

%package sounds-pt
Summary:        Portuguese sounds for GCompris
Group: 		Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:	locales-pt

%description sounds-pt
Portuguese sounds for gcompris.

%package sounds-da
Summary:        Danish sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:       locales-da

%description sounds-da
Danish sounds for gcompris.

%package sounds-ru
Summary:        Russian sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:       locales-ru

%description sounds-ru
Russian sounds for gcompris.

%package sounds-sv
Summary:        Swedish sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:       locales-sv

%description sounds-sv
Swedish sounds for gcompris.

%package sounds-eu
Summary:        Basque sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:       locales-eu

%description sounds-eu
Basque sounds for gcompris.

%package sounds-hu
Summary:        Hungarian sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:       locales-hu

%description sounds-hu
Hungarian sounds for gcompris.

%package sounds-fi
Summary:        Finnish sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:       locales-fi

%description sounds-fi
Finnish sounds for gcompris.

%package sounds-nl
Summary:        Nederland sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:       locales-nl

%description sounds-nl
Nederland sounds for gcompris.

%package sounds-so
Summary:        Somalian sounds for GCompris
Group:          Games/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sound = %{version}
Requires:       locales-so

%description sounds-so
Somalian sounds for gcompris.

%prep
%setup -q -n %name-%{version}

%ifarch x86_64
%patch1 -p1 -b .x86_64
%endif

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

(cd $RPM_BUILD_ROOT
mkdir -p ./%{_menudir}

cat > ./%{_menudir}/%{name} <<EOF
?package(%{name}): \
command="%{_bindir}/%{name}" \
title="Gcompris" \
longtitle="Educational game" \
icon="%{name}.png" \
needs="x11" \
section="More Applications/Education/Other" \
xdg="true"
?package(%{name}): \
command="%{_bindir}/%{name} -a" \
title="Gcompris administration" \
longtitle="Administration module of gcompris" \
icon="%{name}.png" \
needs="x11" \
section="More Applications/Education/Other" \
xdg="true"
EOF

)

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{Summary}
Exec=%{name} 
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Education-Other;
EOF

cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}-administration.desktop << EOF
[Desktop Entry]
Name="Gcompris administration"
Comment="Administration module of gcompris"
Exec=%{name} -a
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Education-Other;Art
EOF


# install icons
mkdir -p $RPM_BUILD_ROOT{%{_liconsdir},%{_miconsdir},%{_iconsdir}}
cp %{name}.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
convert -scale 32x32 %{name}.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert -scale 16x16 %{name}.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

 
%find_lang %name
find $RPM_BUILD_ROOT/%_datadir/%{name}/ -type d | grep -v sounds | sed 's|'$RPM_BUILD_ROOT'\(.*\)|%dir "\1" |' > %{name}.dir
find $RPM_BUILD_ROOT/%_datadir/%{name}/ -type f | grep -v sounds | sed 's|'$RPM_BUILD_ROOT'\(.*\)|"\1"|' > %{name}.files
find $RPM_BUILD_ROOT/%_datadir/%{name}/boards/sounds/ -type f -maxdepth 1 | sed 's|'$RPM_BUILD_ROOT'||' >> %{name}.files

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

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -f  %{name}.all
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%_bindir/*
%_libdir/%{name}/
%_datadir/applications/*
%_datadir/gnome/help/%{name}/*
%_datadir/%name/boards/flags/*
%_datadir/%name/boards/sounds/chronos
%_datadir/%name/boards/sounds/melody/
%_datadir/%name/boards/sounds/LuneRouge/
%_datadir/%name/boards/sounds/memory/
%_datadir/%name/boards/sounds/cs/
%_datadir/%name/boards/sounds/mr/
%_datadir/%name/boards/sounds/pt_BR/
%_datadir/%name/boards/sounds/tr/
%_datadir/pixmaps/*
%_menudir/*
%_infodir/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%_mandir/man6/*

%files sounds-de
%defattr(-, root, root)
%_datadir/%{name}/boards/sounds/de/*
%dir %_datadir/%{name}/boards/sounds/de

%files sounds-en
%defattr(-, root, root)
%_datadir/%{name}/boards/sounds/en/*
%dir %_datadir/%{name}/boards/sounds/en

%files sounds-es
%defattr(-, root, root)
%_datadir/%{name}/boards/sounds/es/*
%dir %_datadir/%{name}/boards/sounds/es

%files sounds-fr
%defattr(-, root, root)
%_datadir/%{name}/boards/sounds/fr/*
%dir %_datadir/%{name}/boards/sounds/fr

%files sounds-pt
%defattr(-, root, root)
%_datadir/%{name}/boards/sounds/pt/*
%dir %_datadir/%{name}/boards/sounds/pt

%files sounds-it
%defattr(-, root, root)
%_datadir/%{name}/boards/sounds/it/*
%dir %_datadir/%{name}/boards/sounds/it

%files sounds-da
%defattr(-, root, root)
%_datadir/%{name}/boards/sounds/da/*
%dir %_datadir/%{name}/boards/sounds/da

%files sounds-ru
%defattr(-, root, root)
%_datadir/%{name}/boards/sounds/ru/*
%dir %_datadir/%{name}/boards/sounds/ru

%files sounds-sv
%defattr(-, root, root)
%_datadir/%{name}/boards/sounds/sv/*
%dir %_datadir/%{name}/boards/sounds/sv

%files sounds-eu
%defattr(-, root, root)
%_datadir/%{name}/boards/sounds/eu/*
%dir %_datadir/%{name}/boards/sounds/eu

%files sounds-hu
%defattr(-, root, root)
%_datadir/%{name}/boards/sounds/hu/*
%dir %_datadir/%{name}/boards/sounds/hu

%files sounds-fi
%defattr(-, root, root)
%_datadir/%{name}/boards/sounds/fi/*
%dir %_datadir/%{name}/boards/sounds/fi

%files sounds-nl
%defattr(-, root, root)
%_datadir/%{name}/boards/sounds/nl/*
%dir %_datadir/%{name}/boards/sounds/nl

%files sounds-so
%defattr(-, root, root)
%_datadir/%{name}/boards/sounds/so/*
%dir %_datadir/%{name}/boards/sounds/so


%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/*so.*

%files -n %{libname}-devel
%defattr(-, root, root)
%{_includedir}/libgcompris-1.0/
%{_libdir}/pkgconfig/*
%{_libdir}/*so
%{_libdir}/*la


