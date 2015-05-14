%define version 0.2.2

Name:	redhat-access-plugin-sat5
Version:	%{version}
Release:	1%{?dist}
Summary:	Red Hat Access Plugin for Satellite 5.7
Group:	Applications/System	
License:	MIT
Source0: redhat-access-plugin-sat5.tar.gz 
BuildArch: noarch
#BuildRequires:	
#Requires:	

%description
Red Hat Access Plugin for Satellite 5.7


%prep
%setup -q


%build
echo OK


%install
rm -rf $RPM_BUILD_ROOT
#httpd.conf
mkdir -p $RPM_BUILD_ROOT/etc/httpd/conf.d
cp rh-insights-sat5.conf $RPM_BUILD_ROOT/etc/httpd/conf.d
#js
mkdir -p $RPM_BUILD_ROOT/var/www/html/javascript
cp insights.js $RPM_BUILD_ROOT/var/www/html/javascript
#css
mkdir -p $RPM_BUILD_ROOT/var/www/html/css
cp insights.css $RPM_BUILD_ROOT/var/www/html/css
#war
mkdir -p $RPM_BUILD_ROOT/usr/share/tomcat6/webapps
cp redhat_access.war $RPM_BUILD_ROOT/usr/share/tomcat6/webapps
#jsp files
mkdir -p $RPM_BUILD_ROOT/usr/share/tomcat6/webapps/rhn/WEB-INF/pages/admin
mkdir -p $RPM_BUILD_ROOT/usr/share/tomcat6/webapps/rhn/WEB-INF/pages/systems/sdc
cp jsp/admin/insights.jsp $RPM_BUILD_ROOT/usr/share/tomcat6/webapps/rhn/WEB-INF/pages/admin
cp jsp/systems/insights.jsp $RPM_BUILD_ROOT/usr/share/tomcat6/webapps/rhn/WEB-INF/pages/systems
cp jsp/systems/sdc/insights.jsp $RPM_BUILD_ROOT/usr/share/tomcat6/webapps/rhn/WEB-INF/pages/systems/sdc
#log
mkdir -p $RPM_BUILD_ROOT/var/log
touch $RPM_BUILD_ROOT/var/log/rhai.log


%files
%config %attr(0644,root,root) /etc/httpd/conf.d/rh-insights-sat5.conf
%config %attr(0644,root,root) /var/www/html/javascript/insights.js
%config %attr(0644,root,root) /var/www/html/css/insights.css
%config %attr(0644,root,root) /usr/share/tomcat6/webapps/redhat_access.war
%config %attr(0644,root,root) /usr/share/tomcat6/webapps/rhn/WEB-INF/pages/systems/insights.jsp
%config %attr(0644,root,root) /usr/share/tomcat6/webapps/rhn/WEB-INF/pages/systems/sdc/insights.jsp
%config %attr(0644,root,root) /usr/share/tomcat6/webapps/rhn/WEB-INF/pages/admin/insights.jsp
%config %attr(0660,tomcat,root) /var/log/rhai.log


%changelog
* Thu May 14 2015 Chris Kyrouac <ckyrouac@redhat.com>
- Testing tomcat cache

* Thu May 14 2015 Chris Kyrouac <ckyrouac@redhat.com>
- Remove config stuff

* Wed May 13 2015 Chris Kyrouac <ckyrouac@redhat.com>
- Tech preview mostly ready

* Thu Feb 12 2015 Chris Kyrouac <ckyrouac@redhat.com>
- Version 1

