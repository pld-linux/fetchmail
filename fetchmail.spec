Summary:	Remote mail fetch daemon for POP2, POP3, APOP, IMAP
Summary(da):	Alsidig POP/IMAP post-afhentnings dæmon
Summary(de):	Dämon zum Laden entfernter Mail (POP2, POP3, APOP, IMAP)
Summary(es):	Recolector de correo via POP/IMAP
Summary(fr):	Démon de récupération du mail pour POP2, POP3, APOP, IMAP
Summary(pl):	Zdalny demon pocztowy do protoko³ów POP2, POP3, APOP, IMAP
Summary(pt):	Busca mensagens de um servidor usando POP ou IMAP
Summary(tr):	POP2, POP3, APOP, IMAP protokolleri ile uzaktan mektup alma yazýlýmý
Name:		fetchmail
Version:	5.4.3
Release:	1
License:	GPL
Group:		Applications/Mail
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Vendor:		Eric S. Raymond <esr@thyrsus.com>
Source0:	ftp://locke.ccil.org/pub/esr/fetchmail/%{name}-%{version}.tar.gz
Source1:	fetchmailconf.desktop
Source2:	fetchmail.sysconfig
Source3:	fetchmail.init
Patch0:		fetchmail-DESTDIR.patch
Patch1:		fetchmail-strcasemp.patch
Icon:		fetchmail.gif
URL:		http://www.tuxedo.org/~esr/fetchmail/
BuildRequires:	openssl-devel >= 0.9.4-2
BuildRequires:	gettext-devel
Requires:	smtpdaemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fetchmail is a program that is used to retrieve mail from a remote
mail server. It can use the Post Office Protocol (POP) or IMAP
(Internet Mail Access Protocol) for this, and delivers the mail
through the local SMTP server (normally sendmail).

%description -l da
Fetchmail er et gratis, robust, alsidigt og vel-dokumenteret værktøj
til afhentning og videresending af elektronisk post via TCP/IP
baserede opkalds-forbindelser (såsom SLIP eller PPP forbindelser). Den
henter post fra en ekstern post-server, og videresender den til din
lokale klient-maskines post-system, så den kan læses af almindelige
mail klienter såsom mutt, elm, pine, (x)emacs/gnus, eller mailx. Der
medfølger også et interaktivt GUI-baseret konfigurations-program, som
kan bruges af almindelige brugere.

