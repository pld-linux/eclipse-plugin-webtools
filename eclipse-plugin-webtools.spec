%include	/usr/lib/rpm/macros.java
Summary:	Web Tools Platform (WTP) Project
Name:		eclipse-plugin-webtools
Version:	2.0.3
Release:	2
License:	EPL v1.0
Group:		Development/Tools
URL:		http://www.eclipse.org/webtools/
Source0:	http://archive.eclipse.org/webtools/downloads/drops/R2.0/R-%{version}-20080710044639/wtp-R-%{version}-20080710044639.zip
# Source0-md5:	50b71ffba34da650dfa259388c043ab3
BuildRequires:	rpm-javaprov
BuildRequires:	unzip
Requires:	eclipse >= 3.3
Requires:	eclipse-dtp >= 1.5.2
Requires:	eclipse-emf-sdo-xsd >= 2.3
Requires:	eclipse-gef >= 3.3.2
#Suggests:	eclipse-test-framework >= 3.3
#Suggests:	org.eclipse.releng.tools >= 3.3
BuildArch:	noarch
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
mv eclipse/*.html .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{eclipsedir}/{features,plugins}
cp -a eclipse/* $RPM_BUILD_ROOT%{eclipsedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{eclipsedir}/features/org.eclipse.jpt.*
%{eclipsedir}/plugins/org.eclipse.jpt[._]*.jar

%{eclipsedir}/features/org.eclipse.jst[._]*
%{eclipsedir}/plugins/org.eclipse.jst.*
%{eclipsedir}/plugins/org.eclipse.jst_*.jar

%{eclipsedir}/features/org.eclipse.wst[._]*

%{eclipsedir}/plugins/org.eclipse.wst.*
%{eclipsedir}/plugins/org.eclipse.wst_*.jar

%{eclipsedir}/plugins/org.eclipse.jem[._]*.jar
%{eclipsedir}/plugins/org.uddi4j_*.jar

# deps
%{eclipsedir}/plugins/javax.servlet_*.jar
%{eclipsedir}/plugins/javax.servlet.jsp_*.jar
%{eclipsedir}/plugins/javax.wsdl15_*.jar
%{eclipsedir}/plugins/javax.wsdl_*.jar
%{eclipsedir}/plugins/javax.xml.rpc_*
%{eclipsedir}/plugins/javax.xml.soap_*
%{eclipsedir}/plugins/org.apache.axis_*
%{eclipsedir}/plugins/org.apache.cactus_*
%{eclipsedir}/plugins/org.apache.commons.discovery_*
%{eclipsedir}/plugins/org.apache.commons.el_*.jar
%{eclipsedir}/plugins/org.apache.commons.logging_*.jar
%{eclipsedir}/plugins/org.apache.log4j_*.jar
%{eclipsedir}/plugins/org.apache.wsil4j_*.jar
%{eclipsedir}/plugins/org.apache.xerces_*.jar
%{eclipsedir}/plugins/org.apache.xml.resolver_*.jar
