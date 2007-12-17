%define	name	fpm
%define	version	0.60
%define	release	%mkrel 5

Summary:	Figaro's Password Manager
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Graphical desktop/GNOME
License:	GPL
Source0:	%{name}-%{version}.tar.bz2
URL:		http://fpm.sourceforge.net/
Buildrequires:	gtk+-devel 
Buildrequires:  automake1.8
Buildrequires:  libgnome-devel

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
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std} MKINSTALLDIRS=%{_datadir}/automake-1.9/mkinstalldirs

# menu
install -d $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="fpm" \
needs="x11" \
icon="other_archiving.png" \
section="System/Archiving/Other" \
title="Fpm" \
longtitle="Fpm password manager" \
xdg="true"
EOF

#xdg
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{Summary}
Exec=%{name} 
Icon=other_archiving.png
Terminal=false
Type=Application
Categories=X-MandrivaLinux-System-Archiving-Other;Archiving
EOF


%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}/*
%{_menudir}/%{name}
%_mandir/man1/*
%{_datadir}/applications/*
