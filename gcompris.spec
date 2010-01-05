%define name	gcompris
%define version 9.0
%define release %mkrel 1

Summary: An educational game for children starting at 2
Name: 	%name
Version: %version
Release: %release
License: GPLv2+
Group: Education
Source: http://prdownloads.sourceforge.net/gcompris/%name-%{version}.tar.gz
# trem : no more needed
# Patch0:         gcompris-8.4.13-icon.patch
# Patch1:         gcompris-9.0-tuxpaint-fullscreen.patch
Patch2:		gcompris-9.0-linkage.patch
BuildRoot: %_tmppath/%name-%version-buildroot
Buildrequires: gnuchess libogg-devel
Buildrequires: libxml2-devel libgnomeui2-devel
Buildrequires: libvorbis-devel libao-devel 
Buildrequires: imagemagick
BuildRequires: desktop-file-utils
BuildRequires: libgnet2-devel
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
BuildRequires: libgstreamer-devel >= 0.10.0
BuildRequires: intltool librsvg-devel
Requires:      %{name}-sound = %{version}-%{release}
# (misc) gnuchess for the chees activitie, gnome-python-canvas for python board
Requires:      gnuchess >= 5.02 
Requires:      python gnome-python gnome-python-canvas pygtk2.0 python-sqlite2
Requires:      librsvg tuxpaint
Requires:      gnucap gstreamer0.10-plugins-good
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
Group:          Education
Provides:       %{name}-music = %{version}
Conflicts:	%name < 8.4.2-2

%description music
Background music for gcompris.

%package sounds-ar
Summary:        Arabic (Tunisia) sounds for GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:	locales-ar
Conflicts:      %name < 8.4.2-2

%description sounds-ar
Arabic (Tunisia) sounds for gcompris.

%package sounds-bg
Summary:        Bulgarian sounds for GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:       locales-bg
Conflicts:      %name < 8.4.4-2

%description sounds-bg
Bulgarian sounds for gcompris.

%package sounds-br
Summary:        Breton sounds for GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:       locales-br
Conflicts:      %name < 8.4.2-2

%description sounds-br
Breton sounds for gcompris.

%package sounds-cs
Summary:        Czech sounds for GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:	locales-cs
Conflicts:      %name < 8.4.2-2

%description sounds-cs
Czech sounds for gcompris.

%package sounds-de
Summary:        German sounds for GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:	locales-de
Conflicts:      %name < 8.4.2-2

%description sounds-de
German sounds for gcompris.

%package sounds-da
Summary:        Danish sounds for GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:       locales-da
Conflicts:      %name < 8.4.2-2

%description sounds-da
Danish sounds for gcompris.

%package sounds-es
Summary:        Spanish sounds for GCompris
Group: 		Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:	locales-es
Conflicts:      %name < 8.4.2-2

%description sounds-es
Spanish sounds for gcompris.

%package sounds-el
Summary:        Greek sounds for GCompris
Group: 		Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:	locales-el
Conflicts:      %name < 8.4.2-2

%description sounds-el
Greek sounds for gcompris.

%package sounds-en
Summary:        English sounds for GCompris
Group: 		Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:	locales-en
Conflicts:      %name < 8.4.2-2

%description sounds-en
English sounds for gcompris.

%package sounds-eu
Summary:        Basque sounds for GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:       locales-eu
Conflicts:      %name < 8.4.2-2

%description sounds-eu
Basque sounds for gcompris.

%package sounds-fi
Summary:        Finnish sounds for GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:       locales-fi
Conflicts:      %name < 8.4.2-2

%description sounds-fi
Finnish sounds for gcompris.

%package sounds-fr
Summary:        French sounds for GCompris
Group: 		Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:	locales-fr
Conflicts:      %name < 8.4.2-2

%description sounds-fr
French sounds for gcompris.

%package sounds-he
Summary:        Hebrew soundsfor GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:       locales-he
Conflicts:      %name < 8.4.6-2

