Summary:        Remote mail fetch daemon for POP2, POP3, APOP, IMAP
Summary(de):    Dämon zum Laden entfernter Mail (POP2, POP3, APOP, IMAP)
Summary(fr):    Démon de récupération du mail pour POP2, POP3, APOP, IMAP.
Summary(pl):    Zdalny demon pocztowy do protoko³ów POP2, POP3, APOP, IMAP
Summary(pt_BR): Busca mensagens de um servidor usando POP ou IMAP
Summary(tr):    POP2, POP3, APOP, IMAP protokolleri ile uzaktan mektup alma yazýlýmý
Name:           fetchmail
Version:        4.7.2
Release:        1
Copyright:      freely redistributable
Group:          Applications/Mail
Group(pt_BR):   Aplicações/Correio Eletrônico
Vendor:         Eric S. Raymond <esr@thyrsus.com>
Source:         ftp://locke.ccil.org/pub/esr/fetchmail/%{name}-%{version}.tar.gz
Icon:           fetchmail.gif
URL:            http://www.tuxedo.org/~esr/fetchmail
Requires:       smtpdaemon
Buildroot:      /tmp/%{name}-%{version}-root

%description
Fetchmail is a program that is used to retrieve mail from a remote mail
server. It can use the Post Office Protocol (POP) or IMAP (Internet Mail
Access Protocol) for this, and delivers the mail through the local SMTP
server (normally sendmail).

%description -l de                                                                                            
Fetchmail ist ein freies, vollständiges, robustes und wohldokumentiertes
Werkzeug zum Abholen und Weiterreichen von E-Mail, gedacht zum Gebrauchüber
temporäre TCP/IP-Verbindungen (wie z.B. SLIP- oder PPP-Verbindungen).  Es
holt E-Mail von (weit) entfernten Mail-Servern abund reicht sie an das
Auslieferungssystem der lokalen Client-Maschine weiter, damit sie dann von
normalen MUAs ("mail user agents") wie mutt, elm, pine, (x)emacs/gnus oder
mailx gelesen werden kann.  Ein interaktiver GUI-Konfigurator auch gut
geeignet zum Gebrauch durch Endbenutzer wird mitgeliefert.

%description -l fr
Fetchmail est un programme utilisé pour récupérer le mail depuis un serveur
distant. Il peut utiliser POP (Post Office Protocol) ou IMAP (Internet Mail
Access Protocol) pour cela, et achemine le courrier à travers le serveur
SMTP local (sendmail normal).

%description -l pl
Fetchmail jest programem do ¶ci±gania poczty ze zdalnych serwerów
pocztowych. Do ¶ci±gania poczty mo¿e on uzywaæ protoko³ów POP (Post Office
Protocol) lub IMAP (Internet Mail Access Protocol). ¦ci±gniêt± pocztê
dostarcza do koñcowych odbiorców poprzez lokalny serwer SMTP.

%description -l pt_BR
fetchmail é um programa que é usado para recuperar mensagens de um servidor
de mail remoto. Ele pode usar Post Office Protocol (POP) ou IMAP (Internet
Mail Access Protocol) para isso, e entrega o mail através do servidor local
SMTP (normalmente sendmail).

%description -l tr
fetchmail yazýlýmý, POP veya IMAP desteði veren bir sunucuda yer alan
mektuplarýnýzý alýr.

%package -n fetchmailconf
Summary:        A GUI configurator for generating fetchmail configuration files
Summary(pl):    GUI konfigurator do fetchmaila
Group:          Utilities/System
Requires:       %{name} = %{version}, python

%description -n fetchmailconf
A GUI configurator for generating fetchmail configuration file writen in
python

%description -n fetchmailconf -l pl 
GUI konfigurator do fetchmaila napisany w pythonie.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr \
	--enable-nls \
	--without-included-gettext

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/lib/rhs/control-panel}

make install prefix=$RPM_BUILD_ROOT/usr

install rh-config/*.{xpm,init} $RPM_BUILD_ROOT/usr/lib/rhs/control-panel                               
install rh-config/fetchmailconf.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/fetchmailconf
rm -f $RPM_BUILD_ROOT/usr/man/man1/fetchmailconf.1
echo ".so fetchmail.1" > $RPM_BUILD_ROOT/usr/man/man1/fetchmailconf.1

gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc FEATURES README NEWS NOTES *.html FAQ COPYING sample.rcfile
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/fetchmail.1.gz
%lang(pt) /usr/share/locale/pt*/LC_MESSAGES/fetchmail.mo

%files -n fetchmailconf
%defattr(644, root, root, 755)
/etc/X11/wmconfig/fetchmailconf
/usr/lib/rhs/control-panel/*
%attr(755, root, root) /usr/bin/fetchmailconf
%attr(644, root,  man) /usr/man/man1/fetchmailconf.1.gz

%changelog
* Mon Dec 28 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.7.1-1]
- added gzipping man pages,
- added pl translation,
- Vendor field to "Eric S. Raymond <esr@thyrsus.com>",
- added pt_BR and de translationc from Eric spec,
- added fetchmail.mo file with %lang macro,
- fetchmailconf(1) man page maked as nroff include to 
  fetchmail(1),
- removed INSTALL from %doc,
- added using LDFLAGS="-s" to ./configure enviroment,
- added "Requires: python" to fetchmailconf subpackage,
- added URL,
- added --enable-nls and --without-included-gettext to 
  ./configure parameters (libint is integrated in glibc),
- added full %attr description in %files.

* Wed Jul 22 1998 Jeff Johnson <jbj@redhat.com>
- update to 4.5.3.

* Fri May 08 1998 Cristian Gafton <gafton@redhat.com>
- fixed spelung eror in the decsriptoin

* Thu May 07 1998 Cristian Gafton <gafton@redhat.com>
- new version 4.4.4 fixes a lot of bugs

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 4.4.1
- buildroot

* Thu Oct 23 1997 Michael Fulbright <msf@redhat.com>
- Updated to 4.3.2 using SRPM from Eric Raymond

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
