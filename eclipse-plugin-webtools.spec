%include	/usr/lib/rpm/macros.java
Summary:	Web Tools Platform (WTP) Project
Name:		eclipse-plugin-webtools
Version:	2.0.3
Release:	1
License:	EPL v1.0
Group:		Development/Tools
URL:		http://www.eclipse.org/webtools/
Source0:	http://archive.eclipse.org/webtools/downloads/drops/R2.0/R-%{version}-20080710044639/wtp-R-%{version}-20080710044639.zip
# Source0-md5:	50b71ffba34da650dfa259388c043ab3
BuildRequires:	rpm-javaprov
BuildRequires:	unzip
#Requires:	dtp-sdk >= 1.5.2
Requires:	eclipse >= 3.3
Requires:	eclipse-gef >= 3.3.2
#Requires:	emf-sdo-xsd-sdk >= 2.3
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
%{eclipsedir}/features/org.eclipse.jpt.feature_*
%{eclipsedir}/features/org.eclipse.jst_*
%{eclipsedir}/features/org.eclipse.jst.common_*
%{eclipsedir}/features/org.eclipse.jst.enterprise_*
%{eclipsedir}/features/org.eclipse.jst.server_*
%{eclipsedir}/features/org.eclipse.jst.web_*
%{eclipsedir}/features/org.eclipse.jst.webpageeditor.feature_*
%{eclipsedir}/features/org.eclipse.wst_*
%{eclipsedir}/features/org.eclipse.wst.common_*
%{eclipsedir}/features/org.eclipse.wst.server_*
%{eclipsedir}/features/org.eclipse.wst.web_*
%{eclipsedir}/features/org.eclipse.wst.ws_*
%{eclipsedir}/features/org.eclipse.wst.xml_*
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
%{eclipsedir}/plugins/org.eclipse.jem.beaninfo_*.jar
%{eclipsedir}/plugins/org.eclipse.jem_*.jar
%{eclipsedir}/plugins/org.eclipse.jem.proxy_*.jar
%{eclipsedir}/plugins/org.eclipse.jem.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jem.util_*.jar
%{eclipsedir}/plugins/org.eclipse.jem.workbench_*.jar
%{eclipsedir}/plugins/org.eclipse.jpt.core_*.jar
%{eclipsedir}/plugins/org.eclipse.jpt.db_*.jar
%{eclipsedir}/plugins/org.eclipse.jpt.db.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jpt.doc.user_*.jar
%{eclipsedir}/plugins/org.eclipse.jpt.gen_*.jar
%{eclipsedir}/plugins/org.eclipse.jpt_*.jar
%{eclipsedir}/plugins/org.eclipse.jpt.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jpt.utility_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.common.annotations.controller_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.common.annotations.core_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.common.annotations.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.common.frameworks_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.common.project.facet.core_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ejb.doc.user_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ejb.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.j2ee.core_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.j2ee.doc.user_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.j2ee.ejb.annotation.model_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.j2ee.ejb.annotations.emitter_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.j2ee.ejb.annotations.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.j2ee.ejb.annotations.xdoclet_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.j2ee.ejb_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.j2ee.infopop_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.j2ee_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.j2ee.jca_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.j2ee.jca.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.j2ee.navigator.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.j2ee.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.j2ee.web_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.j2ee.webservice_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.j2ee.webservice.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.j2ee.xdoclet.runtime_*.jar
%{eclipsedir}/plugins/org.eclipse.jst_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.jee.ejb_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.jee_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.jee.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.jee.web_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.jsf.common_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.jsf.common.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.jsf.core_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.jsf.doc.user_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.jsf.facesconfig_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.jsf.facesconfig.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.jsf.standard.tagsupport_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.jsf.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.jsp.core_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.jsp.ui.infopop_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.jsp.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.pagedesigner_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.pagedesigner.jsf.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.pagedesigner.jsp.core_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.server.core_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.server.generic.core_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.server.generic.jboss_*
%{eclipsedir}/plugins/org.eclipse.jst.server.generic.jonas_*
%{eclipsedir}/plugins/org.eclipse.jst.server.generic.oc4j_*
%{eclipsedir}/plugins/org.eclipse.jst.server.generic.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.server.installable_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.server.preview.adapter_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.server.tomcat.core_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.server.tomcat.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.server.ui.doc.user_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.server.ui.infopop_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.server.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.server.websphere.core_*
%{eclipsedir}/plugins/org.eclipse.jst.servlet.ui.infopop_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.servlet.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.standard.schemas_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.axis2.consumption.core_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.axis2.consumption.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.axis2.core_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.axis2.creation.core_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.axis2.creation.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.axis2.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.axis.consumption.core_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.axis.consumption.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.axis.creation.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.axis.infopop_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.axis.ui.doc.user_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.consumption_*
%{eclipsedir}/plugins/org.eclipse.jst.ws.consumption.infopop_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.consumption.ui.doc.user_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.consumption.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.creation.ejb.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.creation.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.doc.user_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.infopop_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.uddiregistry_*.jar
%{eclipsedir}/plugins/org.eclipse.jst.ws.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.command.env_*
%{eclipsedir}/plugins/org.eclipse.wst.command.env.core_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.command.env.doc.user_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.command.env.infopop_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.command.env.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.common.core_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.common.emf_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.common.emfworkbench.integration_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.common.environment_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.common.frameworks_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.common.frameworks.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.common.infopop_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.common.modulecore_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.common.project.facet.core_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.common.project.facet.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.common.snippets_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.common.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.common.ui.properties_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.common.uriresolver_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.css.core_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.css.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.doc.user_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.dtd.core_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.dtdeditor.doc.user_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.dtd.ui.infopop_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.dtd.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.html.core_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.html.ui.infopop_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.html.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.internet.cache_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.internet.monitor.core_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.internet.monitor.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.wst_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.javascript.core_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.javascript.ui.infopop_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.javascript.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.server.core_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.server.http.core_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.server.http.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.server.preview.adapter_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.server.preview_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.server.ui.doc.user_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.server.ui.infopop_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.server.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.sse.core_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.sse.doc.user_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.sse.ui.infopop_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.sse.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.standard.schemas_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.validation.infopop_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.validation_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.validation.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.web_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.webtools.doc.user_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.web.ui.infopop_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.web.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.wsdl_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.wsdl.ui.doc.user_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.wsdl.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.wsdl.validation_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.ws.explorer_*
%{eclipsedir}/plugins/org.eclipse.wst.wsi_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.ws.infopop_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.wsi.ui.doc.user_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.wsi.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.ws_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.ws.parser_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.ws.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.xml.core_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.xmleditor.doc.user_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.xml.ui.infopop_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.xml.ui_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.xsd.core_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.xsdeditor.doc.user_*.jar
%{eclipsedir}/plugins/org.eclipse.wst.xsd.ui_*.jar
%{eclipsedir}/plugins/org.uddi4j_*.jar
