<?xml version="1.0" encoding="UTF-8"?>
<!-- s2_flatten.xsl, version 0.9, 2010-09-18 -->
<!-- s2_flatten.xsl is third step of pipeline_xml2csv.xsl, published at www.xmlplease.com/pipeline_xml2csv -->
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output indent="yes"/>
    <xsl:strip-space elements="*"/>

    <xsl:template match="/" mode="s2_flatten">
        <xsl:apply-templates mode="s2_flatten"/>
    </xsl:template>

    <xsl:template match="/*" mode="s2_flatten">
        <xsl:copy>
            <!-- Attributes at top-level is ignored. -->
            <xsl:apply-templates select="node()" mode="s2_flatten"/>
        </xsl:copy>
    </xsl:template>

    <!-- Elements at item level.  -->
    <xsl:template match="/*/*" mode="s2_flatten">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()" mode="s2_flatten"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="*" mode="s2_flatten">
        <xsl:choose>
            <xsl:when test="*">
                <xsl:apply-templates select="@*|node()" mode="s2_flatten"/>
            </xsl:when>
            <xsl:otherwise>
                <xsl:variable name="name"
                    select="if(count(ancestor::*) > 2) then for $a in ancestor::*[count(ancestor::*) > 1] return for $b in $a return local-name($b) else ''"/>
                <xsl:element
                    name="{concat(string-join($name, '_'), if(count(ancestor::*) > 2)then '_' else '',  local-name(.))}">
                    <xsl:value-of select="."/>
                </xsl:element>
                <xsl:apply-templates select="@*" mode="s2_flatten"/>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
     
    <!-- All attributes except first and second level.  --> 
    <xsl:template match="@*" mode="s2_flatten">
                <xsl:variable name="name"
                    select="if(count(ancestor::*) > 2) then for $a in ancestor::*[count(ancestor::*) > 1] return for $b in $a return local-name($b) else ''"/>
                <xsl:element
                    name="{concat(string-join($name, '_'), if(count(ancestor::*) > 2)then '.' else '',  local-name(.))}">
                    <xsl:value-of select="."/>
                </xsl:element>
    </xsl:template>
    
    <!-- Attributes of item (/*/*) need an extra ancestor level to get element name right. -->
    <xsl:template match="/*/*/@*" mode="s2_flatten">
        <xsl:variable name="name"
            select="if(count(ancestor::*) > 1) then for $a in ancestor::*[count(ancestor::*) > 0] return for $b in $a return local-name($b) else ''"/>
        <!--<xsl:element
            name="{concat(string-join($name, '_'), if(count(ancestor::*) > 1)then '.' else '',  local-name(.))}">
            <xsl:value-of select="."/>
        </xsl:element>-->
        <xsl:element
            name="{local-name(.)}">
            <xsl:value-of select="."/>
        </xsl:element>
    </xsl:template>
    
    <!-- Comments and processing-instructions are first ignored at STEP-7, s7_xml2csv.xsl. -->
    <!-- We keep them alive until then: They might contain information that can remind us of something. -->
    <xsl:template match="comment()|processing-instruction()" mode="s2_flatten">
        <xsl:copy/>          
    </xsl:template>

</xsl:stylesheet>
