# NYPD-disciplinary-proceedings
Scraping, cleaning, visualization, and analysis of NYPD disciplinary proceedings (2011-2015)

### Background
On April 16th, 2018, records were made public of ~1,800 New York City police department employees with departmental misconduct charges brought between 2011 and 2015. This information allows us to launch an evidence-based assessment of the department’s disciplinary system. There are not resources available online to search for problematic officers in NYC; [a few options](https://openoversight.lucyparsonslabs.com/find "OpenOversight") exist for a handful of cities. 

### Data
This data was made public by an anonymous source within the NYPD. [Buzzfeed](https://www.buzzfeed.com/kendalltaggart/nypd-police-misconduct-database?utm_term=.mvV5dKZp0#.xcqdjR5Xw) delivered a .csv file with officer names and links to PDFs of the records. Each PDF contains multiple records. We scrape and parse the text to extract the employee name, rank, specification(s), disposition, penalty, date of disposition, and date of charges. 

### Objectives 

We are not attempting to make the disciplinary system more fair with this project. Rather, we are trying to hold officers accountable to the current rules in place. This project is in response to the failure of leaders in local governments to implement systems that effectively and safely allow the public to identify and report problematic police officers.

### Specifications
1. Searchable web application
2. Data visualization describing the relationship between the type of misconduct and penalty
    * Investigate officers with repeated allegations of misconduct. Do the punishments increase with repeated violations of policy and procedure?
3. Statistical analysis
    * Establish the relationship between degree of offense and penalty received.
    * Does pre-employment history matter in degree of punishment? I.e., are officers whose life histories include records of arrest, traffic violations, and failure in other jobs are more likely than other officers to be involuntarily separated from the NYPD? What role does training and education have in severity of punishment received? 
    * Will variations in community structure (i.e., per capita income, % minority population) and public crime (homicide, FBI index crimes) predict variations in police misconduct within police precincts over time?
    * Do police officers with more connections in the department receive less serious punishment? 
      * Subset analysis to cases that resulted in involuntary separation. 
      
### Contributing
[Hope Johnson](hopecaneel@gmail.com) (code, documentation) and Jason Stein (code). 


