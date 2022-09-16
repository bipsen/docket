# docket

Maintain queue's of eg. webscraping jobs via airtable. 

## How to use

Set up at database and a table using the correct format.

Set the two following enviromental variables ([learn how to set env variables](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html)):

* `AIRTABLE_API_KEY` [How do I get my api key?](https://support.airtable.com/docs/how-do-i-get-my-api-key-)
* `AIRTABLE_WEBSCRAPING_BASE_ID` [How do I get my Base ID?](https://support.airtable.com/docs/understanding-airtable-ids)

### Example

    from docket import Docket
    import my_scraping_library

    d = Docket("name_of_my_table")
    for target in d.get_jobs():
        my_scraping_library.scrape(target)
