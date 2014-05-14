Komadu Transformation Tool
==========================

This tool transforms a PROV xml into two CSV files: an edge list CSV and a node list CSV. These CSV files can be 
imported and visualized by many standard visualization tools including Cytoscape and Gephi.

Software Dependency:
Before you start to use this tool, you have to install a XSLT engine. This is because, essentially, this tool 
comprises a list of XSLT documents.
These XSLT documents should be executable from any standard XSLT engine. For example, we've installed SAXON-HE:
http://saxon.sourceforge.net/ 

How to Use:
In the 'visualization' directory, type command in your terminal:
java net.sf.saxon.Transform -s:<your-PROV-file> -xsl:xslt/pipeline_xml2csv.xsl

We've provided some example PROV files in 'samples' directory, and you can transform those using command:
java net.sf.saxon.Transform -s:sample1.xml -xsl:xslt/pipeline_xml2csv.xsl

After it finishes, you'll see two CSV files: 'edges.csv' and 'nodes.csv'.
For information about how to import these two CSV files into visualization tools such as Cytoscape, please read 
their manuals, for example:
http://wiki.cytoscape.org/Cytoscape_3/UserManual#Cytoscape_3.2BAC8-UserManual.2BAC8-Creating_Networks.Import_Networks_from_Unformatted_Table_Files

Below is a brief summary of importing CSV files into Cytoscape:
1, Import Network From File:
Choose 'edges.csv'. Check 'Show TextFile Import Options', make sure you select 'Comma' as delimiter and check the option 'Transfer first line as column name'. Select the right 'Source' (2nd column), 'Interaction' (1st), and 'Target' (3rd). Left clicks to enable the columns that you want to import as attributes.

2, Import Table From File:
Choose 'nodes.csv'. Check 'Show Text File Import Options', make sure you select 'Comma' as delimiter and check the option 'Transfer first line as column name'. Check 'Show Mapping Options' and the 'primary key' should be default to 'id' already.

3, Apply Visual Style
Import vismap through 'File-->Import-->Vismap File', and select 'style/prov-visMap.xml'. Apply the 'PROV' visual style by right click on the network from the network control panel and choose 'Apply Visual Style', then select 'PROV' from the list. We recommend to choose 'Layout-->Hierarchical Layout' as the first layout algorithm.
