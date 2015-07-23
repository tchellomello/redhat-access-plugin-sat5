<%@ taglib uri="http://www.opensymphony.com/sitemesh/decorator" prefix="decorator" %>
<%@ taglib uri="http://struts.apache.org/tags-html" prefix="html" %>
<%@ taglib uri="http://rhn.redhat.com/rhn" prefix="rhn" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn" %>

<html:html >
  <body>
    <rhn:require acl="system_has_management_entitlement()">
        <c:choose>
            <c:when test="${!inSSM}">
                <c:set var="actionLink" value="/rhn/systems/details/AddToSSM.do?sid=${system.id}"/>
                <c:set var="actionMessage" value="toolbar.ssm.add"/>
                <c:set var="actionIcon" value="item-ssm-add"/>
            </c:when>
            <c:otherwise>
                <c:set var="actionLink" value="/rhn/systems/details/RemoveFromSSM.do?sid=${system.id}"/>
                <c:set var="actionMessage" value="toolbar.ssm.remove"/>
                <c:set var="actionIcon" value="item-ssm-del"/>
            </c:otherwise>
        </c:choose>
    </rhn:require>

    <c:choose>
        <c:when test="${system.virtualGuest}">
            <c:set var="systemIcon" value="header-system-virt-guest"/>
        </c:when>
        <c:when test="${system.virtualHost}">
            <c:set var="systemIcon" value="header-system-virt-host"/>
        </c:when>
        <c:otherwise>
            <c:set var="systemIcon" value="header-system-physical"/>
        </c:otherwise>
    </c:choose>

    <rhn:toolbar base="h1"
                 icon="${systemIcon}" miscUrl="${actionLink}" miscIcon="${actionIcon}" miscText="${actionMessage}" miscAlt="${actionMessage}"
                 miscAcl="system_has_management_entitlement()"
                 helpUrl=""
                 deletionUrl="/rhn/systems/details/DeleteConfirm.do?sid=${system.id}"
                 deletionType="system">
    </rhn:toolbar>


    <rhn:dialogmenu mindepth="0" maxdepth="3" definition="/WEB-INF/nav/system_detail.xml" renderer="com.redhat.rhn.frontend.nav.DialognavRenderer" />
  </body>
</html:html>

