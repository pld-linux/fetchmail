# TODO: kerberos5/gssapi support?
#
# Conditional build:
%bcond_without	ssl	# build without SSL support
#
Summary:	Remote mail fetch daemon for POP2, POP3, APOP, IMAP
Summary(da.UTF-8):	Alsidig POP/IMAP post-afhentnings dæmon
Summary(de.UTF-8):	Dämon zum Laden entfernter Mail (POP2, POP3, APOP, IMAP)
Summary(es.UTF-8):	Recolector de correo via POP/IMAP
Summary(fr.UTF-8):	Démon de récupération du mail pour POP2, POP3, APOP, IMAP
Summary(pl.UTF-8):	Zdalny demon pocztowy do protokołów POP2, POP3, APOP, IMAP
Summary(pt.UTF-8):	Busca mensagens de um servidor usando POP ou IMAP
Summary(ru.UTF-8):	Утилита извлечения почты с удаленной машины по протоколам POP/IMAP
Summary(tr.UTF-8):	POP2, POP3, APOP, IMAP protokolleri ile uzaktan mektup alma yazılımı
Summary(uk.UTF-8):	Утиліта отримання пошти з віддаленої машини по протоколам POP/IMAP
Summary(zh_CN.UTF-8):	功能强大的 POP/IMAP 电子邮件收取守护进程
Name:		fetchmail
Version:	6.3.11
Release:	2
License:	GPL
Group:		Applications/Mail
#Source0Download: http://developer.berlios.de/project/showfiles.php?group_id=1824
Source0:	http://download.berlios.de/fetchmail/%{name}-%{version}.tar.bz2
# Source0-md5:	43b28f296cc0024d3c727319eacae324
Source1:	%{name}conf.desktop
Source2:	%{name}.sysconfig
Source3:	%{name}.init
Source4:	%{name}.logrotate
Patch0:		%{name}-pl.po-update.patch
URL:		http://fetchmail.berlios.de/
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	lzma >= 1:4.42
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.7l}
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	setup >= 2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fetchmail is a program that is used to retrieve mail from a remote
mail server. It can use the Post Office Protocol (POP) or IMAP
(Internet Mail Access Protocol) for this, and delivers the mail
through the local SMTP server (normally sendmail).

%description -l da.UTF-8
Fetchmail er et gratis, robust, alsidigt og vel-dokumenteret værktøj
til afhentning og videresending af elektronisk post via TCP/IP
baserede opkalds-forbindelser (såsom SLIP eller PPP forbindelser). Den
henter post fra en ekstern post-server, og videresender den til din
lokale klient-maskines post-system, så den kan læses af almindelige
mail klienter såsom mutt, elm, pine, (x)emacs/gnus, eller mailx. Der
medfølger også et interaktivt GUI-baseret konfigurations-program, som
kan bruges af almindelige brugere.

