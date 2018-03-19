# What do I do?
As a content editor you will start with the base question and response spreadsheet and review all of the questions and responses for suitability for your institution. 
We have highlighted in red words or phrases that you will most likely have to modify. These include terminology that may differ between institutions e.g. unit vs subject, names of specific systems e.g. student portal name (could be LearnJCU, Moodle, ...) and contact details and links to where further information can be found in your institution's systems.
There is a chance that we have missed highlighting a word or phrase that needs changing to be a good fit for your institution so do please read critically.
There is one question 'p-personalcontact' that definitely only applies to some institutions, we've marked the whole row red. Just delete it if it doesn't apply to yours.
Do not add or delete columns or modify column headers please.
For the purposes of this project no rows should be added or deleted either unless absolutely necessary.


## Spreadsheet Columns explained
|Column name | What goes here?
|--- | ---
|Section | Questions should be grouped with other similar questions. Ideally each section will have an introduction that helps the student get their bearings and helps them realise that any problems they may have are shared by others and they probably aren't the first.
The section name should be brief but must be text that you would be happy to see on the web-site. They will be used as a quick jump in point for a student returning to the tool for whatever reason.
|Question Code | A short code that uniquely identifies this question. It will be used within the responses to specify which question is next after the student has selected a particular response. Usually the flow will be onto the next question (this is the default behaviour) but if you want to skip the next question based on a particular response then you must specify which is the next question to jump to. This is done by adding `GOTO:`<question code> at the end of the response text. This will never be visible on the web-site.
|Question / Statement | This text will be shown in the conversation bubble from the university's avatar. It can be a statement of information or a question that elicits a response. You may use formatting in this content - Content formatting explained.
|Possible Responses | Comma separated, brief responses for the student to choose between to answer the question. Try to keep to a consistent voice - don't swap between formal and informal. Do try to mix up the responses a bit, don't always have *yes,no* or it will become a bit of a blur for the user. Think about adding a *not sure* option so that they don't feel pressured if they aren't confident of exactly what the question was trying to elicit. These responses will get displayed in the order that you enter them here and with the same capitalisation and spelling.
|If they choose response 1 | This is what will happen if they choose the 1st response from the list in the `Possible Responses column` (when reading left to right). Any text here will be only be displayed if the student selected this response. You may use formatting in this text, see `Content formatting explained`. It will be displayed in another conversation bubble. If this field is left empty no additional text will be displayed and the next question in the spreadsheet will start immediately after the response is selected. If you want to direct them to a different question after selecting this response then you must tell us by adding `GOTO:`<question code> here.
|If they choose response 2-5 | Exactly the behaviour as for `If they choose response 1`.


## Content formatting explained
Wat I want to achieve | Format to use | Details
--- | --- | ---
**New bubble** | && | Adding `&&` anywhere in the content of a question or a response will cause the content following the && to be displayed in a new conversation bubble in the online conversation.
**Add a hyperlink** | `[`text to show`](`url that you want that text to link to`)` | In the final conversation (once the spreadsheet has been converted) this will display some text and hyperlink it to the URL that you specify in the round brackets. If you just want the URL to show as is and be hyperlinked then just type it straight in without any other formatting. Don't forget the http:// or https:// prefix. Example: `[Read XKCD](https://www.xkcd.com/557/)` becomes (after processing) [Read XKCD](https://www.xkcd.com/557/).

# What happens next?
After you have updated your version of the spreadsheet you need to email it to the online self-assessment tool admin at **EMAIL ADDRESS HERE**.
The admin will process the spreadsheet and generate the online conversation and a flowchart for the conversation.


