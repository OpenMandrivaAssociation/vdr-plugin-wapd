
%define plugin	wapd
%define name	vdr-plugin-%plugin
%define version	0.9
%define rel	6

Summary:	VDR plugin: Remote control by WAP
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.heiligenmann.de/vdr/vdr/plugins/wapd.html
Source:		http://www.heiligenmann.de/vdr/download/vdr-%plugin-%version.tgz
Patch0:		02_gettext-i18n.dpatch
Patch1:		03_gcc-4.1.x.dpatch
Patch2:		wapd-linking-order.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin lets VDR listen to WAP requests to allow remote control
by WML enabled browsers - eg. mobile devices - and is called "WAP
daemon" or "wapd".

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# use PORT for WAP (default: 8888)
var=PORT
param="-p PORT"
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
%vdr_plugin_install
install -D -m755 wappasswd %{buildroot}%{_bindir}/wappasswd

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%{_bindir}/wappasswd


%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.9-5mdv2010.0
+ Revision: 401088
- rebuild for new VDR
- fix build failure due to wrong linking order (linking-order.patch)

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.9-4mdv2009.1
+ Revision: 359383
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.9-3mdv2009.0
+ Revision: 197997
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.9-2mdv2009.0
+ Revision: 197741
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (P0 from e-tobi)
- fix compiler warnings (P1 from e-tobi)

* Fri Feb 29 2008 Anssi Hannula <anssi@mandriva.org> 0.9-1mdv2008.1
+ Revision: 176882
- new version
- drop patch, fixed upstream

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.8-3mdv2008.1
+ Revision: 145262
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.8-2mdv2008.1
+ Revision: 103243
- rebuild for new vdr

* Fri Jul 20 2007 Anssi Hannula <anssi@mandriva.org> 0.8-1mdv2008.0
+ Revision: 53741
- initial Mandriva release

