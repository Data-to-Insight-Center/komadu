package edu.indiana.d2i.komadu.ingest;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

import org.apache.xmlbeans.SchemaTypeLoader;
import org.apache.xmlbeans.XmlBeans;
import org.apache.xmlbeans.XmlError;
import org.apache.xmlbeans.XmlException;
import org.apache.xmlbeans.XmlObject;
import org.apache.xmlbeans.XmlOptions;

public class Validation {
	public static boolean validate(File dataFile, File schemaFile) {
		boolean status = false;

		try {
			// Only one schema to validate it against
			XmlObject[] schemas = { XmlObject.Factory.parse(schemaFile,
					new XmlOptions().setLoadLineNumbers()
							.setLoadMessageDigest()) };

			SchemaTypeLoader loader = XmlBeans.compileXsd(schemas, null,
					new XmlOptions().setErrorListener(null)
							.setCompileDownloadUrls().setCompileNoPvrRule());

			XmlObject object = loader
					.parse(dataFile,
							null,
							new XmlOptions()
									.setLoadLineNumbers(XmlOptions.LOAD_LINE_NUMBERS_END_ELEMENT));

			XmlOptions ValidateOptions = new XmlOptions();
			ArrayList errorList = new ArrayList();
			ValidateOptions.setErrorListener(errorList);
			
			status = object.validate(ValidateOptions);
			
			System.out.println("Validation Status: " + status);
			
			if(!status)
			{
				String error_message="";
				for (int i = 0; i < errorList.size(); i++)
			     {
			          XmlError error = (XmlError)errorList.get(i);
			          error_message+="\n";
			          error_message+="Message: " + error.getMessage() + "\n";
			          error_message+="Location of invalid XML: " + error.getCursorLocation().xmlText() + "\n";
			      }
				System.out.println("Validation diagnose: "+error_message);
			}
			
		} catch (XmlException e1) {
			e1.printStackTrace();
		} catch (IOException e1) {
			e1.printStackTrace();
		}

		return status;
	}
	
	public static boolean validate(XmlObject dataObject, File schemaFile)
	{
		boolean status = false;
		
		try {
			// Only one schema to validate it against
			XmlObject[] schemas = { XmlObject.Factory.parse(schemaFile,
					new XmlOptions().setLoadLineNumbers()
							.setLoadMessageDigest()) };

			SchemaTypeLoader loader = XmlBeans.compileXsd(schemas, null,
					new XmlOptions().setErrorListener(null)
							.setCompileDownloadUrls().setCompileNoPvrRule());
			
			XmlObject object = loader
					.parse(dataObject.xmlText(),
							null,
							new XmlOptions()
									.setLoadLineNumbers(XmlOptions.LOAD_LINE_NUMBERS_END_ELEMENT));

			
			XmlOptions ValidateOptions = new XmlOptions();
			ArrayList errorList = new ArrayList();
			ValidateOptions.setErrorListener(errorList);
			
			status = object.validate(ValidateOptions);
			
			System.out.println("Validation Status: " + status);
			
			if(!status)
			{
				String error_message="";
				for (int i = 0; i < errorList.size(); i++)
			     {
			          XmlError error = (XmlError)errorList.get(i);
			          error_message+="\n";
			          error_message+="Message: " + error.getMessage() + "\n";
			          error_message+="Location of invalid XML: " + error.getCursorLocation().xmlText() + "\n";
			      }
				System.out.println("Validation diagnose: "+error_message);
			}
			
		} catch (XmlException e1) {
			e1.printStackTrace();
		} catch (IOException e1) {
			e1.printStackTrace();
		}

		
		return status;
	}
	
	public static boolean validate(String dataString, File schemaFile)
	{
		boolean status = false;
		
		try {
			// Only one schema to validate it against
			XmlObject[] schemas = { XmlObject.Factory.parse(schemaFile,
					new XmlOptions().setLoadLineNumbers()
							.setLoadMessageDigest()) };

			SchemaTypeLoader loader = XmlBeans.compileXsd(schemas, null,
					new XmlOptions().setErrorListener(null)
							.setCompileDownloadUrls().setCompileNoPvrRule());

			XmlObject dataObject = loader
					.parse(dataString,
							null,
							new XmlOptions()
									.setLoadLineNumbers(XmlOptions.LOAD_LINE_NUMBERS_END_ELEMENT));

			
			XmlOptions ValidateOptions = new XmlOptions();
			ArrayList errorList = new ArrayList();
			ValidateOptions.setErrorListener(errorList);
			
			status = dataObject.validate(ValidateOptions);
			
			System.out.println("Validation Status: " + status);
			
			if(!status)
			{
				String error_message="";
				for (int i = 0; i < errorList.size(); i++)
			     {
			          XmlError error = (XmlError)errorList.get(i);
			          error_message+="\n";
			          error_message+="Message: " + error.getMessage() + "\n";
			          error_message+="Location of invalid XML: " + error.getCursorLocation().xmlText() + "\n";
			      }
				System.out.println("Validation diagnose: "+error_message);
			}
			
		} catch (XmlException e1) {
			e1.printStackTrace();
		} catch (IOException e1) {
			e1.printStackTrace();
		}

		
		return status;
	}
}
