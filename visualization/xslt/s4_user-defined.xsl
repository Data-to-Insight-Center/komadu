<?xml version="1.0" encoding="UTF-8"?>
<!-- s4_user-defined.xsl, version 0.9, 2010-09-15 -->
<!-- s4_user-defined.xsl is 5th step of pipeline_xml2csv.xsl, published at www.xmlplease.com/pipeline_xml2csv -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0">
    <xsl:strip-space elements="*"/>
    <xsl:output indent="yes"/>

    <!-- Identity template -->
    <xsl:template match="@*|node()" mode="s4_user-defined">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()" mode="s4_user-defined"/>
        </xsl:copy>
    </xsl:template>

    <!-- ONLY EXAMPLES FOR INSPIRATION -->
    <!-- Deleting the third child of item. -->
    <xsl:template match="/*/*/*[3]" mode="s4_user-defined" use-when="false()"/>

    <!-- Renaming the first child of item to test -->
    <xsl:template match="/*/*/*[1]" mode="s4_user-defined" use-when="false()">
        <test>
            <xsl:apply-templates select="@*|node()" mode="s4_user-defined"/>
        </test>
    </xsl:template>

</xsl:stylesheet>
