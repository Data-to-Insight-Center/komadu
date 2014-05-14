<?xml version="1.0" encoding="UTF-8"?>
<!-- s1_extract_edges.xsl, version 0.9, 2010-09-15 -->
<!-- s1_user-defdined.xsl is first step of pipeline_xml2csv.xsl, published at www.xmlplease.com/pipeline_xml2csv -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:prov="http://www.w3.org/ns/prov#"
    xmlns:kom="http://komadu.d2i.indiana.edu" xmlns:ext="http://komadu.d2i.indiana.edu/external"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs" version="2.0">
    <xsl:strip-space elements="*"/>
    <xsl:output indent="yes"/>

    <xsl:template match="prov:document" mode="s1_extract_edges">
        <xsl:copy>
            <xsl:apply-templates select="prov:used" mode="s1_extract_edges"/>
            <xsl:apply-templates select="prov:wasGeneratedBy" mode="s1_extract_edges"/>
            <xsl:apply-templates select="prov:wasDerivedFrom" mode="s1_extract_edges"/>
            <xsl:apply-templates select="prov:wasAssociatedWith" mode="s1_extract_edges"/>
	    <xsl:apply-templates select="prov:actedOnBehalfOf" mode="s1_extract_edges"/>
	    <xsl:apply-templates select="prov:alternateOf" mode="s1_extract_edges"/>
	    <xsl:apply-templates select="prov:wasAttributedTo" mode="s1_extract_edges"/>
	    <xsl:apply-templates select="prov:specializationOf" mode="s1_extract_edges"/>
	    <xsl:apply-templates select="prov:wasInformedBy" mode="s1_extract_edges"/>
	    <xsl:apply-templates select="prov:wasInvalidatedBy" mode="s1_extract_edges"/>
	    <xsl:apply-templates select="prov:wasStartedBy" mode="s1_extract_edges"/>
	    <xsl:apply-templates select="prov:wasEndedBy" mode="s1_extract_edges"/>
	    <xsl:apply-templates select="prov:wasRevisionOf" mode="s1_extract_edges"/>
	    <xsl:apply-templates select="prov:wasQuotedFrom" mode="s1_extract_edges"/>
	    <xsl:apply-templates select="prov:hadPrimarySource" mode="s1_extract_edges"/>
	    <xsl:apply-templates select="prov:wasInfluencedBy" mode="s1_extract_edges"/>
	    <xsl:apply-templates select="prov:hadMember" mode="s1_extract_edges"/>
	    <xsl:apply-templates select="prov:mentionOf" mode="s1_extract_edges"/>
        </xsl:copy>
    </xsl:template>
    
    <!--  Rewrite the used relations -->
    <xsl:template match="/prov:document/prov:used" mode="s1_extract_edges">
        <xsl:copy>
            <prov:edgeType>used</prov:edgeType>
            <xsl:apply-templates select="node()" mode="s1_extract_edges"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:used/prov:activity" mode="s1_extract_edges" priority="5">
        <prov:source>
            <xsl:value-of select="@prov:ref"/>
        </prov:source>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:used/prov:entity" mode="s1_extract_edges" priority="5">
        <prov:dest>
            <xsl:value-of select="@prov:ref"/>
        </prov:dest>
    </xsl:template>

    <xsl:template match="/prov:document/prov:used/*" mode="s1_extract_edges">
        <xsl:copy-of select="."/>
    </xsl:template>
    
    <!--<xsl:template match="/prov:document/prov:used//@*|/prov:document/prov:used//node()" mode="s1_extract_edges">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()" mode="s1_extract_edges"/>
        </xsl:copy>
    </xsl:template>-->
    
    <!--  Rewrite the wasGeneratedBy relations -->
    <xsl:template match="/prov:document/prov:wasGeneratedBy" mode="s1_extract_edges">
        <xsl:copy>
            <prov:edgeType>wasGeneratedBy</prov:edgeType>
            <xsl:apply-templates select="node()" mode="s1_extract_edges"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasGeneratedBy/prov:entity" mode="s1_extract_edges" priority="5">
        <prov:source>
            <xsl:value-of select="@prov:ref"/>
        </prov:source>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasGeneratedBy/prov:activity" mode="s1_extract_edges" priority="5">
        <prov:dest>
            <xsl:value-of select="@prov:ref"/>
        </prov:dest>
    </xsl:template>

    <xsl:template match="/prov:document/prov:wasGeneratedBy/*" mode="s1_extract_edges">
        <xsl:copy-of select="."/>
    </xsl:template>
    
    <!--  Rewrite the wasDerivedFrom relations -->
    <xsl:template match="/prov:document/prov:wasDerivedFrom" mode="s1_extract_edges">
        <xsl:copy>
            <prov:edgeType>wasDerivedFrom</prov:edgeType>
            <xsl:apply-templates select="node()" mode="s1_extract_edges"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasDerivedFrom/prov:generatedEntity" mode="s1_extract_edges" priority="5">
        <prov:source>
            <xsl:value-of select="@prov:ref"/>
        </prov:source>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasDerivedFrom/prov:usedEntity" mode="s1_extract_edges" priority="5">
        <prov:dest>
            <xsl:value-of select="@prov:ref"/>
        </prov:dest>
    </xsl:template>

    <xsl:template match="/prov:document/prov:wasDerivedFrom/*" mode="s1_extract_edges">
        <xsl:copy-of select="."/>
    </xsl:template>
    
    <!--  Rewrite the wasAssociatedWith relations -->
    <!--  currently we capture 'plan' as an attribute -->
    <!--  break a one-to-many relation into many one-to-one relations -->
    <xsl:template match="/prov:document/prov:wasAssociatedWith" mode="s1_extract_edges">
        <xsl:apply-templates select="node()" mode="s1_extract_edges"/>
    </xsl:template>

    <xsl:template match="/prov:document/prov:wasAssociatedWith/prov:activity" mode="s1_extract_edges" priority="5">
	<prov:wasAssociatedWith>
            <prov:edgeType>wasAssociatedWith</prov:edgeType>
            <prov:source>
                <xsl:value-of select="@prov:ref"/>
            </prov:source>
            <prov:dest>
                <xsl:value-of select="parent::prov:wasAssociatedWith/prov:agent/@prov:ref"/>
            </prov:dest>
	    <!--  copy all other children -->
            <xsl:copy-of select="parent::prov:wasAssociatedWith/*[not(self::prov:activity or self::prov:agent)]"/>
	</prov:wasAssociatedWith>
    </xsl:template>

    <!--  avoid the duplicate copy of others -->
    <xsl:template match="/prov:document/prov:wasAssociatedWith/*" mode="s1_extract_edges"/>

    <!--  Rewrite the actedOnBehalfOf relations -->
    <!--  currently capture 'activity' as an attribute -->
    <xsl:template match="/prov:document/prov:actedOnBehalfOf" mode="s1_extract_edges">
        <xsl:copy>
            <prov:edgeType>actedOnBehalfOf</prov:edgeType>
            <xsl:apply-templates select="node()" mode="s1_extract_edges"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:actedOnBehalfOf/prov:delegate" mode="s1_extract_edges" priority="5">
        <prov:source>
            <xsl:value-of select="@prov:ref"/>
        </prov:source>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:actedOnBehalfOf/prov:responsible" mode="s1_extract_edges" priority="5">
        <prov:dest>
            <xsl:value-of select="@prov:ref"/>
        </prov:dest>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:actedOnBehalfOf/*" mode="s1_extract_edges">
        <xsl:copy-of select="."/>
    </xsl:template>

    <!--  Rewrite the alternateOf relations -->
    <xsl:template match="/prov:document/prov:alternateOf" mode="s1_extract_edges">
        <xsl:copy>
            <prov:edgeType>alternateOf</prov:edgeType>
            <xsl:apply-templates select="node()" mode="s1_extract_edges"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:alternateOf/prov:alternate1" mode="s1_extract_edges" priority="5">
        <prov:source>
            <xsl:value-of select="@prov:ref"/>
        </prov:source>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:alternateOf/prov:alternate2" mode="s1_extract_edges" priority="5">
        <prov:dest>
            <xsl:value-of select="@prov:ref"/>
        </prov:dest>
    </xsl:template>

    <xsl:template match="/prov:document/prov:alternateOf/*" mode="s1_extract_edges">
        <xsl:copy-of select="."/>
    </xsl:template>

    <!--  Rewrite the wasAttributedTo relations -->
    <xsl:template match="/prov:document/prov:wasAttributedTo" mode="s1_extract_edges">
        <xsl:copy>
            <prov:edgeType>wasAttributedTo</prov:edgeType>
            <xsl:apply-templates select="node()" mode="s1_extract_edges"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasAttributedTo/prov:entity" mode="s1_extract_edges" priority="5">
        <prov:source>
            <xsl:value-of select="@prov:ref"/>
        </prov:source>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasAttributedTo/prov:agent" mode="s1_extract_edges" priority="5">
        <prov:dest>
            <xsl:value-of select="@prov:ref"/>
        </prov:dest>
    </xsl:template>

    <xsl:template match="/prov:document/prov:wasAttributedTo/*" mode="s1_extract_edges">
        <xsl:copy-of select="."/>
    </xsl:template>

    <!--  Rewrite the specializationOf relations -->
    <xsl:template match="/prov:document/prov:specializationOf" mode="s1_extract_edges">
        <xsl:copy>
            <prov:edgeType>specializationOf</prov:edgeType>
            <xsl:apply-templates select="node()" mode="s1_extract_edges"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:specializationOf/prov:specificEntity" mode="s1_extract_edges" priority="5">
        <prov:source>
            <xsl:value-of select="@prov:ref"/>
        </prov:source>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:specializationOf/prov:generalEntity" mode="s1_extract_edges" priority="5">
        <prov:dest>
            <xsl:value-of select="@prov:ref"/>
        </prov:dest>
    </xsl:template>

    <xsl:template match="/prov:document/prov:specializationOf/*" mode="s1_extract_edges">
        <xsl:copy-of select="."/>
    </xsl:template>

    <!--  Rewrite the wasInformedBy relations -->
    <xsl:template match="/prov:document/prov:wasInformedBy" mode="s1_extract_edges">
        <xsl:copy>
            <prov:edgeType>wasInformedBy</prov:edgeType>
            <xsl:apply-templates select="node()" mode="s1_extract_edges"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasInformedBy/prov:informed" mode="s1_extract_edges" priority="5">
        <prov:source>
            <xsl:value-of select="@prov:ref"/>
        </prov:source>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasInformedBy/prov:informant" mode="s1_extract_edges" priority="5">
        <prov:dest>
            <xsl:value-of select="@prov:ref"/>
        </prov:dest>
    </xsl:template>

    <xsl:template match="/prov:document/prov:wasInformedBy/*" mode="s1_extract_edges">
        <xsl:copy-of select="."/>
    </xsl:template>

    <!--  Rewrite the wasInvalidatedBy relations -->
    <xsl:template match="/prov:document/prov:wasInvalidatedBy" mode="s1_extract_edges">
        <xsl:copy>
            <prov:edgeType>wasInvalidatedBy</prov:edgeType>
            <xsl:apply-templates select="node()" mode="s1_extract_edges"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasInvalidatedBy/prov:entity" mode="s1_extract_edges" priority="5">
        <prov:source>
            <xsl:value-of select="@prov:ref"/>
        </prov:source>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasInvalidatedBy/prov:activity" mode="s1_extract_edges" priority="5">
        <prov:dest>
            <xsl:value-of select="@prov:ref"/>
        </prov:dest>
    </xsl:template>

    <xsl:template match="/prov:document/prov:wasInvalidatedBy/*" mode="s1_extract_edges">
        <xsl:copy-of select="."/>
    </xsl:template>

    <!--  Rewrite the wasStartedBy relations -->
    <!-- currently we capture 'starter' as an attribute -->
    <xsl:template match="/prov:document/prov:wasStartedBy" mode="s1_extract_edges">
        <xsl:copy>
            <prov:edgeType>wasStartedBy</prov:edgeType>
            <xsl:apply-templates select="node()" mode="s1_extract_edges"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasStartedBy/prov:activity" mode="s1_extract_edges" priority="5">
        <prov:source>
            <xsl:value-of select="@prov:ref"/>
        </prov:source>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasStartedBy/prov:trigger" mode="s1_extract_edges" priority="5">
        <prov:dest>
            <xsl:value-of select="@prov:ref"/>
        </prov:dest>
    </xsl:template>

    <xsl:template match="/prov:document/prov:wasStartedBy/*" mode="s1_extract_edges">
        <xsl:copy-of select="."/>
    </xsl:template>

    <!--  Rewrite the wasEndedBy relations -->
    <!-- currently we capture 'ender' as an attribute -->
    <xsl:template match="/prov:document/prov:wasEndedBy" mode="s1_extract_edges">
        <xsl:copy>
            <prov:edgeType>wasEndedBy</prov:edgeType>
            <xsl:apply-templates select="node()" mode="s1_extract_edges"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasEndedBy/prov:activity" mode="s1_extract_edges" priority="5">
        <prov:source>
            <xsl:value-of select="@prov:ref"/>
        </prov:source>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasEndedBy/prov:trigger" mode="s1_extract_edges" priority="5">
        <prov:dest>
            <xsl:value-of select="@prov:ref"/>
        </prov:dest>
    </xsl:template>

    <xsl:template match="/prov:document/prov:wasEndedBy/*" mode="s1_extract_edges">
        <xsl:copy-of select="."/>
    </xsl:template>

    <!--  Rewrite the wasRevisionOf relations -->
    <xsl:template match="/prov:document/prov:wasRevisionOf" mode="s1_extract_edges">
        <xsl:copy>
            <prov:edgeType>wasRevisionOf</prov:edgeType>
            <xsl:apply-templates select="node()" mode="s1_extract_edges"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasRevisionOf/prov:generatedEntity" mode="s1_extract_edges" priority="5">
        <prov:source>
            <xsl:value-of select="@prov:ref"/>
        </prov:source>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasRevisionOf/prov:usedEntity" mode="s1_extract_edges" priority="5">
        <prov:dest>
            <xsl:value-of select="@prov:ref"/>
        </prov:dest>
    </xsl:template>

    <xsl:template match="/prov:document/prov:wasRevisionOf/*" mode="s1_extract_edges">
        <xsl:copy-of select="."/>
    </xsl:template>

    <!--  Rewrite the wasQuotedFrom relations -->
    <xsl:template match="/prov:document/prov:wasQuotedFrom" mode="s1_extract_edges">
        <xsl:copy>
            <prov:edgeType>wasQuotedFrom</prov:edgeType>
            <xsl:apply-templates select="node()" mode="s1_extract_edges"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasQuotedFrom/prov:generatedEntity" mode="s1_extract_edges" priority="5">
        <prov:source>
            <xsl:value-of select="@prov:ref"/>
        </prov:source>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasQuotedFrom/prov:usedEntity" mode="s1_extract_edges" priority="5">
        <prov:dest>
            <xsl:value-of select="@prov:ref"/>
        </prov:dest>
    </xsl:template>

    <xsl:template match="/prov:document/prov:wasQuotedFrom/*" mode="s1_extract_edges">
        <xsl:copy-of select="."/>
    </xsl:template>

    <!--  Rewrite the hadPrimarySource relations -->
    <xsl:template match="/prov:document/prov:hadPrimarySource" mode="s1_extract_edges">
        <xsl:copy>
            <prov:edgeType>hadPrimarySource</prov:edgeType>
            <xsl:apply-templates select="node()" mode="s1_extract_edges"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:hadPrimarySource/prov:generatedEntity" mode="s1_extract_edges" priority="5">
        <prov:source>
            <xsl:value-of select="@prov:ref"/>
        </prov:source>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:hadPrimarySource/prov:usedEntity" mode="s1_extract_edges" priority="5">
        <prov:dest>
            <xsl:value-of select="@prov:ref"/>
        </prov:dest>
    </xsl:template>

    <xsl:template match="/prov:document/prov:hadPrimarySource/*" mode="s1_extract_edges">
        <xsl:copy-of select="."/>
    </xsl:template>

    <!--  Rewrite the wasInfluencedBy relations -->
    <xsl:template match="/prov:document/prov:wasInfluencedBy" mode="s1_extract_edges">
        <xsl:copy>
            <prov:edgeType>wasInfluencedBy</prov:edgeType>
            <xsl:apply-templates select="node()" mode="s1_extract_edges"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasInfluencedBy/prov:influencee" mode="s1_extract_edges" priority="5">
        <prov:source>
            <xsl:value-of select="@prov:ref"/>
        </prov:source>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:wasInfluencedBy/prov:influencer" mode="s1_extract_edges" priority="5">
        <prov:dest>
            <xsl:value-of select="@prov:ref"/>
        </prov:dest>
    </xsl:template>

    <xsl:template match="/prov:document/prov:wasInfluencedBy/*" mode="s1_extract_edges">
        <xsl:copy-of select="."/>
    </xsl:template>

    <!--  Rewrite the hadMember relations -->
    <!-- hadMember is a one-to-many relationship, so we break it into many new hadMember one-to-one relations -->
    <xsl:template match="/prov:document/prov:hadMember" mode="s1_extract_edges">
        <xsl:apply-templates select="node()" mode="s1_extract_edges"/>
    </xsl:template>

    <xsl:template match="/prov:document/prov:hadMember/prov:entity" mode="s1_extract_edges">
	<prov:hadMember>
            <prov:edgeType>hadMember</prov:edgeType>
            <prov:source>
                <xsl:value-of select="parent::prov:hadMember/prov:collection/@prov:ref"/>
            </prov:source>
            <prov:dest>
                <xsl:value-of select="@prov:ref"/>
            </prov:dest>
	</prov:hadMember>
    </xsl:template>

    <!--  Rewrite the mentionOf relations -->
    <!--  currrently capture 'bundle' as attributes -->
    <xsl:template match="/prov:document/prov:mentionOf" mode="s1_extract_edges">
        <xsl:copy>
            <prov:edgeType>mentionOf</prov:edgeType>
            <xsl:apply-templates select="node()" mode="s1_extract_edges"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:mentionOf/prov:specificEntity" mode="s1_extract_edges" priority="5">
        <prov:source>
            <xsl:value-of select="@prov:ref"/>
        </prov:source>
    </xsl:template>
    
    <xsl:template match="/prov:document/prov:mentionOf/prov:generalEntity" mode="s1_extract_edges" priority="5">
        <prov:dest>
            <xsl:value-of select="@prov:ref"/>
        </prov:dest>
    </xsl:template>

    <xsl:template match="/prov:document/prov:mentionOf/*" mode="s1_extract_edges">
        <xsl:copy-of select="."/>
    </xsl:template>

    <!-- ONLY EXAMPLES FOR INSPIRATION -->
    <!-- Deleting the third child of item. -->
    <xsl:template match="/*/*/*[3]" mode="s1_extract_edges" use-when="false()"/>

    <!-- Renaming the first child of item to test -->
    <xsl:template match="/*/*/*[1]" mode="s1_extract_edges" use-when="false()">
        <test>
            <xsl:apply-templates select="@*|node()" mode="s1_extract_edges"/>
        </test>
    </xsl:template>

</xsl:stylesheet>
