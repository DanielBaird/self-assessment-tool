# What do I do?
As a content editor you will start with the base question and response spreadsheet and review all of the questions and responses for suitability for your institution.

We have highlighted in **red** words or phrases that you will most likely have to modify. These include terminology that may differ between institutions e.g. unit vs subject, names of specific systems e.g. student portal name (could be LearnJCU, Moodle, ...) and contact details and links to where further information can be found in your institution's systems.

There is a chance that we have missed highlighting a word or phrase that needs changing to be a good fit for your institution so do please read critically.

You can change more than just the highlighted words to make the wording a good fit for your purpose.

There is one question 'p-personalcontact' that definitely only applies to some institutions, we've marked the whole row red. Just delete it if it doesn't apply to yours.

**Do not add or delete or rearrange columns or modify column headers please.**
For the purposes of this project no rows should be added or deleted either unless absolutely necessary.


## Spreadsheet Columns explained
The spreadsheet has nine columns. These should not be renamed, deleted or rearranged in any way.

The purpose of each column is explained below:

#### Section
Questions should be grouped with other similar questions. Ideally each section will have an introduction that helps the student get their bearings and helps them realise that any problems they may have are shared by others and they probably aren't the first.

The section name should be brief but must be text that you would be happy to see on the web-site. They will be used as a quick jump in point for a student returning to the tool for whatever reason.
#### Question Code
A short code that uniquely identifies this question. 

It will be used within the responses to specify which question is next after the student has selected a particular response. Usually the flow will be onto the next question (this is the default behaviour) but if you want to skip the next question based on a particular response then you must specify which is the next question to jump to. This is done by adding `GOTO:<question code>` at the end of the response text. 

The question code will never be visible on the web-site.
#### Question / Statement 
This text will be shown in a conversation bubble from the university's avatar. It can be a statement of information or a question that elicits a response. 

You may use formatting in this content, see [Content formatting explained](#content-formatting-explained).
#### Possible Responses
These are brief responses for the student to choose between to answer the question. They must be comma separated, for example `yes, no, not sure`.

Try to keep to a consistent voice - don't swap between formal and informal. Do try to mix up the responses a bit, don't always have *yes,no* or it will become a bit of a blur for the user. Think about adding a *not sure* option so that they don't feel pressured if they aren't confident of exactly what the question was trying to elicit. 

These responses will get displayed in the order that you enter them here and with the same capitalisation and spelling.
#### If they choose response 1
This is what will happen if they choose the 1st response from the list in the `Possible Responses column` (when reading left to right). Any text here will be only be displayed if the student selected this response. 

You may use formatting in this text, see [Content formatting explained](#content-formatting-explained). 

The text will be displayed in another conversation bubble. If this field is left empty no additional text will be displayed and the next question in the spreadsheet will start immediately after the response is selected. If you want to direct them to a different question after selecting this response then you must tell us by adding `GOTO:<question code>` here. For example, if I want to direct a user who has selected the response `yes` to skip the next question I would get the `Question Code` of the next question I wanted them to see, e.g. `lb-studyload`, and add `GOTO:lb-studyload` at the end of any text in this cell.

#### If they choose response 2-5
Exactly the behaviour as for `If they choose response 1`.


## Content formatting explained
Markdown can be used in the `Question / Statement` and `If they choose responseX` column content to provide simple formatting such as bold, italics and hyperlinks to other web pages. Note: **The formatting will not show up in the spreadsheet, it will only be visible in the final conversation after the spreadsheet has been processed.**

#### Bold
Any words you put inside double asterisks `**` will be bolded. For example
`An **apple** and an orange`
becomes
An **apple** and an orange.

#### Italics
Any words or letters you encase in underscores `_` will become italicised.
For example `An apple and an _orange_`
becomes
An apple and an _orange_.

#### Break up text into multiple bubbles
Adding `&&` anywhere in the content of a question or a response will cause the content following the `&&` to be displayed in a new conversation bubble in the online conversation. This is useful for breaking up longer blocks of text, there will be a pause before each new conversation bubble is presented, giving the student time to read the contents of the one before.

#### Add a hyperlink
`[text to show](url that you want that text to link to)`

In the final conversation (once the spreadsheet has been converted) this will display some text and hyperlink it to the URL that you specify in the round brackets. If you just want the URL to show as is and be hyperlinked then just type it straight in without any other formatting. Don't forget the http:// or https:// prefix. 

For example: `[Read XKCD](https://www.xkcd.com/557/)` 
after processing becomes 
[Read XKCD](https://www.xkcd.com/557/).

#### Add an image
`![text to show on hover](url of the image or image filename)`

In the online conversation this will cause a thumbnail of the image to be displayed and when the image is clicked on it will expand to full size. The text given will show on hover and be available to screen readers and thus help people with visual impairment. The image can be one you have provided with the spreadsheet, in which case just put the filename inside the `()`s OR it can be one available from another server in your institution in which case provide the full URL inside the `()`s.

#### Ask the user to type something in
`{text}`

This markdown only works in the [Possible responses](#possible-responses) column. Including `{text}` as the possible response will prompt the user to enter something using their keyboard.
For example: If a row in your spreadsheet has these column values: 

| Section |Question Code | Question / Statement | Possible Responses
|---------|--------------|----------------------|--------------------
|         |`q-askname`   | `What is your name?` | `{text}`

then the user will be asked `What is your name?`, and given a space to type it.

To use the result of this query see [Use something the user typed](#use-something-the-user-typed).

#### Use something the user typed
`{question-id}`

Any time after you have used a `{text}` response to get the user to type something, you can show them what they typed by putting that *question-id* into curly brackets, {}.

For example: `Hi {q-askname}, did you know about the cheap beer on Fridays?` would become: Hi Aragorn, did you know about the cheap beer on Fridays?

Assuming the student had entered 'Aragorn' as the response to the question in the [Ask the user to type something in](#ask-the-user-to-type-something-in) example above.

#### Skip a question or several
`GOTO:question-code`

This is only available in a `If they choose response x` cell. It directs the system to show the question identified by the question-code next. Any questions in between will be skipped unless you do a complicated set of GOTOs and give yourself a big headache. Note that the question-code must be a value that exists in a cell in the [Question Code](#question-code) column.


# What happens next?
After you have updated your version of the spreadsheet you need to email it to the online self-assessment tool admin at **EMAIL ADDRESS HERE**.
The admin will process the spreadsheet and generate the online conversation and a flowchart for the conversation.


