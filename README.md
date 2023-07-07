POC to demonstrate possibility of ServiceNow development using a framework outside of ServiceNow.  Built with assistance from Chat GPT . This will generate a valid 'before' business rule that runs on insert and update on the task table. Please only use in PDI , I make no guarantees of warranty lol.


#Usage

1. Look at business_rule.yaml and update fields such as collection (the table) and name to personalize the business rule. This is currently just a direct translation of xml fields from a template business rule created in my PDI , but the hope is to abstract most of these fields away in the future to utlize a simplified framework.

2. Update script.js as you would the 'script' field of a business rule.

3. Make sure to have the python packages uuid , yaml, and lxml accessible in the environment you plan to execute this xml generator in.

4. Run genBus.py which will generate an xml file ready to import into your pdi. 
