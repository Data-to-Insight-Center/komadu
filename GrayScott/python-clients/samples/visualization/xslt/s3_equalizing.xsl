<?xml version="1.0" encoding="UTF-8"?>
<!-- s3_equalizing.xsl, version 0.9, 2010-09-15 -->
<!-- s3_equalizing.xsl is 4th step of pipeline_xml2csv.xsl, published at www.xmlplease.com/pipeline_xml2csv -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0">
    <xsl:strip-space elements="*"/>
    <xsl:output indent="yes"/>

    <!-- Identity template, mode="s3_equalizing". -->
    <xsl:template match="node()" mode="s3_equalizing">
        <xsl:copy>
            <xsl:apply-templates select="node()" mode="s3_equalizing"/>
        </xsl:copy>
    </xsl:template>

    <!-- Root template, mode="s3_equalizing" -->
    <xsl:template match="/" mode="s3_equalizing">
        <!-- this sub-step adds a children count attribute to each item element -->
        <xsl:variable name="children-count">
            <xsl:apply-templates mode="children-count"/>
        </xsl:variable>
        <!-- this sub-step sorts in descending order the item elements based on the count in the children count attribute. -->
        <xsl:variable name="sort">
            <items>
                <xsl:perform-sort select="$children-count/*/*">
                    <xsl:sort select="@count" data-type="number" order="descending"/>
                </xsl:perform-sort>
            </items>
        </xsl:variable>

        <xsl:variable name="elements" select="$sort/*/*/*"/>
        <xsl:variable name="elements-localname" select="for $a in $elements return local-name($a)"/>
        <xsl:variable name="elements-localname-distinct" select="for $a in distinct-values($elements-localname) return $a"/>

        <xsl:variable name="first">
            <xsl:apply-templates mode="s3_equalizing">
                <xsl:with-param name="elements" tunnel="yes" select="$elements-localname-distinct"/>
            </xsl:apply-templates>
        </xsl:variable>
        
        <xsl:apply-templates mode="s3_equalizing_2" select="$first" use-when="true()"/>
    </xsl:template>

    <!-- Item template, mode="s3_equalizing" -->
    <xsl:template match="/*/*" mode="s3_equalizing">
        <xsl:param name="elements" tunnel="yes"/>
        <xsl:copy>
            <xsl:variable name="item" select="."/>

            <xsl:for-each select="$elements">
                <xsl:variable name="position" select="position()"/>
                <xsl:variable name="element-context" select="."/>

                <xsl:for-each select="$item/*[local-name() = $element-context]">
                    <xsl:variable name="position" select="position()"/>
                    
                    <xsl:element name="{concat($element-context, '_', $position)}">
                        <xsl:value-of select="$item/*[local-name() = $element-context][$position]"/>
                    </xsl:element>
                </xsl:for-each>
            </xsl:for-each>
        </xsl:copy>
    </xsl:template>
    
    <!-- identity template, mode="children-count" -->
    <xsl:template match="node()" mode="children-count">
        <xsl:copy>
            <xsl:apply-templates select="node()" mode="children-count"/>
        </xsl:copy>
    </xsl:template>
    
    <!-- item template, mode="children-count" -->
    <xsl:template match="/*/*" mode="children-count">
        <xsl:copy>
            <xsl:attribute name="count" select="count(*)"/>
            <xsl:apply-templates mode="children-count"/>
        </xsl:copy>
    </xsl:template>
    
    <!-- 22222222222222222222222222222222222222222222222222222222 -->

    <!-- Identity template: mode="s3_equalizing_2" -->
    <xsl:template match="node()" mode="s3_equalizing_2">
        <xsl:copy>
            <xsl:apply-templates select="node()" mode="s3_equalizing_2"/>
        </xsl:copy>
    </xsl:template>

    <!-- Root template: mode="s3_equalizing_2" -->
    <xsl:template match="/" mode="s3_equalizing_2">
        <!-- this sub-step adds a children count attribute to each item element -->
        <xsl:variable name="children-count">
            <xsl:apply-templates mode="children-count"/>
        </xsl:variable>
        <!-- this sub-step sort in descending order the item elements based on the count in the children count attribute. -->
        <xsl:variable name="sort">
            <item>
                <xsl:perform-sort select="$children-count/*/*">
                    <xsl:sort select="@count" data-type="number" order="descending"/>
                </xsl:perform-sort>
            </item>
        </xsl:variable>

        <xsl:variable name="elements" select="$sort/*/*/*"/>
        <xsl:variable name="elements-localname" select="for $a in $elements return local-name($a)"/>
        <xsl:variable name="elements-localname-distinct"
            select="for $a in distinct-values($elements-localname) return $a"/>
        
        <xsl:apply-templates mode="s3_equalizing_2">
            <xsl:with-param name="elements" tunnel="yes" select="$elements-localname-distinct"/>
        </xsl:apply-templates>
    </xsl:template>

    <!-- Item template, mode="s3_equalizing_2" -->
    <xsl:template match="/*/*" mode="s3_equalizing_2">
        <xsl:param name="elements" tunnel="yes"/>
        <xsl:copy>
            <xsl:variable name="item" select="."/>
            <xsl:for-each select="$elements">
                <xsl:variable name="position" select="position()"/>
                <xsl:variable name="element-context" select="."/>
                <xsl:element name="{string-join(tokenize(., '_')[position() != last()], '_')}">
                    <xsl:value-of select="$item/*[local-name() = $element-context]"/>
                </xsl:element>
            </xsl:for-each>
        </xsl:copy>
    </xsl:template>
</xsl:stylesheet>