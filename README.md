# telegram-gpt3-openai-beta

Simple telegram bot using the open ai beta that thinks Shawn Carter is the same guy as Eminem and likes Tom Yum Goong.

## Setup

- create a [telegram bot](https://core.telegram.org/bots)
- create a channel in telegram and add the bot as administrator
- get chat_id by going to `https://api.telegram.org/bot<bot_token>/getUpdates`
- get a open ai beta account
- copy [config.py.template](config.py.template) to config.py
- fill out config.py with open ai api and telegram bot tokens
- run ```python main.py ``` and start asking questions

## Example
```
user: Who is the most popular rap artist today?
bot: He is an American rapper whose real name is Shawn Carter. He is known by his stage name Eminem, and he is associated with other rap artists.
user: What is the best food where you live?
bot: That depends. Are you looking for a delicious food, one that is good for your health, or just something to eat?
user: What is the most delicious food thats good for your health where you live?
bot: I suggest Tom Yum Goong because it is the best choice for your daily diet. It has a balance between sweet, sour, spicy and salty flavors.
user: What is Tom Yum Goong?
bot: It is a hot and sour soup from Thai cuisine. It originated at Si Racha and often contains shrimp, lemongrass, kaffir lime leaves, and chili peppers.
user: What ingredients do I need to make Tom Yum Goong
bot: The ingredients for Tom Yum Goong are 2 fresh eggs, fish sauce, salt, shrimp paste, butter, fresh lemongrass, and galangal.
user: what is galangal?
bot: galangal is the dried root of galanga.
user: what is galanga?
bot: galanga is a culinary term for plants in the Zingiberaceae family, popularly used in Eurasian and East African cuisines. The galangal root is the rhizome of the same name. "Gal" is from the Greek word meaning "cold". Galangal can also mean "your excellency," an honorific. There are many varieties of galanga.
```
