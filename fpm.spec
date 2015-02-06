%define	name	fpm
%define	version	0.60
%define release	11

Summary:	Figaro's Password Manager
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Graphical desktop/GNOME
License:	GPL
Source0:	%{name}-%{version}.tar.bz2
URL:		http://fpm.sourceforge.net/
Buildrequires:	gtk+-devel 
Buildrequires:  libgnome-devel
Buildrequires:  libxml2-devel
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
Figaro's Password Manager is a program that allows you to securely store the
passwords you use on the web.  Features include:
- Passwords are encrypted with the blowfish algorithm
- Copy passwords or usernames to the clipboard
- Copy passwords or usernames to the primary selection. (And paste them with a
  middle mouse button click)
- If the password is for a web site, FPM can keep track of the URLs of your
  login screens and can automatically launch your browser.  In this capacity,
  FPM acts as a kind of bookmark manager.
- Combine all three features: you can configure FPM to bring you to a web
  login screen, copy your username to the clipboard and your password to the
  primary selection, all with a single button click.
- FPM also has a passord generator that can choose passwords for you.  It
  allows you to determine how long the password should be, and what types of
  characters (lower case, upper case, numbers and symbols) should be used.
  You can even have it avoid ambiguous characters such as a capital O or the
  number zero.
         
%prep
%setup -q

%build
#./autogen.sh
CFLAGS="`xml2-config --cflags` $RPM_OPT_FLAGS" \
%configure
%make

%install
rm -rf %{buildroot}
%{makeinstall_std}

# menu

#xdg
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{summary}
Exec=%{name} 
Icon=other_archiving
Terminal=false
Type=Application
Categories=Utility;Archiving;
EOF


%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}/*
%_mandir/man1/*
%{_datadir}/applications/*



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.60-10mdv2011.0
+ Revision: 610745
- rebuild

* Sat May 01 2010 Funda Wang <fwang@mandriva.org> 0.60-9mdv2010.1
+ Revision: 541469
- fix desktop

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.60-9mdv2010.0
+ Revision: 437575
- rebuild

* Sat Mar 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.60-8mdv2009.1
+ Revision: 354771
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - Buildrequires xml2-devel for xml2-config
    - fix 'error: for key "Icon" in group "Desktop Entry" is an icon name with an
      extension, but there should be no extension as described in the Icon Theme
      Specification if the value is not an absolute path'
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
    - import fpm

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Aug 09 2006 Lenny Cartier <lenny@mandriva.com> 0.60-5mdv2007.0
- xdg

* Wed Apr 26 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.60-4mdk
- Fix BuildRequires

* Wed Apr 26 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.60-3mdk
- Fix BuildRequires

* Tue Jan 03 2006 Lenny Cartier <lenny@mandriva.com> 0.60-2mdk
- rebuild

* Sun Jul 25 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 0.60-1mdk
- 0.60
- update url
- cleanups

* Mon Oct 13 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.56-1mdk
- 0.56
