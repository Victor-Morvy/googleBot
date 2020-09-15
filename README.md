# googleBot page finder bot
Este é um page finder de interesse utilizando argumentos de pesquisa no google, feito para estudos

Módulos utilizados:
```
pip install selenium
pip install webdriver_manager
```
### set a object for GoogleSearchBot() class, code example:
```
import lib.googleBot as GoogleBot

roBot = GoogleBot.GoogleSearchBot("facebook.com", [
        "couzine group",
        "game groups",
        "old viodegames marketplace",
        "games couzine",
        "python groups",
        "c# groups",
        "c groups"
        "algorithms groups"
    ])
    
roBot.execute()
```

## Instance Attributes

### interestLink (string)
```Here you will write your interest link who the bot will find at the links in the page```

### searchListArgs (list)
```Here you will write a list with the arguments who the will search in google page```

### maxPage (int)
```Here you will set the maximum of pages who the bot will search in the interest link on the page for each argument in searchListArgs (10 as default) ```

## METHODS
### options(interestLink_, searchListArgs, maxPages)
```Set the Attributes values```

### get_list_search_args_size()
```it will return the size of searchListArgs```

### _check_next_exists()
```it will check and return true or false if the element next page exists on the page```

### _next_page()
```it will click on the next page button```

### execute()
```it will execute the bot```

# P.S.: Google will know it's a bot