%description sounds-he
Hebrew sounds for gcompris.

%package sounds-hi
Summary:	Hindi soundsfor GCompris
Group:		Education
Requires:	%{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:	locales-hi
Conflicts:      %name < 8.4.2-2

%description sounds-hi
Hindi sounds for gcompris.

%package sounds-hu
Summary:        Hungarian sounds for GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:       locales-hu
Conflicts:      %name < 8.4.2-2

%description sounds-hu
Hungarian sounds for gcompris.

%package sounds-id
Summary:        Indonesian sounds for GCompris
Group: 		Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:	locales-id
Conflicts:      %name < 8.4.2-2

%description sounds-id
Indonesian sounds for gcompris.

%package sounds-it
Summary:        Italian sounds for GCompris
Group: 		Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:	locales-it
Conflicts:      %name < 8.4.2-2

%description sounds-it
Italian sounds for gcompris.

%package sounds-mr
Summary:        Marathi sounds for GCompris
Group: 		Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:	locales-mr
Conflicts:      %name < 8.4.2-2

%description sounds-mr
Marathi sounds for gcompris.

%package sounds-nb
Summary:        Norvegian Bokmal sounds for GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:       locales-no
Conflicts:      %name < 8.4.2-2

%description sounds-nb
Norvegian Bökmal sounds for gcompris.

%package sounds-nl
Summary:        Nederland sounds for GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:       locales-nl
Conflicts:      %name < 8.4.2-2

%description sounds-nl
Nederland sounds for gcompris.

%package sounds-nn
Summary:        Norvegian sounds for GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:       locales-nn

%description sounds-nn
Norvegian sounds for gcompris.

%package sounds-pa
Summary:        Punjabi sounds for GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:       locales-pa
Conflicts:      %name < 8.4.2-2

%description sounds-pa
Punjabi sounds for gcompris.

%package sounds-pt
Summary:        Portuguese sounds for GCompris
Group: 		Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:	locales-pt
Conflicts:      %name < 8.4.2-2

%description sounds-pt
Portuguese sounds for gcompris.

%package sounds-pt_BR
Summary:        Brasilian Portuguese sounds for GCompris
Group: 		Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:	locales-pt
Conflicts:      %name < 8.4.2-2

%description sounds-pt_BR
Brasilian Portuguese sounds for gcompris.

%package sounds-ru
Summary:        Russian sounds for GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:       locales-ru
Conflicts:      %name < 8.4.2-2

%description sounds-ru
Russian sounds for gcompris.

%package sounds-so
Summary:        Somalian sounds for GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:       locales-so
Conflicts:      %name < 8.4.2-2

%description sounds-so
Somalian sounds for gcompris.

%package sounds-sr
Summary:        Serbian sounds for GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:       locales-sr
Conflicts:      %name < 8.4.2-2

%description sounds-sr
Serbian sounds for gcompris.

%package sounds-sv
Summary:        Swedish sounds for GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:       locales-sv
Conflicts:      %name < 8.4.2-2

%description sounds-sv
Swedish sounds for gcompris.

%package sounds-tr
Summary:        Turkish sounds for GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:       locales-tr
Conflicts:      %name < 8.4.2-2

%description sounds-tr
Turkish sounds for gcompris.

%package sounds-ur
Summary:        Urdu sounds for GCompris
Group:          Education
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-sound = %{version}
Requires:       locales-ur
Conflicts:      %name < 8.4.4-1

%description sounds-ur
Urdu sounds for gcompris.

%prep
%setup -q -n %name-%{version}
# trem : no more needed
#patch0 -p1
#patch1 -p1
%patch2 -p1

%build
%ifarch alpha
  MYARCH_FLAGS="--host=alpha-redhat-linux"
%endif

%configure2_5x --enable-py-build-only --enable-gnet

# 6.0-1mdk, (misc)
# paralel build is broken
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#Fixing desktop file to match spec
perl -pi -e "s/Icon=.*/Icon=gcompris/g" $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
perl -pi -e "s/(Categories=).*/$1/" $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
perl -pi -e "s/Icon=.*/Icon=gcompris-edit/g" $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-edit.desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Education" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Education" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-edit.desktop

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
rm -f $RPM_BUILD_ROOT/%{_menudir}/%{name}

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post 
%if %mdkversion < 200900
%update_menus
%endif
%_install_info %{name}.info

%if %mdkversion < 200900
%postun 
%clean_menus
%endif

%preun
%_remove_install_info %{name}.info

%files -f  %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%_bindir/*
%_libdir/%{name}
%_datadir/applications/*
%_datadir/pixmaps/*
%{_iconsdir}/hicolor/*/apps/*
%_mandir/man6/*
%_infodir/*
%_datadir/%name
%_datadir/gnome/help/%{name}/eu/*
%exclude %_datadir/%{name}/boards/music
%exclude %_datadir/%{name}/boards/voices/ar
%exclude %_datadir/%{name}/boards/voices/bg
%exclude %_datadir/%{name}/boards/voices/br
%exclude %_datadir/%{name}/boards/voices/cs
%exclude %_datadir/%{name}/boards/voices/da
%exclude %_datadir/%{name}/boards/voices/de
%exclude %_datadir/%{name}/boards/voices/el
%exclude %_datadir/%{name}/boards/voices/en
%exclude %_datadir/%{name}/boards/voices/es
%exclude %_datadir/%{name}/boards/voices/eu
%exclude %_datadir/%{name}/boards/voices/fi
%exclude %_datadir/%{name}/boards/voices/fr
%exclude %_datadir/%{name}/boards/voices/he
%exclude %_datadir/%{name}/boards/voices/hi
%exclude %_datadir/%{name}/boards/voices/hu
%exclude %_datadir/%{name}/boards/voices/id
%exclude %_datadir/%{name}/boards/voices/it
%exclude %_datadir/%{name}/boards/voices/mr
%exclude %_datadir/%{name}/boards/voices/nb
%exclude %_datadir/%{name}/boards/voices/nn
%exclude %_datadir/%{name}/boards/voices/nl
%exclude %_datadir/%{name}/boards/voices/pa
%exclude %_datadir/%{name}/boards/voices/pt
%exclude %_datadir/%{name}/boards/voices/pt_BR
%exclude %_datadir/%{name}/boards/voices/ru
%exclude %_datadir/%{name}/boards/voices/so
%exclude %_datadir/%{name}/boards/voices/sr
%exclude %_datadir/%{name}/boards/voices/sv
%exclude %_datadir/%{name}/boards/voices/tr
%exclude %_datadir/%{name}/boards/voices/ur

%files music
%defattr(-, root, root)
%_datadir/%{name}/boards/music

%files sounds-ar
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/ar

%files sounds-bg
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/bg

%files sounds-br
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/br

%files sounds-cs
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/cs

%files sounds-da
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/da

%files sounds-de
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/de

%files sounds-el
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/el

%files sounds-en
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/en

%files sounds-eu
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/eu

%files sounds-es
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/es

%files sounds-fi
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/fi

%files sounds-fr
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/fr

%files sounds-he
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/he

%files sounds-hi
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/hi

%files sounds-hu
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/hu

%files sounds-id
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/id

%files sounds-it
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/it

%files sounds-mr
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/mr

%files sounds-nb
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/nb

%files sounds-nl
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/nl

%files sounds-nn
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/nn

%files sounds-pa
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/pa

%files sounds-pt
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/pt

%files sounds-pt_BR
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/pt_BR

%files sounds-ru
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/ru

%files sounds-so
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/so

%files sounds-sr
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/sr

%files sounds-sv
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/sv

%files sounds-tr
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/tr

%files sounds-ur
%defattr(-, root, root)
%_datadir/%{name}/boards/voices/ur
