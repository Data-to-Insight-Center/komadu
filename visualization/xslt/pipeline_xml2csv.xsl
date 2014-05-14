<?xml version="1.0" encoding="UTF-8"?>
<!-- pipeline_xml2csv.xsl, version 0.9, 2010-09-15 -->
<!-- pipeline_xml2csv.xsl is the master stylesheet including 7 step stylesheets in a pipeline. -->
<!--Published with tutorial at www.xmlplease.com/pipeline_xml2csv -->
<!-- Made by Jesper Tverskov, Adelaide, Australia. -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
    xmlns:prov="http://www.w3.org/ns/prov#"
    version="2.0">
    <!--
STEP-1: s1_user-defined.xsl
Add user-defined templates of exceptions to delete, rename or add attributes and elements.

STEP-2: s2_flatten.xsl
Automatically flattens XML, attributes and elements, to three levels. "_" and "." are used as delimiters in flattened element names.

STEP-3: s3_equalizing.xsl
Automatically adds missing optional elements: <element/>, if they are missing from a sub-set of item elements.

STEP-4: s4_user-defined.xsl
Add user-defined templates of exceptions to fine-tune the work of step-3 if necessary (typically to get better element names).

STEP-5: s5_xml2csv.xsl
The final transformation of input or modified input xml file to CSV.
-->

    <!-- 
    Param values:
    0 = skip.
    1 = use included step stylesheet.
    2 = and serialize step to file. -->

    <xsl:param name="param_s1_extract" select="1"/>
    <xsl:param name="param_s2_flatten" select="1"/>
    <xsl:param name="param_s3_equalizing" select="1"/>
    <xsl:param name="param_s4_user-defined" select="1"/>
    <xsl:param name="param_s5_xml2csv" select="2"/>

    <xsl:include href="s1_extract_edges.xsl"/>
    <xsl:include href="s1_extract_nodes.xsl"/>
    <xsl:include href="s2_flatten.xsl"/>
    <xsl:include href="s3_equalizing.xsl"/>
    <xsl:include href="s4_user-defined.xsl"/>
    <xsl:include href="s5_xml2csv.xsl"/>

    <xsl:template match="/">

        <!-- STEP-1: extract edges and nodes -->
        <xsl:variable name="s1_extract_edges">
            <xsl:choose>
                <xsl:when test="$param_s1_extract = 1 or $param_s1_extract = 2">
                    <xsl:apply-templates mode="s1_extract_edges"/>
                </xsl:when>
                <xsl:when test="$param_s1_extract = 0">
                    <xsl:copy-of select="."/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:message terminate="yes">param_s1_user-defined must have value
                        0|1|2</xsl:message>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:variable>
        <xsl:variable name="s1_extract_nodes">
            <xsl:choose>
                <xsl:when test="$param_s1_extract = 1 or $param_s1_extract = 2">
                    <xsl:apply-templates mode="s1_extract_nodes"/>
                </xsl:when>
                <xsl:when test="$param_s1_extract = 0">
                    <xsl:copy-of select="."/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:message terminate="yes">param_s1_user-defined must have value
                        0|1|2</xsl:message>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:variable>
        
        <!--save intermediate files-->
        <xsl:if test="$param_s1_extract = 2">
            <xsl:result-document href="temp_s1_extract_edges.xml" method="xml" indent="yes">
                <xsl:copy-of select="$s1_extract_edges"/>
            </xsl:result-document>
        </xsl:if>
        <xsl:if test="$param_s1_extract = 2">
            <xsl:result-document href="temp_s1_extract_nodes.xml" method="xml" indent="yes">
                <xsl:copy-of select="$s1_extract_nodes"/>
            </xsl:result-document>
        </xsl:if>

        <!-- STEP-2: s2_flatten.xsl -->
        <xsl:variable name="s2_flatten_edges">
            <xsl:choose>
                <xsl:when test="$param_s2_flatten = 1 or $param_s2_flatten = 2">
                    <xsl:apply-templates mode="s2_flatten" select="$s1_extract_edges"/>
                </xsl:when>
                <xsl:when test="$param_s2_flatten = 0">
                    <xsl:copy-of select="$s1_extract_edges"/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:message terminate="yes">param_s2_flatten must have value
                        0|1|2</xsl:message>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:variable>
        <xsl:variable name="s2_flatten_nodes">
            <xsl:choose>
                <xsl:when test="$param_s2_flatten = 1 or $param_s2_flatten = 2">
                    <xsl:apply-templates mode="s2_flatten" select="$s1_extract_nodes"/>
                </xsl:when>
                <xsl:when test="$param_s2_flatten = 0">
                    <xsl:copy-of select="$s1_extract_nodes"/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:message terminate="yes">param_s2_flatten must have value
                        0|1|2</xsl:message>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:variable>
        
        <!--save intermediate files-->
        <xsl:if test="$param_s2_flatten = 2">
            <xsl:result-document href="temp_s2_flatten_edges.xml" method="xml" indent="yes">
                <xsl:copy-of select="$s2_flatten_edges"/>
            </xsl:result-document>
        </xsl:if>
        <xsl:if test="$param_s2_flatten = 2">
            <xsl:result-document href="temp_s2_flatten_nodes.xml" method="xml" indent="yes">
                <xsl:copy-of select="$s2_flatten_nodes"/>
            </xsl:result-document>
        </xsl:if>

        <!-- STEP-3: s3_equalizing.xsl -->
        <xsl:variable name="s3_equalizing_edges">
            <xsl:choose>
                <xsl:when test="$param_s3_equalizing = 1 or $param_s3_equalizing = 2">
                    <xsl:apply-templates mode="s3_equalizing" select="$s2_flatten_edges"/>
                </xsl:when>
                <xsl:when test="$param_s3_equalizing = 0">
                    <xsl:copy-of select="$s2_flatten_edges"/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:message terminate="yes">param_s3_equalizing must have value
                        0|1|2</xsl:message>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:variable>
        <xsl:variable name="s3_equalizing_nodes">
            <xsl:choose>
                <xsl:when test="$param_s3_equalizing = 1 or $param_s3_equalizing = 2">
                    <xsl:apply-templates mode="s3_equalizing" select="$s2_flatten_nodes"/>
                </xsl:when>
                <xsl:when test="$param_s3_equalizing = 0">
                    <xsl:copy-of select="$s2_flatten_nodes"/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:message terminate="yes">param_s3_equalizing must have value
                        0|1|2</xsl:message>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:variable>
        
        <!--save intermediate files-->
        <xsl:if test="$param_s3_equalizing = 2">
            <xsl:result-document href="temp_s3_equalizing_edges.xml" method="xml" indent="yes">
                <xsl:copy-of select="$s3_equalizing_edges"/>
            </xsl:result-document>
        </xsl:if>
        <xsl:if test="$param_s3_equalizing = 2">
            <xsl:result-document href="temp_s3_equalizing_nodes.xml" method="xml" indent="yes">
                <xsl:copy-of select="$s3_equalizing_nodes"/>
            </xsl:result-document>
        </xsl:if>

        <!-- STEP-4: s4_user-defined.xsl -->
        <xsl:variable name="s4_user-defined_edges">
            <xsl:choose>
                <xsl:when test="$param_s4_user-defined = 1 or $param_s4_user-defined = 2">
                    <xsl:apply-templates mode="s4_user-defined" select="$s3_equalizing_edges"/>
                </xsl:when>
                <xsl:when test="s4_user-defined = 0">
                    <xsl:copy-of select="$s3_equalizing_edges"/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:message terminate="yes">param_s4_user-defined must have value
                        0|1|2</xsl:message>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:variable>
        <xsl:variable name="s4_user-defined_nodes">
            <xsl:choose>
                <xsl:when test="$param_s4_user-defined = 1 or $param_s4_user-defined = 2">
                    <xsl:apply-templates mode="s4_user-defined" select="$s3_equalizing_nodes"/>
                </xsl:when>
                <xsl:when test="s4_user-defined = 0">
                    <xsl:copy-of select="$s3_equalizing_nodes"/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:message terminate="yes">param_s4_user-defined must have value
                        0|1|2</xsl:message>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:variable>
        
        <!--save intermediate files-->
        <xsl:if test="$param_s4_user-defined = 2">
            <xsl:result-document href="temp_s4_user-defined-edges.xml" method="xml" indent="yes">
                <xsl:copy-of select="$s4_user-defined_edges"/>
            </xsl:result-document>
        </xsl:if>
        <xsl:if test="$param_s4_user-defined = 2">
            <xsl:result-document href="temp_s4_user-defined-nodes.xml" method="xml" indent="yes">
                <xsl:copy-of select="$s4_user-defined_nodes"/>
            </xsl:result-document>
        </xsl:if>

        <!-- STEP-5: s5_xml2csv -->
        <xsl:variable name="s5_xml2csv_edges">
            <xsl:choose>
                <xsl:when test="$param_s5_xml2csv = 1 or $param_s5_xml2csv = 2">
                    <xsl:apply-templates mode="s5_xml2csv" select="$s4_user-defined_edges"/>
                </xsl:when>
                <xsl:when test="$param_s5_xml2csv = 1">
                    <xsl:copy-of select="$s4_user-defined_edges"/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:message terminate="yes">param_s5_xml2csv must have value
                        0|1|2</xsl:message>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:variable>
        <xsl:variable name="s5_xml2csv_nodes">
            <xsl:choose>
                <xsl:when test="$param_s5_xml2csv = 1 or $param_s5_xml2csv = 2">
                    <xsl:apply-templates mode="s5_xml2csv" select="$s4_user-defined_nodes"/>
                </xsl:when>
                <xsl:when test="$param_s5_xml2csv = 1">
                    <xsl:copy-of select="$s4_user-defined_nodes"/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:message terminate="yes">param_s5_xml2csv must have value
                        0|1|2</xsl:message>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:variable>
        
        <!--save final output files-->
        <xsl:if test="$param_s5_xml2csv = 2">
            <xsl:result-document href="edges.csv" method="text">
                <xsl:copy-of select="$s5_xml2csv_edges"/>
            </xsl:result-document>
        </xsl:if>
        <xsl:if test="$param_s5_xml2csv = 2">
            <xsl:result-document href="nodes.csv" method="text">
                <xsl:copy-of select="$s5_xml2csv_nodes"/>
            </xsl:result-document>
        </xsl:if>
        
        <!-- the XSLT output can be null-->
        <!--<xsl:copy-of select="$s5_xml2csv_edges"/>-->
    </xsl:template>
</xsl:stylesheet>