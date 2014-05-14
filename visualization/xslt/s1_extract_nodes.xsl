<?xml version="1.0" encoding="UTF-8"?>
<!-- s1_extract_nodes.xsl, version 0.9, 2010-09-15 -->
<!-- s1_user-defdined.xsl is first step of pipeline_xml2csv.xsl, published at www.xmlplease.com/pipeline_xml2csv -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:prov="http://www.w3.org/ns/prov#"
    xmlns:kom="http://komadu.d2i.indiana.edu" xmlns:ext="http://komadu.d2i.indiana.edu/external"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs" version="2.0">
    <xsl:strip-space elements="*"/>
    <xsl:output indent="yes"/>

    <xsl:template match="prov:document" mode="s1_extract_nodes">
        <xsl:copy>
            <xsl:apply-templates select="prov:activity" mode="s1_extract_nodes"/>
            <xsl:apply-templates select="prov:entity" mode="s1_extract_nodes"/>
            <xsl:apply-templates select="prov:bundle" mode="s1_extract_nodes"/>
            <xsl:apply-templates select="prov:collection" mode="s1_extract_nodes"/>
            <xsl:apply-templates select="prov:plan" mode="s1_extract_nodes"/>
            <xsl:apply-templates select="prov:agent" mode="s1_extract_nodes"/>
            <xsl:apply-templates select="prov:person" mode="s1_extract_nodes"/>
            <xsl:apply-templates select="prov:organization" mode="s1_extract_nodes"/>
            <xsl:apply-templates select="prov:softwareAgent" mode="s1_extract_nodes"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:activity" mode="s1_extract_nodes">
        <xsl:copy>
            <xsl:copy-of select="@*|node()"/>
            <prov:nodeType>activity</prov:nodeType>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:entity" mode="s1_extract_nodes">
        <xsl:copy>
            <xsl:copy-of select="@*|node()"/>
            <prov:nodeType>entity</prov:nodeType>
        </xsl:copy>
    </xsl:template>

    <!-- subclasses of entity -->
    <xsl:template match="/prov:document/prov:bundle" mode="s1_extract_nodes">
        <xsl:copy>
            <xsl:copy-of select="@*|node()"/>
            <prov:nodeType>entity</prov:nodeType>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="/prov:document/prov:collection" mode="s1_extract_nodes">
        <xsl:copy>
            <xsl:copy-of select="@*|node()"/>
            <prov:nodeType>entity</prov:nodeType>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="/prov:document/prov:plan" mode="s1_extract_nodes">
        <xsl:copy>
            <xsl:copy-of select="@*|node()"/>
            <prov:nodeType>entity</prov:nodeType>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="/prov:document/prov:agent" mode="s1_extract_nodes">
        <xsl:copy>
	    <xsl:copy-of select="@*"/>
	    <xsl:apply-templates select="node()" mode="s1_extract_nodes"/>
            <prov:nodeType>agent</prov:nodeType>
        </xsl:copy>
    </xsl:template>

    <!-- subclasses of agent -->
    <xsl:template match="/prov:document/prov:person" mode="s1_extract_nodes">
        <xsl:copy>
	    <xsl:copy-of select="@*"/>
	    <xsl:apply-templates select="node()" mode="s1_extract_nodes"/>
            <prov:nodeType>agent</prov:nodeType>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="/prov:document/prov:organization" mode="s1_extract_nodes">
        <xsl:copy>
	    <xsl:copy-of select="@*"/>
	    <xsl:apply-templates select="node()" mode="s1_extract_nodes"/>
            <prov:nodeType>agent</prov:nodeType>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="/prov:document/prov:softwareAgent" mode="s1_extract_nodes">
        <xsl:copy>
	    <xsl:copy-of select="@*"/>
	    <xsl:apply-templates select="node()" mode="s1_extract_nodes"/>
            <prov:nodeType>agent</prov:nodeType>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="/prov:document/prov:agent/kom:name" mode="s1_extract_nodes" priority="5">
        <kom:nodeName>
	    <xsl:value-of select="text()"/>
        </kom:nodeName>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:agent/*" mode="s1_extract_nodes">
        <xsl:copy-of select="."/>
    </xsl:template>

    <!-- ONLY EXAMPLES FOR INSPIRATION -->
    <!-- Deleting the third child of item. -->
    <xsl:template match="/*/*/*[3]" mode="s1_extract_nodes" use-when="false()"/>

    <!-- Renaming the first child of item to test -->
    <xsl:template match="/*/*/*[1]" mode="s1_extract_nodes" use-when="false()">
        <test>
            <xsl:apply-templates select="@*|node()" mode="s1_extract_nodes"/>
        </test>
    </xsl:template>

</xsl:stylesheet>
