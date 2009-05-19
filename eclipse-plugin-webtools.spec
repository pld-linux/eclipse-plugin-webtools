%include	/usr/lib/rpm/macros.java
Summary:	Web Tools Platform (WTP) Project
Name:		eclipse-plugin-webtools
Version:	2.0
Release:	0.2
License:	EPL v1.0
Group:		Development/Tools
URL:		http://www.eclipse.org/webtools/
# http://code.google.com/eclipse/docs/install-from-zip.html
Source0:	http://dl.google.com/eclipse/plugin/3.3/zips/gpe-e33-latest.zip
# Source0-md5:	955d207982a0ec954b1c067019c33694
BuildRequires:	rpm-javaprov
Requires:	eclipse >= 3.3
Requires:	eclipse-gef
#  WST Common UI (2.0.2.v200802150100-7C5EH3E9RvTVnirrspVz0bmP7g8d) requires plug-in "org.eclipse.draw2d (3.2.0)", or compatible.
#  WST Common Core (2.0.2.v200802150100-7C78EKOE_EkMNlO6f7cjpz0) requires plug-in "org.eclipse.emf.ecore (2.2.0)", or compatible.
#  Eclipse XML Editors and Tools (2.0.2.v200802150100-7A1ECMCnbcl1bVs9uNm_Zkieb7Qe) requires plug-in "org.eclipse.emf.common (2.2.0)", or compatible.
#  WST XML Core (2.0.2.v200802150100-787BE_4CYQCD-DaQMIfPd) requires plug-in "org.eclipse.emf.ecore (2.2.0)", or compatible.
#  WST Web Services UI (2.0.2.v200802150100-791ECIAufYO9BlarnPCFGewtZiN1) requires plug-in "org.eclipse.emf.common (2.2.0)", or compatible.
#  WST Web Services Core (2.0.2.v200802150100-7E7KEB2EC3wSU5UghChM0v) requires plug-in "org.eclipse.xsd (2.3.0)", or compatible.
#  WST Web UI (2.0.2.v200802150100-7A0EAlCiWfJKsCZoChvz0dMYOb) requires plug-in "org.eclipse.emf.ecore (2.2.0)", or compatible.
#  WST Web Core (2.0.2.v200802150100-42CN_kE77a8F9XCOEL) requires plug-in "org.eclipse.emf.ecore (2.2.0)", or compatible.
BuildArch:	noarch
# FIXME:  we need to investigate the differences between their version and the one in PLD
#BuildRequires:       wsdl4j
BuildRequires:       xerces-j2
BuildRequires:       uddi4j
# FIXME:  update this to 1.7.2
BuildRequires:       java-cactus
BuildRequires:       aspectj
# FIXME:  do I need to BR/R this?
BuildRequires:       xml-commons-apis
BuildRequires:       xml-commons-resolver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		eclipsedir	%{_datadir}/eclipse

%description
The Eclipse Web Tools Platform (WTP) project extends the Eclipse
platform with tools for developing Web and Java EE applications. It
includes source and graphical editors for a variety of languages,
wizards and built-in applications to simplify development, and tools
and APIs to support deploying, running, and testing apps.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{eclipsedir}/{features,plugins}
cp -a features/* $RPM_BUILD_ROOT%{eclipsedir}/features
cp -a plugins/* $RPM_BUILD_ROOT%{eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{eclipsedir}/features/com.google.gdt.eclipse.suite.e33.feature_*
%{eclipsedir}/plugins/com.google.appengine.eclipse.core_*.jar
%{eclipsedir}/plugins/com.google.gdt.eclipse.core_*.jar
%{eclipsedir}/plugins/com.google.gdt.eclipse.suite_*.jar
%{eclipsedir}/plugins/com.google.gwt.eclipse.core_*.jar