%description -l de
Fetchmail ist ein freies, vollständiges, robustes und
wohldokumentiertes Werkzeug zum Abholen und Weiterreichen von E-Mail,
gedacht zum Gebrauchüber temporäre TCP/IP-Verbindungen (wie z.B. SLIP-
oder PPP-Verbindungen). Es holt E-Mail von (weit) entfernten
Mail-Servern abund reicht sie an das Auslieferungssystem der lokalen
Client-Maschine weiter, damit sie dann von normalen MUAs ("mail user
agents") wie mutt, elm, pine, (x)emacs/gnus oder mailx gelesen werden
kann. Ein interaktiver GUI-Konfigurator auch gut geeignet zum Gebrauch
durch Endbenutzer wird mitgeliefert.

%description -l es
Fetchmail es una utilidad gratis, completa, robusta y bien documentada
para la recepción y reeenvío de correo pensada para ser usada en co-
nexiones TCP/IP por demanda (como SLIP y PPP). Recibe el correo de
servidores remotos y lo reenvía al sistema de entrega local, siendo de
ese modo posible leerlo con programas como mutt, elm, pine,
(x)emacs/gnus o mailx. Contiene un configurador GUI interactivo
pensado para usuarios.

%description -l fr
Fetchmail est un programme utilisé pour récupérer le mail depuis un
serveur distant. Il peut utiliser POP (Post Office Protocol) ou IMAP
(Internet Mail Access Protocol) pour cela, et achemine le courrier à
travers le serveur SMTP local (sendmail normal).

%description -l pl
Fetchmail jest programem do ¶ci±gania poczty ze zdalnych serwerów
pocztowych. Do ¶ci±gania poczty mo¿e on u¿ywaæ protoko³ów POP (Post
Office Protocol) lub IMAP (Internet Mail Access Protocol). ¦ci±gniêt±
pocztê dostarcza odbiorcom poprzez lokalny serwer SMTP.

%description -l pt
fetchmail é um programa que é usado para recuperar mensagens de um
servidor de mail remoto. Ele pode usar Post Office Protocol (POP) ou
IMAP (Internet Mail Access Protocol) para isso, e entrega o mail
através do servidor local SMTP (normalmente sendmail).

%description -l tr
fetchmail yazýlýmý, POP veya IMAP desteði veren bir sunucuda yer alan
mektuplarýnýzý alýr.

%package -n fetchmailconf
Summary:	A GUI configurator for generating fetchmail configuration files
Summary(es):	Configurador GUI interactivo por fetchmail
Summary(fr):	GUI configurateur pour fetchmail
Summary(pl):	GUI konfigurator do fetchmaila
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	%{name} = %{version}
Requires:	python
Requires:	tkinter

%description -n fetchmailconf
A GUI configurator for generating fetchmail configuration file writen
in python.

%description -n fetchmailconf -l de
Ein interaktiver GUI-Konfigurator für fetchmail in python.

%description -n fetchmailconf -l es
Configurador gráfico para fetchmail escrito en python.

%description -n fetchmailconf -l pl 
GUI konfigurator do fetchmaila napisany w pythonie.

%package daemon
Summary:	SySV init script for demonize fetchmail for sucking emails
Summary(pl):	SySV init skrypt do uruchamiania systemowego fetchmaila jako daemon
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	%{name} = %{version}
Requires:	rc-scripts >= 0.2.0

%description daemon
SySV init script for demonize fetchmail for sucking emails.

%description -l pl daemon
SySV init skrypt do uruchamiania systemowego fetchmaila jako daemon.

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
chmod -R u+w *
gettextize --copy --force
aclocal
autoconf
LDFLAGS="-s"; export LDFLAGS
CFLAGS="$RPM_OPT_FLAGS -DSSL_ENABLE"
%configure \
	--enable-nls \
	--without-included-gettext \
	--enable-inet6 \
	--enable-RPA \
	--enable-NTLM \
	--enable-SDPS \
	--with-ssl=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/rhs/control-panel \
	$RPM_BUILD_ROOT%{_applnkdir}/Administration \
$RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install rh-config/*.{xpm,init} $RPM_BUILD_ROOT%{_libdir}/rhs/control-panel
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Administration
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/fetchmail
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/fetchmail

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	FEATURES README NEWS NOTES *.html FAQ

touch $RPM_BUILD_ROOT%{_sysconfdir}/fetchmailrc

%find_lang %{name}

%post daemon
/sbin/chkconfig --add fetchmail
if [ -f /var/lock/subsys/fetchmail ]; then
	/etc/rc.d/init.d/fetchmail restart >&2
else
	echo "Run \"/etc/rc.d/init.d/fetchmail start\" to start fetchamil daemon."
fi

%preun daemon
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/fetchmail ]; then
		/etc/rc.d/init.d/fetchmail stop >&2
	fi
	/sbin/chkconfig --del fetchmail
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz sample.rcfile

%attr(755,root,root) %{_bindir}/fetchmail
%{_mandir}/man1/fetchmail.1*

%files -n fetchmailconf
%defattr(644,root,root,755)
%{_libdir}/rhs/control-panel/*
%attr(755,root,root) %{_bindir}/fetchmailconf
%{_mandir}/man1/fetchmailconf.1*

%{_applnkdir}/Administration/fetchmailconf.desktop

%files daemon
%defattr(644,root,root,755)
%attr(600,root,root) %config(noreplace,missingok) %{_sysconfdir}/fetchmailrc
%attr(754,root,root) /etc/rc.d/init.d/fetchmail
%attr(640,root,root) %config(noreplace) /etc/sysconfig/fetchmail
