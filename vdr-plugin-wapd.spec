
%define plugin	wapd
%define name	vdr-plugin-%plugin
%define version	0.9
%define rel	3

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
BuildRoot:	%{_tmppath}/%{name}-buildroot
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
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# use PORT for WAP (default: 8888)
var=PORT
param="-p PORT"
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install
install -D -m755 wappasswd %{buildroot}%{_bindir}/wappasswd

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%{_bindir}/wappasswd
