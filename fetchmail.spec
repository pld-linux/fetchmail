Summary:	Remote mail fetch daemon for POP2, POP3, APOP, IMAP
Summary(da):	Alsidig POP/IMAP post-afhentnings dæmon
Summary(de):	Dämon zum Laden entfernter Mail (POP2, POP3, APOP, IMAP)
Summary(es):	Recolector de correo via POP/IMAP
Summary(fr):	Démon de récupération du mail pour POP2, POP3, APOP, IMAP
Summary(pl):	Zdalny demon pocztowy do protoko³ów POP2, POP3, APOP, IMAP
Summary(pt):	Busca mensagens de um servidor usando POP ou IMAP
Summary(ru):	õÔÉÌÉÔÁ ÉÚ×ÌÅÞÅÎÉÑ ÐÏÞÔÙ Ó ÕÄÁÌÅÎÎÏÊ ÍÁÛÉÎÙ ÐÏ ÐÒÏÔÏËÏÌÁÍ POP/IMAP
Summary(tr):	POP2, POP3, APOP, IMAP protokolleri ile uzaktan mektup alma yazýlýmý
Summary(uk):	õÔÉÌ¦ÔÁ ÏÔÒÉÍÁÎÎÑ ÐÏÛÔÉ Ú ×¦ÄÄÁÌÅÎÏ§ ÍÁÛÉÎÉ ÐÏ ÐÒÏÔÏËÏÌÁÍ POP/IMAP
Summary(zh_CN):	¹¦ÄÜÇ¿´óµÄ POP/IMAP µç×ÓÓÊ¼þÊÕÈ¡ÊØ»¤½ø³Ì
Name:		fetchmail
Version:	6.2.4
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://catb.org/~esr/fetchmail/%{name}-%{version}.tar.gz
# Source0-md5:	3614acbda936548d2f8d5bffb161ff59
Source1:	%{name}conf.desktop
Source2:	%{name}.sysconfig
Source3:	%{name}.init
Source4:	%{name}.logrotate
Patch0:		%{name}-pl.po-update.patch
Icon:		fetchmail.gif
URL:		http://www.tuxedo.org/~esr/fetchmail/
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
%{!?_without_ssl:BuildRequires:	openssl-devel >= 0.9.6j}
Requires:	setup >= 2.3
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

%description -l ru
Fetchmail - ÜÔÏ ÕÔÉÌÉÔÁ ÉÚ×ÌÅÞÅÎÉÑ ÐÏÞÔÙ Ó ÕÄÁÌÅÎÎÏÊ ÍÁÛÉÎÙ É
ÆÏÒ×ÁÒÄÉÎÇÁ, ÐÒÅÄÎÁÚÎÁÞÅÎÎÁÑ ÄÌÑ ÉÓÐÏÌØÚÏ×ÁÎÉÑ ÎÁ on-demand TCP/IP
ÓÏÅÄÉÎÅÎÉÑÈ, ÔÁËÉÈ ËÁË SLIP ÉÌÉ PPP ÓÏÅÄÎÅÎÉÑ. Fetchmail ÐÏÄÄÅÒÖÉ×ÁÅÔ
×ÓÅ ÉÓÐÏÌØÚÕÅÍÙÅ × ÎÁÓÔÏÑÝÅÅ ×ÒÅÍÑ × éÎÅÒÎÅÔÅ ÐÒÏÔÏËÏÌÙ ÕÄÁÌÅÎÎÏÊ
ÐÏÞÔÙ (POP2, POP3, RPOP, APOP, KPOP, ×ÓÅ IMAPÙ, ESMTP ETRN). úÁÔÅÍ
Fetchmail ÆÏÒ×ÁÒÄÉÔ ÉÚ×ÌÅÞÅÎÎÕÀ ÐÏÞÔÕ ÞÅÒÅÚ SMTP, ÞÔÏÂÙ ×É ÍÏÇÌÉ
ÐÒÏÞÉÔÁÔØ ÅÅ Ó×ÏÉÍ ÌÀÂÉÍÙÍ ÐÏÞÔÏ×ÙÍ ËÌÉÅÎÔÏÍ.

%description -l tr
fetchmail yazýlýmý, POP veya IMAP desteði veren bir sunucuda yer alan
mektuplarýnýzý alýr.

%description -l uk
Fetchmail - ÃÅ ÕÔÉÌ¦ÔÁ ÏÔÒÉÍÁÎÎÑ ÐÏÛÔÉ Ú ×¦ÄÄÁÌÅÎÏ§ ÍÁÛÉÎÉ ÔÁ
ÆÏÒ×ÁÒÄÉÎÇÕ, ÐÒÉÚÎÁÞÅÎÁ ÄÌÑ ×ÉËÏÒÉÓÔÁÎÎÑ ÎÁ on-demand TCP/IP
Ú'¤ÄÎÁÎÎÑÈ, ÔÁËÉÈ ÑË SLIP ÞÉ PPP Ú'¤ÄÎÁÎÎÑ. Fetchmail Ð¦ÄÔÒÉÍÕ¤ ×Ó¦
×ÉËÏÒÉÓÔÏ×Õ×ÁÎ¦ ÎÁ ÓØÏÇÏÄÎ¦ ÐÒÏÔÏËÏÌÉ ×¦ÄÄÁÌÅÎÏ§ ÐÏÛÔÉ (POP2, POP3,
RPOP, APOP, KPOP, ×Ó¦ IMAPÉ, ESMTP ETRN). ð¦ÓÌÑ ÏÔÒÉÍÁÎÎÑ Fetchmail
ÆÏÒ×ÁÒÄÉÔØ ÐÏÛÔÕ ÞÅÒÅÚ SMTP, ÝÏÂ ×É ÍÏÇÌÉ ÐÒÏÞÉÔÁÔÉ §§ Ó×Ï§Í ÕÌÀÂÌÅÎÉÍ
ÐÏÛÔÏ×ÉÍ ËÌ¦¤ÎÔÏÍ.

