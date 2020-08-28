# googleBot
This is a google bot, i used selenium webdriver in python 3.7.

This is a google search bot, it will search the arguments who you write, and will find the interest link.

Before you use that, install this modules:
```
pip install selenium
pip install webdriver_manager
```

## Instance Attributes

### set a variable for GoogleSearchBot(interestLink, searchListArgs, maxPage=10(default)) class

### interestLink (string)
 Here you will write your interest link who the bot will find at the links in the page

### searchListArgs (list)
 Here you will write a list with the arguments who the will search in google page

### maxPage (int)
 Here you will set the maximum of pages who the bot will search in the interest link on the page for each argument in searchListArgs (10 as default) 

## METHODS
### options(interestLink_, searchListArgs, maxPages)
 Set the Attributes values

### get_list_search_args_size()
#### it will return the size of searchListArgs

### _check_next_exists()
 it will check and return true or false if the element next page exists on the page

### _next_page()
 it will click on the next page button

### execute()
 it will execute the bot

# P.S. GOOGLE WILL SUSPECT YOU ARE BOT :(