%description -l de.UTF-8
Fetchmail ist ein freies, vollständiges, robustes und
wohldokumentiertes Werkzeug zum Abholen und Weiterreichen von E-Mail,
gedacht zum Gebrauchüber temporäre TCP/IP-Verbindungen (wie z.B. SLIP-
oder PPP-Verbindungen). Es holt E-Mail von (weit) entfernten
Mail-Servern abund reicht sie an das Auslieferungssystem der lokalen
Client-Maschine weiter, damit sie dann von normalen MUAs ("mail user
agents") wie mutt, elm, pine, (x)emacs/gnus oder mailx gelesen werden
kann. Ein interaktiver GUI-Konfigurator auch gut geeignet zum Gebrauch
durch Endbenutzer wird mitgeliefert.

%description -l es.UTF-8
Fetchmail es una utilidad gratis, completa, robusta y bien documentada
para la recepción y reeenvío de correo pensada para ser usada en co-
nexiones TCP/IP por demanda (como SLIP y PPP). Recibe el correo de
servidores remotos y lo reenvía al sistema de entrega local, siendo de
ese modo posible leerlo con programas como mutt, elm, pine,
(x)emacs/gnus o mailx. Contiene un configurador GUI interactivo
pensado para usuarios.

%description -l fr.UTF-8
Fetchmail est un programme utilisé pour récupérer le mail depuis un
serveur distant. Il peut utiliser POP (Post Office Protocol) ou IMAP
(Internet Mail Access Protocol) pour cela, et achemine le courrier à
travers le serveur SMTP local (sendmail normal).

%description -l pl.UTF-8
Fetchmail jest programem do ściągania poczty ze zdalnych serwerów
pocztowych. Do ściągania poczty może on używać protokołów POP (Post
Office Protocol) lub IMAP (Internet Mail Access Protocol). Ściągniętą
pocztę dostarcza odbiorcom poprzez lokalny serwer SMTP.

%description -l pt.UTF-8
fetchmail é um programa que é usado para recuperar mensagens de um
servidor de mail remoto. Ele pode usar Post Office Protocol (POP) ou
IMAP (Internet Mail Access Protocol) para isso, e entrega o mail
através do servidor local SMTP (normalmente sendmail).

%description -l ru.UTF-8
Fetchmail - это утилита извлечения почты с удаленной машины и
форвардинга, предназначенная для использования на on-demand TCP/IP
соединениях, таких как SLIP или PPP соеднения. Fetchmail поддерживает
все используемые в настоящее время в Инернете протоколы удаленной
почты (POP2, POP3, RPOP, APOP, KPOP, все IMAPы, ESMTP ETRN). Затем
Fetchmail форвардит извлеченную почту через SMTP, чтобы ви могли
прочитать ее своим любимым почтовым клиентом.

%description -l tr.UTF-8
fetchmail yazılımı, POP veya IMAP desteği veren bir sunucuda yer alan
mektuplarınızı alır.

%description -l uk.UTF-8
Fetchmail - це утиліта отримання пошти з віддаленої машини та
форвардингу, призначена для використання на on-demand TCP/IP
з'єднаннях, таких як SLIP чи PPP з'єднання. Fetchmail підтримує всі
використовувані на сьогодні протоколи віддаленої пошти (POP2, POP3,
RPOP, APOP, KPOP, всі IMAPи, ESMTP ETRN). Після отримання Fetchmail
форвардить пошту через SMTP, щоб ви могли прочитати її своїм улюбленим
поштовим клієнтом.

%package -n fetchmailconf
Summary:	A GUI configurator for generating fetchmail configuration files
Summary(es.UTF-8):	Configurador GUI interactivo por fetchmail
Summary(fr.UTF-8):	GUI configurateur pour fetchmail
Summary(pl.UTF-8):	Konfigurator GUI do fetchmaila
Summary(pt.UTF-8):	Um configurador gráfico para a criação de arquivos de configuração para o fetchmail
Summary(ru.UTF-8):	Графическая утилита для конфигурации предпочтений для fetchmail
Summary(uk.UTF-8):	Графічна утиліта для конфігурації вподобань для fetchmail
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	python
Requires:	python-tkinter

%description -n fetchmailconf
A GUI configurator for generating fetchmail configuration file written
in python.

%description -n fetchmailconf -l de.UTF-8
Ein interaktiver GUI-Konfigurator für fetchmail in python.

%description -n fetchmailconf -l es.UTF-8
Configurador gráfico para fetchmail escrito en python.

%description -n fetchmailconf -l pl.UTF-8
Konfigurator GUI do fetchmaila napisany w pythonie.

%description -n fetchmailconf -l pt.UTF-8
Um configurador gráfico para a criação de arquivos de configuração
para o fetchmail.

%description -n fetchmailconf -l ru.UTF-8
Fetchmailconf - это программа на Tcl/Tk для конфигурации вашего файла
предпочтений ~/.fetchmailrc.

%description -n fetchmailconf -l uk.UTF-8
Fetchmailconf - це програма на Tcl/Tk для конфігурації вашого файла
вподобань ~/.fetchmailrc.

%package daemon
Summary:	SysV init script for demonize fetchmail for sucking emails
Summary(pl.UTF-8):	Skrypt startowy SysV do uruchamiania systemowego fetchmaila jako demona
Group:		Applications/System
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Requires:	rc-scripts

%description daemon
SysV init script for demonize fetchmail for sucking emails.

%description daemon -l pl.UTF-8
Skrypt startowy SysV do uruchamiania systemowego fetchmaila jako
demona.

%prep
%setup -q
#%patch0 -p1

# to rebuild po/pl.gmo
rm -f po/stamp-po

%build
cp -f /usr/share/automake/config.* .
%configure \
	--enable-nls \
	--enable-RPA \
	--enable-NTLM \
	--enable-SDPS \
	%{?with_ssl:--with-ssl=%{_prefix}} \
	%{!?with_ssl:--without-ssl} \
	--without-kerberos
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig} \
	$RPM_BUILD_ROOT/etc/logrotate.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/fetchmail
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/fetchmail
install %{SOURCE4} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}

sed 's,\.py,\.pyc,' fetchmailconf > $RPM_BUILD_ROOT%{_bindir}/fetchmailconf

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/fetchmailconf.1
echo ".so fetchmail.1" > $RPM_BUILD_ROOT%{_mandir}/man1/fetchmailconf.1

> $RPM_BUILD_ROOT%{_sysconfdir}/fetchmailrc

%find_lang %{name}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post daemon
/sbin/chkconfig --add fetchmail
%service fetchmail restart "fetchmail daemon"

%preun daemon
if [ "$1" = "0" ]; then
	%service fetchmail stop
	/sbin/chkconfig --del fetchmail
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc FEATURES README NEWS NOTES README.NTLM *.html FAQ
%attr(755,root,root) %{_bindir}/fetchmail
%{_mandir}/man1/fetchmail.1*

%files -n fetchmailconf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fetchmailconf
%{_desktopdir}/fetchmailconf.desktop
%{_mandir}/man1/fetchmailconf.1*
%{py_sitescriptdir}/*.py[co]

%files daemon
%defattr(644,root,root,755)
%attr(600,root,root) %config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/fetchmailrc
%attr(754,root,root) /etc/rc.d/init.d/fetchmail
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/fetchmail
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/fetchmail