%package -n fetchmailconf
Summary:	A GUI configurator for generating fetchmail configuration files
Summary(es):	Configurador GUI interactivo por fetchmail
Summary(fr):	GUI configurateur pour fetchmail
Summary(pl):	Konfigurator GUI do fetchmaila
Summary(pt):	Um configurador gráfico para a criação de arquivos de configuração para o fetchmail
Summary(ru):	çÒÁÆÉÞÅÓËÁÑ ÕÔÉÌÉÔÁ ÄÌÑ ËÏÎÆÉÇÕÒÁÃÉÉ ÐÒÅÄÐÏÞÔÅÎÉÊ ÄÌÑ fetchmail
Summary(uk):	çÒÁÆ¦ÞÎÁ ÕÔÉÌ¦ÔÁ ÄÌÑ ËÏÎÆ¦ÇÕÒÁÃ¦§ ×ÐÏÄÏÂÁÎØ ÄÌÑ fetchmail
Group:		Applications/System
Requires:	%{name} = %{version}
Requires:	python
Requires:	tkinter

%description -n fetchmailconf
A GUI configurator for generating fetchmail configuration file written
in python.

%description -n fetchmailconf -l de
Ein interaktiver GUI-Konfigurator für fetchmail in python.

%description -n fetchmailconf -l es
Configurador gráfico para fetchmail escrito en python.

%description -n fetchmailconf -l pl
Konfigurator GUI do fetchmaila napisany w pythonie.

%description -n fetchmailconf -l pt
Um configurador gráfico para a criação de arquivos de configuração
para o fetchmail.

%description -n fetchmailconf -l ru
Fetchmailconf - ÜÔÏ ÐÒÏÇÒÁÍÍÁ ÎÁ TCL/TK ÄÌÑ ËÏÎÆÉÇÕÒÁÃÉÉ ×ÁÛÅÇÏ ÆÁÊÌÁ
ÐÒÅÄÐÏÞÔÅÎÉÊ ~/.fetchmailrc.

%description -n fetchmailconf -l uk
Fetchmailconf - ÃÅ ÐÒÏÇÒÁÍÁ ÎÁ TCL/TK ÄÌÑ ËÏÎÆ¦ÇÕÒÁÃ¦§ ×ÁÛÏÇÏ ÆÁÊÌÁ
×ÐÏÄÏÂÁÎØ ~/.fetchmailrc.

%package daemon
Summary:	SysV init script for demonize fetchmail for sucking emails
Summary(pl):	Skrypt startowy SysV do uruchamiania systemowego fetchmaila jako demona
Group:		Applications/System
Requires:	%{name} = %{version}
PreReq:		rc-scripts >= 0.2.0
Requires(post,preun):	/sbin/chkconfig

%description daemon
SysV init script for demonize fetchmail for sucking emails.

%description daemon -l pl
Skrypt startowy SysV do uruchamiania systemowego fetchmaila jako demona.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
%configure \
	--enable-nls \
	--without-included-gettext \
	--enable-inet6 \
	--enable-RPA \
	--enable-NTLM \
	--enable-SDPS \
	%{!?_without_ssl:--with-ssl=%{_prefix}} \
	%{?_without_ssl:--without-ssl} \
	--without-kerberos
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig} \
	$RPM_BUILD_ROOT/etc/logrotate.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/fetchmail
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/fetchmail
install %{SOURCE4} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/fetchmailconf.1
echo ".so fetchmail.1" > $RPM_BUILD_ROOT%{_mandir}/man1/fetchmailconf.1

> $RPM_BUILD_ROOT%{_sysconfdir}/fetchmailrc

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post daemon
/sbin/chkconfig --add fetchmail
if [ -f /var/lock/subsys/fetchmail ]; then
	/etc/rc.d/init.d/fetchmail restart >&2
else
	echo "Run \"/etc/rc.d/init.d/fetchmail start\" to start fetchmail daemon."
fi

%preun daemon
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/fetchmail ]; then
		/etc/rc.d/init.d/fetchmail stop >&2
	fi
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
%{_applnkdir}/Settings/fetchmailconf.desktop
%{_mandir}/man1/fetchmailconf.1*

%files daemon
%defattr(644,root,root,755)
%attr(600,root,root) %config(noreplace,missingok) %{_sysconfdir}/fetchmailrc
%attr(754,root,root) /etc/rc.d/init.d/fetchmail
%attr(640,root,root) %config(noreplace) /etc/sysconfig/fetchmail
%attr(640,root,root) /etc/logrotate.d/fetchmail
