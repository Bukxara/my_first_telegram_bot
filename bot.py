import logging
from config import API_TOKEN, admin

from aiogram import Bot, Dispatcher, executor, types
from sq_cls import Database
from buttons import *

#TOKEN AND ADMIN FILES ARE LOCATED IN config.py FILE


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db = Database()
db.create()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    tg_id = message.from_user.id
    username = message.from_user.username
    data = db.select(tg_id)
    if data is None:
        await message.reply("Welcome to just different bot!\nPlease, share your phone number!", 
            reply_markup = contact)
        db.insert(tg_id, username)
    else:
        await message.answer("Hi there!", reply_markup = menu)


@dp.message_handler(content_types='contact')
async def echo(message: types.Message):
    """requests for contact"""
    tg_id = message.from_user.id
    ph_num = message.contact.phone_number
    db.update_contact(tg_id, ph_num)
    await message.answer("Thank you for sharing\nNow we would like you to share your location :)", 
        reply_markup = location)


@dp.message_handler(content_types='location')
async def echo(message: types.Message):
    """requests for location"""
    tg_id = message.from_user.id
    location = (message.location.latitude, message.location.longitude)
    db.update_location(tg_id, location)
    await message.answer("You've successfully signed up to our bot!", reply_markup = menu)


@dp.message_handler(text = "Order 🍽")
async def echo(message: types.Message):
    """Main Menu"""
    await message.answer("Here is our menu:", reply_markup = order)
    

@dp.callback_query_handler(text = "lavash")
async def order_lavash(call: types.CallbackQuery):
    """Menu for Lavash"""
    await call.message.answer_photo(
        photo = open("images/lavash_menu.jpg", "rb"),
        caption = "Here is our lavash🌯🌯 menu:", reply_markup = lavash)

@dp.callback_query_handler(text = "back1")
async def order_lavash(call: types.CallbackQuery):
    """Backs from menu Lavash to Main Menu"""
    await call.message.answer("Here is our menu:", reply_markup = order)


@dp.callback_query_handler(text = "beef_lavash")
async def order_lavash(call: types.CallbackQuery):
    """Asks a user about the size of the beef_lavash only"""
    await call.message.answer("What size do you want?", reply_markup = beef_lavash_size)


@dp.callback_query_handler(text = "beef_lavash_mini")
async def order_lavash(call: types.CallbackQuery):
    """Ordering beef lavash mini"""
    await call.message.answer_photo(
        photo = open("images/beef_lavash.jpg", "rb"),
        caption = """Price 18 000
Ingredients: Beef, fries, tomato, cucumber, sauce, mayonnaise
How many?""", reply_markup = beef_lavash_quantity)


@dp.callback_query_handler(text = "beef_lavash_classic")
async def order_lavash(call: types.CallbackQuery):
    """Ordering beef lavash classic"""
    await call.message.answer_photo(
        photo = open("images/beef_lavash.jpg", "rb"),
        caption = """Price 20 000
Ingredients: Beef, fries, tomato, cucumber, sauce, mayonnaise
How many?""", reply_markup = beef_lavash_quantity)


@dp.callback_query_handler(text = "beef:from_quantity_to_size_menu")
async def order_lavash(call: types.CallbackQuery):
    """Backs from Beef Lavash Quantity Menu to Lavash Size Menu"""
    await call.message.answer("What size do you want?", reply_markup = beef_lavash_size)


@dp.callback_query_handler(text = "chicken_lavash")
async def order_lavash(call: types.CallbackQuery):
    """Asks a user about the size of the chicken lavash only"""
    await call.message.answer("What size do you want?", reply_markup = chicken_lavash_size)


@dp.callback_query_handler(text = "chicken_lavash_mini")
async def order_lavash(call: types.CallbackQuery):
    """Ordering chicken lavash mini"""
    await call.message.answer_photo(
        photo = open("images/chicken_lavash.jpg", "rb"),
        caption = """Price 18 000
Ingredients: Chicken, fries, tomato, cucumber, sauce, mayonnaise
How many?""", reply_markup = chicken_lavash_quantity)


@dp.callback_query_handler(text = "chicken_lavash_classic")
async def order_lavash(call: types.CallbackQuery):
    """Ordering chicken lavash classic"""
    await call.message.answer_photo(
        photo = open("images/chicken_lavash.jpg", "rb"),
        caption = """Price 20 000
Ingredients: Chicken, fries, tomato, cucumber, sauce, mayonnaise
How many?""", reply_markup = chicken_lavash_quantity)   


@dp.callback_query_handler(text = "chicken:from_quantity_to_size_menu")
async def order_lavash(call: types.CallbackQuery):
    """Backs from Chicken Lavash Quantity Menu to Lavash Size Menu"""
    await call.message.answer("What size do you want?", reply_markup = chicken_lavash_size)


@dp.callback_query_handler(text = "spicy_beef_lavash")
async def order_lavash(call: types.CallbackQuery):
    """Asks a user about the size of the spicy beef lavash only"""
    await call.message.answer("What size do you want?", reply_markup = spicy_beef_lavash_size)


@dp.callback_query_handler(text = "spicy_beef_lavash_mini")
async def order_lavash(call: types.CallbackQuery):
    """Ordering spicy beef lavash mini"""
    await call.message.answer_photo(
        photo = open("images/spicy_beef_lavash.jpg", "rb"),
        caption = """Price 18 000
Ingredients: Chili pepper, Beef, fries, tomato, cucumber, sauce, mayonnaise
How many?""", reply_markup = spicy_beef_lavash_quantity)


@dp.callback_query_handler(text = "spicy_beef_lavash_classic")
async def order_lavash(call: types.CallbackQuery):
    """Ordering spicy beef lavash classic"""
    await call.message.answer_photo(
        photo = open("images/spicy_beef_lavash.jpg", "rb"),
        caption = """Price 20 000
Ingredients: Chili pepper, Beef, fries, tomato, cucumber, sauce, mayonnaise
How many?""", reply_markup = spicy_beef_lavash_quantity)   


@dp.callback_query_handler(text = "spicy_beef:from_quantity_to_size_menu")
async def order_lavash(call: types.CallbackQuery):
    """Backs from Spicy Beef Lavash Quantity Menu to Lavash Size Menu"""
    await call.message.answer("What size do you want?", reply_markup = spicy_beef_lavash_size)


@dp.callback_query_handler(text = "spicy_chicken_lavash")
async def order_lavash(call: types.CallbackQuery):
    """Asks a user about the size of the spicy chicken lavash only"""
    await call.message.answer("What size do you want?", reply_markup = spicy_chicken_lavash_size)


@dp.callback_query_handler(text = "spicy_chicken_lavash_mini")
async def order_lavash(call: types.CallbackQuery):
    """Ordering spicy chicken lavash mini"""
    await call.message.answer_photo(
        photo = open("images/spicy_chicken_lavash.jpg", "rb"),
        caption = """Price 18 000
Ingredients: Chili pepper, Chicken, fries, tomato, cucumber, sauce, mayonnaise
How many?""", reply_markup = spicy_chicken_lavash_quantity)


@dp.callback_query_handler(text = "spicy_chicken_lavash_classic")
async def order_lavash(call: types.CallbackQuery):
    """Ordering spicy chicken lavash classic"""
    await call.message.answer_photo(
        photo = open("images/spicy_chicken_lavash.jpg", "rb"),
        caption = """Price 20 000
Ingredients: Chili pepper, Chicken, fries, tomato, cucumber, sauce, mayonnaise
How many?""", reply_markup = spicy_chicken_lavash_quantity)   


@dp.callback_query_handler(text = "spicy_chicken:from_quantity_to_size_menu")
async def order_lavash(call: types.CallbackQuery):
    """Backs from Spicy Chicken Lavash Quantity Menu to Lavash Size Menu"""
    await call.message.answer("What size do you want?", reply_markup = spicy_chicken_lavash_size)


@dp.callback_query_handler(text = "cheesy_beef_lavash")
async def order_lavash(call: types.CallbackQuery):
    """Asks a user about the size of the cheesy beef lavash only"""
    await call.message.answer("What size do you want?", reply_markup = cheesy_beef_lavash_size)


@dp.callback_query_handler(text = "cheesy_beef_lavash_mini")
async def order_lavash(call: types.CallbackQuery):
    """Ordering cheesy beef lavash mini"""
    await call.message.answer_photo(
        photo = open("images/cheesy_beef_lavash.jpg", "rb"),
        caption = """Price 18 000
Ingredients: Cheese, Beef, fries, tomato, cucumber, sauce, mayonnaise
How many?""", reply_markup = cheesy_beef_lavash_quantity)


@dp.callback_query_handler(text = "cheesy_beef_lavash_classic")
async def order_lavash(call: types.CallbackQuery):
    """Ordering cheesy beef lavash classic"""
    await call.message.answer_photo(
        photo = open("images/cheesy_beef_lavash.jpg", "rb"),
        caption = """Price 20 000
Ingredients: Cheese, Beef, fries, tomato, cucumber, sauce, mayonnaise
How many?""", reply_markup = cheesy_beef_lavash_quantity)  


@dp.callback_query_handler(text = "cheesy_beef:from_quantity_to_size_menu")
async def order_lavash(call: types.CallbackQuery):
    """Backs from Cheesy Beef Lavash Quantity Menu to Lavash Size Menu"""
    await call.message.answer("What size do you want?", reply_markup = cheesy_beef_lavash_size)


@dp.callback_query_handler(text = "cheesy_chicken_lavash")
async def order_lavash(call: types.CallbackQuery):
    """Asks a user about the size of the cheesy chicken lavash only"""
    await call.message.answer("What size do you want?", reply_markup = cheesy_chicken_lavash_size)


@dp.callback_query_handler(text = "cheesy_chicken_lavash_mini")
async def order_lavash(call: types.CallbackQuery):
    """Ordering cheesy chicken lavash mini"""
    await call.message.answer_photo(
        photo = open("images/cheesy_chicken_lavash.jpg", "rb"),
        caption = """Price 18 000
Ingredients: Cheese, Chicken, fries, tomato, cucumber, sauce, mayonnaise
How many?""", reply_markup = cheesy_chicken_lavash_quantity)


@dp.callback_query_handler(text = "cheesy_chicken_lavash_classic")
async def order_lavash(call: types.CallbackQuery):
    """Ordering cheesy chicken lavash classic"""
    await call.message.answer_photo(
        photo = open("images/cheesy_chicken_lavash.jpg", "rb"),
        caption = """Price 20 000
Ingredients: Cheese, Chicken, fries, tomato, cucumber, sauce, mayonnaise
How many?""", reply_markup = cheesy_chicken_lavash_quantity) 


@dp.callback_query_handler(text = "cheesy_chicken:from_quantity_to_size_menu")
async def order_lavash(call: types.CallbackQuery):
    """Backs from Cheesy Chicken Lavash Quantity Menu to Lavash Size Menu"""
    await call.message.answer("What size do you want?", reply_markup = cheesy_chicken_lavash_size)


@dp.callback_query_handler(text = "from_size_to_lavash_menu")
async def order_lavash(call: types.CallbackQuery):
    """Backs from menu Lavash Size Menu to Lavash Menu"""
    await call.message.answer_photo(
        photo = open("images/lavash_menu.jpg", "rb"),
        caption = "Here is our lavash🌯🌯 menu:", reply_markup = lavash)


@dp.callback_query_handler(text = "fitter")
async def order_fitter(call: types.CallbackQuery):
    """Quantity of fitter to order"""
    await call.message.answer_photo(
        photo = open("images/fitter.jpg", "rb"),
        caption = """Price is 18 000.
Ingredients: Chilli pepper, Beef, iceberg, fries, tomato, cucumber, sauce, mayonnaise 
How many?""", reply_markup = fitter_quantity)


@dp.callback_query_handler(text = "from_quantity_to_lavash_menu")
async def order_lavash(call: types.CallbackQuery):
    """Backs from menu Order Quantity Fitter Menu to Lavash Menu"""
    await call.message.answer_photo(
        photo = open("images/lavash_menu.jpg", "rb"),
        caption = "Here is our lavash🌯🌯 menu:", reply_markup = lavash)
#THE END OF LAVASH MENU       THE END OF LAVASH MENU         THE END OF LAVASH MENU     THE END OF LAVASH MENU


@dp.callback_query_handler(text = "hot_dog")
async def order_hot_dog(call: types.CallbackQuery):
    """Menu for Hot-Dog"""
    await call.message.answer("Here is our 🌭Hot-Dog🌭 menu:", reply_markup = hot_dog)


@dp.callback_query_handler(text = "hot-dog-baget-double")
async def order_hot_dog(call: types.CallbackQuery):
    """Menu for Hot-Dog Baget Double quantity"""
    await call.message.answer_photo(
        photo = open("images/hot_dog_baget_double.jpg", "rb"),
        caption = """Price is 18 000.
Ingredients: 2x sausage, ketch-up, cheese, tomato 
How many?""", reply_markup = hot_dog_quantity)


@dp.callback_query_handler(text = "classic-hot-dog")
async def order_hot_dog(call: types.CallbackQuery):
    """Menu for Classic Hot-Dog quantity"""
    await call.message.answer_photo(
        photo = open("images/classic_hotdog.jpg", "rb"),
        caption = """Price is 8 000.
Ingredients: Sausage, ketch-up, tomato 
How many?""", reply_markup = hot_dog_quantity)


@dp.callback_query_handler(text = "royal-hot-dog")
async def order_hot_dog(call: types.CallbackQuery):
    """Menu for Royal Hot-Dog quantity"""
    await call.message.answer_photo(
        photo = open("images/royal_hotdog.jpg", "rb"),
        caption = """Price is 15 000.
Ingredients: 2x sausage, ketch-up, cheese, tomato, cucumber 
How many?""", reply_markup = hot_dog_quantity)


@dp.callback_query_handler(text = "chicken-hot-dog")
async def order_hot_dog(call: types.CallbackQuery):
    """Menu for Chicken Hot-Dog quantity"""
    await call.message.answer_photo(
        photo = open("images/chicken_hotdog.jpg", "rb"),
        caption = """Price is 17 000.
Ingredients: Sausage, ketch-up, Chicken, tomato 
How many?""", reply_markup = hot_dog_quantity)


@dp.callback_query_handler(text = "from_quantity_to_hot_dog_menu")
async def order_hot_dog(call: types.CallbackQuery):
    """Backs from menu Hot-Dog quantity menu to Hot-Dog Menu"""
    await call.message.answer("Here is our 🌭Hot-Dog🌭 menu:", reply_markup = hot_dog)
#THE END OF LAVASH MENU     THE END OF LAVASH MENU      THE END OF LAVASH MENU      THE END OF LAVASH MENU

@dp.callback_query_handler(text = "sandwich_club")
async def order_sandwich(call: types.CallbackQuery):
    """Menu for Sandwich Club"""
    await call.message.answer("Here is our Sandwich🥪🥪 menu:", reply_markup = sandwich)


@dp.callback_query_handler(text = "classic-sandwich")
async def order_sandwich(call: types.CallbackQuery):
    """Menu for Both Sandwich-Club quantity"""
    await call.message.answer_photo(
        photo = open("images/classic_sandwich.jpg", "rb"),
        caption = """Price is 22 000. 
Ingredients: Beef, tomato, sauce, fries
How many?""", reply_markup = sanwich_club_quantity)


@dp.callback_query_handler(text = "chicken-sandwich")
async def order_sandwich(call: types.CallbackQuery):
    """Menu for Both Sandwich-Club quantity"""
    await call.message.answer_photo(
        photo = open("images/chicken_sandwich.jpg", "rb"),
        caption = """Price is 22 000. 
Ingredients: Chicken, tomato, sauce, fries
How many?""", reply_markup = sanwich_club_quantity)


@dp.callback_query_handler(text = "from_quantity_to_sandwich_menu")
async def order_sandwich(call: types.CallbackQuery):
    """Backs from menu Sandwich-Club quantity menu to Sandwich-Club Menu"""
    await call.message.answer("Here is our Sandwich🥪🥪 menu:", reply_markup = sandwich)
#THE END OF SANDWICH MENU       THE END OF SANDWICH MENU        THE END OF SANDWICH MENU        


@dp.callback_query_handler(text = "shaurma")
async def order_shaurma(call: types.CallbackQuery):
    """Menu for Shaurma"""
    await call.message.answer_photo(
        photo = open("images/shaurma_menu.jpg", "rb"),
        caption = "Here is our Shaurma🌮🌮 menu:", reply_markup = shaurma)


@dp.callback_query_handler(text = "beef_shaurma")
async def order_shaurma(call: types.CallbackQuery):
    """Asks a user about the size of the Beef shaurma only"""
    await call.message.answer_photo(
        photo = open("images/beef_shaurma.jpg", "rb"),
        caption = "What size do you want?", reply_markup = beef_shaurma_size)


@dp.callback_query_handler(text = "beef_shaurma_mini")
async def order_shaurma(call: types.CallbackQuery):
    """Asks a user about the size of the Beef shaurma Mini"""
    await call.message.answer_photo(
        photo = open("images/beef_shaurma.jpg", "rb"),
        caption = """Price 18 000.
Ingredients: Beef, Tomato, Sauce, Onion
How many?""", reply_markup = beef_shaurma_quantity)


@dp.callback_query_handler(text = "beef_shaurma_classic")
async def order_shaurma(call: types.CallbackQuery):
    """Asks a user about the size of the Beef shaurma Classic"""
    await call.message.answer_photo(
        photo = open("images/beef_shaurma.jpg", "rb"),
        caption = """Price 20 000.
Ingredients: Beef, Tomato, Sauce, Onion
How many?""", reply_markup = beef_shaurma_quantity)


@dp.callback_query_handler(text = "beef_shaurma:from_quantity_to_size_menu")
async def shaurma_menu(call: types.CallbackQuery):
    """Returns from Quantity to Shaurma menu"""
    await call.message.answer_photo(
        photo = open("images/beef_shaurma.jpg", "rb"),
        caption = "What size do you want?", reply_markup = beef_shaurma_size)


@dp.callback_query_handler(text = "chicken_shaurma")
async def order_shaurma(call: types.CallbackQuery):
    """Asks a user about the size of the Beef shaurma only"""
    await call.message.answer_photo(
        photo = open("images/chicken_shaurma.jpg", "rb"),
        caption = "What size do you want?", reply_markup = chicken_shaurma_size)


@dp.callback_query_handler(text = "chicken_shaurma_mini")
async def order_shaurma(call: types.CallbackQuery):
    """Asks a user about the size of the Chicken shaurma Mini"""
    await call.message.answer_photo(
        photo = open("images/chicken_shaurma.jpg", "rb"),
        caption = """Price 18 000.
Ingredients: Chicken, Tomato, Sauce, Onion
How many?""", reply_markup = chicken_shaurma_quantity)


@dp.callback_query_handler(text = "chicken_shaurma_classic")
async def order_shaurma(call: types.CallbackQuery):
    """Asks a user about the size of the Chicken shaurma Classic"""
    await call.message.answer_photo(
        photo = open("images/chicken_shaurma.jpg", "rb"),
        caption = """Price 20 000.
Ingredients: Chicken, Tomato, Sauce, Onion
How many?""", reply_markup = chicken_shaurma_quantity)


@dp.callback_query_handler(text = "chicken_shaurma:from_quantity_to_size_menu")
async def shaurma_menu(call: types.CallbackQuery):
    """Returns from Quantity to Shaurma menu"""
    await call.message.answer_photo(
        photo = open("images/chicken_shaurma.jpg", "rb"),
        caption = "What size do you want?", reply_markup = chicken_shaurma_size)


@dp.callback_query_handler(text = "spicy_beef_shaurma")
async def order_shaurma(call: types.CallbackQuery):
    """Asks a user about the size of the Beef shaurma only"""
    await call.message.answer_photo(
        photo = open("images/spicy_beef_shaurma.jpg", "rb"),
        caption = "What size do you want?", reply_markup = spicy_beef_shaurma_size)


@dp.callback_query_handler(text = "spicy_beef_shaurma_mini")
async def order_shaurma(call: types.CallbackQuery):
    """Asks a user about the size of the Beef shaurma Mini"""
    await call.message.answer_photo(
        photo = open("images/spicy_beef_shaurma.jpg", "rb"),
        caption = """Price 18 000.
Ingredients: Chili pepper, Beef, Tomato, Sauce, Onion
How many?""", reply_markup = spicy_beef_shaurma_quantity)


@dp.callback_query_handler(text = "spicy_beef_shaurma_classic")
async def order_shaurma(call: types.CallbackQuery):
    """Asks a user about the size of the Beef shaurma Classic"""
    await call.message.answer_photo(
        photo = open("images/spicy_beef_shaurma.jpg", "rb"),
        caption = """Price 20 000.
Ingredients: Chili pepper, Beef, Tomato, Sauce, Onion
How many?""", reply_markup = spicy_beef_shaurma_quantity)


@dp.callback_query_handler(text = "spicy_beef_shaurma:from_quantity_to_size_menu")
async def shaurma_menu(call: types.CallbackQuery):
    """Returns from Quantity to Shaurma menu"""
    await call.message.answer_photo(
        photo = open("images/spicy_beef_shaurma.jpg", "rb"),
        caption = "What size do you want?", reply_markup = spicy_beef_shaurma_size)


@dp.callback_query_handler(text = "spicy_chicken_shaurma")
async def order_shaurma(call: types.CallbackQuery):
    """Asks a user about the size of the Beef shaurma only"""
    await call.message.answer_photo(
        photo = open("images/spicy_chicken_shaurma.jpg", "rb"),
        caption = "What size do you want?", reply_markup = spicy_chicken_shaurma_size)


@dp.callback_query_handler(text = "spicy_chicken_shaurma_mini")
async def order_shaurma(call: types.CallbackQuery):
    """Asks a user about the size of the Chicken shaurma Mini"""
    await call.message.answer_photo(
        photo = open("images/spicy_chicken_shaurma.jpg", "rb"),
        caption = """Price 18 000.
Ingredients: Chicken, Tomato, Sauce, Onion
How many?""", reply_markup = spicy_chicken_shaurma_quantity)


@dp.callback_query_handler(text = "spicy_chicken_shaurma_classic")
async def order_shaurma(call: types.CallbackQuery):
    """Asks a user about the size of the Chicken shaurma Classic"""
    await call.message.answer_photo(
        photo = open("images/spicy_chicken_shaurma.jpg", "rb"),
        caption = """Price 20 000.
Ingredients: Chicken, Tomato, Sauce, Onion
How many?""", reply_markup = spicy_chicken_shaurma_quantity)


@dp.callback_query_handler(text = "spicy_chicken_shaurma:from_quantity_to_size_menu")
async def shaurma_menu(call: types.CallbackQuery):
    """Returns from Quantity to Shaurma menu"""
    await call.message.answer_photo(
        photo = open("images/spicy_chicken_shaurma.jpg", "rb"),
        caption = "What size do you want?", reply_markup = spicy_chicken_shaurma_size)


@dp.callback_query_handler(text = "from_size_to_shaurma_menu")
async def shaurma_menu(call: types.CallbackQuery):
    """Returns from size to shaurma menu"""
    await call.message.answer_photo(
        photo = open("images/shaurma_menu.jpg", "rb"),
        caption = "Here is our Shaurma🌮🌮 menu:", reply_markup = shaurma)

#THE END OF SHAURMA MENU    #THE END OF SHAURMA MENU    #THE END OF SHAURMA MENU    #THE END OF SHAURMA MENU


@dp.callback_query_handler(text = "burger")
async def burger_menu(call: types.CallbackQuery):
    """Menu for Burgers"""
    await call.message.answer("Here is our 🍔Burger🍔 menu:", reply_markup = burger)


@dp.callback_query_handler(text = "hamburger")
async def order_hamburger(call: types.CallbackQuery):
    """Menu for Hamburger Quantity"""
    await call.message.answer_photo(
        photo = open("images/hamburger.jpg", "rb"),
        caption = """Price is 20 000. 
How many?""", reply_markup = burger_quantity)


@dp.callback_query_handler(text = "cheeseburger")
async def order_cheeseburger(call: types.CallbackQuery):
    """Menu for Cheeseburger Quantity"""
    await call.message.answer_photo(
        photo = open("images/cheeseburger.jpg", "rb"),
        caption = """Price is 22 000. 
How many?""", reply_markup = burger_quantity)


@dp.callback_query_handler(text = "from_quantity_to_burger_menu")
async def burger_menu(call: types.CallbackQuery):
    """Returns from Burger quantity to Burger Menu"""
    await call.message.answer("Here is our 🍔Burger🍔 menu:", reply_markup = burger)
#THE END OF BURGER MENU     THE END OF BURGER MENU     THE END OF BURGER MENU     THE END OF BURGER MENU


@dp.callback_query_handler(text = "donar")
async def order_donar(call: types.CallbackQuery):
    """Menu for Donar"""
    await call.message.answer_photo(
        photo = open("images/donar_menu.jpg", "rb"),
        caption = "Here is our 🍱Donar🍱 menu:", reply_markup = donar)


@dp.callback_query_handler(text = "beef_donar")
async def order_donar(call: types.CallbackQuery):
    """Menu for Beef Donar Quantity"""
    await call.message.answer_photo(
        photo = open("images/donar.jpg", "rb"),
        caption = """Price is 23 000.
How many?""", reply_markup = donar_quantity)


@dp.callback_query_handler(text = "chicken_donar")
async def order_donar(call: types.CallbackQuery):
    """Menu for Chicken Donar Quantity"""
    await call.message.answer_photo(
        photo = open("images/donar.jpg", "rb"),
        caption = """Price is 23 000.
How many?""", reply_markup = donar_quantity)


@dp.callback_query_handler(text = "from_quantity_to_donar_menu")
async def donar_menu(call: types.CallbackQuery):
    """Returns from Donar quantity to Donar Menu"""
    await call.message.answer_photo(
        photo = open("images/donar_menu.jpg", "rb"),
        caption = "Here is our 🍱Donar🍱 menu:", reply_markup = donar)
#THE END OF DONAR MENU      THE END OF DONAR MENU       THE END OF DONAR MENU       THE END OF DONAR MENU


@dp.callback_query_handler(text = "fries")
async def fries_menu(call: types.CallbackQuery):
    """Menu for Fries"""
    await call.message.answer("Here is our 🍟Fries🍟 menu:", reply_markup = fries)


@dp.callback_query_handler(text = "15gr_fries")
async def order_fries(call: types.CallbackQuery):
    """Menu for 15gr Fries """
    await call.message.answer_photo(
        photo = open("images/15gr_fri.jpg", "rb"),
        caption = "Price is 6 000. How many?", reply_markup = fries_quantity)


@dp.callback_query_handler(text = "rustic_potatoes")
async def order_fries(call: types.CallbackQuery):
    """Menu for Rustic Potatoes"""
    await call.message.answer_photo(
        photo = open("images/rustic_potatoes.jpg", "rb"),
        caption = "Price is 6 000. How many?", reply_markup = fries_quantity)


@dp.callback_query_handler(text = "small_rice")
async def order_fries(call: types.CallbackQuery):
    """Menu for Large Rice"""
    await call.message.answer_photo(
        photo = open("images/large_rice.jpg", "rb"),
        caption = "Price is 4 000. How many?", reply_markup = fries_quantity)


@dp.callback_query_handler(text = "large_rice")
async def order_fries(call: types.CallbackQuery):
    """Menu for Large Rice"""
    await call.message.answer_photo(
        photo = open("images/large_rice.jpg", "rb"),
        caption = "Price is 8 000. How many?", reply_markup = fries_quantity)


@dp.callback_query_handler(text = "from_quantity_to_fries_menu")
async def fries_menu(call: types.CallbackQuery):
    """Returns from Fries quantity to Fries Menu"""
    await call.message.answer("Here is our 🍟Fries🍟 menu:", reply_markup = fries)
#THE END OF FRIES MENU      THE END OF FRIES MENU       THE END OF FRIES MENU       THE END OF FRIES MENU


@dp.callback_query_handler(text = "drinks")
async def drinks_menu(call: types.CallbackQuery):
    """Menu for Drinks"""
    await call.message.answer("Here is our 🥤Drinks🥤 menu:", reply_markup = drinks)


@dp.callback_query_handler(text = "tea-and-coffee")
async def coffee_tea_menu(call: types.CallbackQuery):
    """Menu for Coffee and Tea"""
    await call.message.answer("Here is our Coffee and Tea menu:", reply_markup = cof_tea)


@dp.callback_query_handler(text = "from_coffee_to_drinks")
async def drinks_menu(call: types.CallbackQuery):
    """Returns from Coffee and Tea Menu to Drinks Menu"""
    await call.message.answer("Here is our 🥤Drinks🥤 menu:", reply_markup = drinks)    


@dp.callback_query_handler(text = "coffee")
async def coffee_menu(call: types.CallbackQuery):
    """Menu for Coffee itself"""
    await call.message.answer("Here is our Coffee menu:", reply_markup = coffees)


@dp.callback_query_handler(text = "from-coffees-to-cofee-and-tea")
async def coffee_tea_menu(call: types.CallbackQuery):
    """Retruns from menu Coffee to Coffee and Tea"""
    await call.message.answer("Here is our Coffee and Tea menu:", reply_markup = cof_tea)


@dp.callback_query_handler(text = "americano")
async def order_americano(call: types.CallbackQuery):
    """Menu for Coffee Americano"""
    await call.message.answer_photo(
        photo = open("images/americano.jpg", "rb"),
        caption = "Price is 12 000. How many?", reply_markup = coffee_quantity)


@dp.callback_query_handler(text = "capuccino")
async def order_capuccino(call: types.CallbackQuery):
    """Menu for Coffee Capuccino"""
    await call.message.answer_photo(
        photo = open("images/capuccino.jpg", "rb"),
        caption = "Price is 18 000. How many?", reply_markup = coffee_quantity)


@dp.callback_query_handler(text = "coffe_3v1")
async def order_3v1(call: types.CallbackQuery):
    """Menu for Coffee 3v1"""
    await call.message.answer_photo(
        photo = open("images/3v1.jpg", "rb"),
        caption = "Price is 5 000. How many?", reply_markup = coffee_quantity)


@dp.callback_query_handler(text = "latte")
async def order_latte(call: types.CallbackQuery):
    """Menu for Coffee Latte"""
    await call.message.answer_photo(
        photo = open("images/latte.jpg", "rb"),
        caption = "Price is 15 000. How many?", reply_markup = coffee_quantity)


@dp.callback_query_handler(text = "from_quantity_to_coffee_menu")
async def coffee_menu(call: types.CallbackQuery):
    """Menu for Coffee itself"""
    await call.message.answer("Here is our Coffee menu:", reply_markup = coffees)
#coffe menusi tugadi

@dp.callback_query_handler(text = "tea")
async def tea_menu(call: types.CallbackQuery):
    """Menu for Tea itself"""
    await call.message.answer("Here is our Tea menu:", reply_markup = teas)


@dp.callback_query_handler(text = "from-teas-to-cofee-and-tea")
async def coffee_tea_menu(call: types.CallbackQuery):
    """Retruns from menu Tea to Coffee and Tea"""
    await call.message.answer("Here is our Coffee and Tea menu:", reply_markup = cof_tea)


@dp.callback_query_handler(text = "green_tea")
async def order_tea(call: types.CallbackQuery):
    """Menu for Black and Green Tea"""
    await call.message.answer_photo(
        photo = open("images/green_tea.jpg", "rb"),
        caption = "Price is 3 000. How many?", reply_markup = tea_quantity)


@dp.callback_query_handler(text = "black_tea")
async def order_tea(call: types.CallbackQuery):
    """Menu for Black and Green Tea"""
    await call.message.answer_photo(
        photo = open("images/black_tea.jpg", "rb"),
        caption = "Price is 3 000. How many?", reply_markup = tea_quantity)


@dp.callback_query_handler(text = "lemon_tea")
async def order_lemon_tea(call: types.CallbackQuery):
    """Menu for Lemon Tea"""
    await call.message.answer_photo(
        photo = open("images/lemon_tea.jpg", "rb"),
        caption = "Price is 5 000. How many?", reply_markup = tea_quantity)


@dp.callback_query_handler(text = "from_quantity_to_tea_menu")
async def tea_menu(call: types.CallbackQuery):
    """Menu for Tea itself"""
    await call.message.answer("Here is our Tea menu:", reply_markup = teas)
#THE END OF TEA&COFFEE MENU     THE END OF TEA&COFFEE MENU      THE END OF TEA&COFFEE MENU

@dp.callback_query_handler(text = "cold-drinks")
async def cold_drinks_menu(call: types.CallbackQuery):
    """Menu for Cold Drinks itself"""
    await call.message.answer("Here is our Cold Drinks menu:", reply_markup = cold_drinks)


@dp.callback_query_handler(text = "from-cold-drinks-to-drinks")
async def drinks_menu(call: types.CallbackQuery):
    """Retruns from Cold Drinks Menu Drinks Menu"""
    await call.message.answer("Here is our 🥤Drinks🥤 menu:", reply_markup = drinks)


@dp.callback_query_handler(text = "coca-cola")
async def order_lemon_tea(call: types.CallbackQuery):
    """Ordering Cola"""
    await call.message.answer_photo(
        photo = open("images/cola.jpg", "rb"),
        caption = "Price is 11 000. How many?", reply_markup = cold_drinks_quantity)


@dp.callback_query_handler(text = "sprite")
async def order_lemon_tea(call: types.CallbackQuery):
    """Ordering Sprite"""
    await call.message.answer_photo(
        photo = open("images/sprite.jpg", "rb"),
        caption = "Price is 11 000. How many?", reply_markup = cold_drinks_quantity)


@dp.callback_query_handler(text = "fanta")
async def order_lemon_tea(call: types.CallbackQuery):
    """Ordering Fanta"""    
    await call.message.answer_photo(
        photo = open("images/fanta.jpg", "rb"),
        caption = "Price is 11 000. How many?", reply_markup = cold_drinks_quantity)


@dp.callback_query_handler(text = "from_quantity_to_cold_drinks_menu")
async def cold_drinks_menu(call: types.CallbackQuery):
    """Menu for Cold Drinks itself"""
    await call.message.answer("Here is our Cold Drinks menu:", reply_markup = cold_drinks)


@dp.callback_query_handler(text = "nestle")
async def order_nestle(call: types.CallbackQuery):
    """Ordering Nestle"""
    await call.message.answer_photo(
        photo = open("images/nestle.jpg", "rb"),
        caption = "Price is 4 000. How many?", reply_markup = cold_drinks_quantity)
#THE END OF COLD-DRINKS MENU        THE END OF COLD-DRINKS MENU         THE END OF COLD-DRINKS MENU


@dp.callback_query_handler(text = "drinks-and-juices")
async def fresh_drinks_menu(call: types.CallbackQuery):
    """Menu for Fresh Drinks and Juices"""
    await call.message.answer("Here is our Fresh Drinks and Juices menu:", reply_markup = fresh_drinks)


@dp.callback_query_handler(text = "from-fresh-drinks-to-drinks")
async def drinks_menu(call: types.CallbackQuery):
    """Retruns from Fresh Drinks Menu Drinks Menu"""
    await call.message.answer("Here is our 🥤Drinks🥤 menu:", reply_markup = drinks)


@dp.callback_query_handler(text = "bliss")
async def order_bliss(call: types.CallbackQuery):
    """Ordering Bliss Juice 1l"""
    await call.message.answer_photo(
        photo = open("images/bliss.jpg", "rb"),
        caption = "Juice Bliss! Price is 10 000. How many?", reply_markup = fresh_drinks_quantity)


@dp.callback_query_handler(text = "fresh")
async def order_bliss(call: types.CallbackQuery):
    """Ordering Fresh Apple and Carrot Juice"""
    await call.message.answer_photo(
        photo = open("images/carrot+apple.jpg", "rb"),
        caption = "Fresh Carrot + Apple! Price is 13 000. How many?", reply_markup = fresh_drinks_quantity)


@dp.callback_query_handler(text = "from_quantity_to_fresh_drinks_menu")
async def cold_drinks_menu(call: types.CallbackQuery):
    """Menu for Fresh Drinks itself"""
    await call.message.answer("Here is our Fresh Drinks and Juices menu:", reply_markup = fresh_drinks)


@dp.callback_query_handler(text = "dessert")
async def dessert_menu(call: types.CallbackQuery):
    """MENU FOR DESSERT"""
    await call.message.answer_photo(
        photo = open("images/dessert_menu.jpg", "rb"),
        caption = "Here is the Dessert menu!!!", reply_markup = dessert)


@dp.callback_query_handler(text = "asalim")
async def order_dessert(call: types.CallbackQuery):
    """MENU FOR DESSERT"""
    await call.message.answer_photo(
        photo = open("images/asalim.jpg", "rb"),
        caption = """Price is 18 000
The traditional flavor is honey biscuits and cream
How many?""", reply_markup = dessert_quantity)


@dp.callback_query_handler(text = "strawberry")
async def order_dessert(call: types.CallbackQuery):
    """MENU FOR DESSERT"""
    await call.message.answer_photo(
        photo = open("images/strawberry.jpg", "rb"),
        caption = """Price is 14 000
Strawberry Muss
How many?""", reply_markup = dessert_quantity)


@dp.callback_query_handler(text = "choco")
async def order_dessert(call: types.CallbackQuery):
    """MENU FOR DESSERT"""
    await call.message.answer_photo(
        photo = open("images/choco.jpg", "rb"),
        caption = """Price is 18 000
The traditional flavor is chocolate biscuits and cream
How many?""", reply_markup = dessert_quantity)


@dp.callback_query_handler(text = "from_quantity_to_dessert_menu")
async def cold_drinks_menu(call: types.CallbackQuery):
    """MENU FOR DESSERT"""
    await call.message.answer_photo(
        photo = open("images/dessert_menu.jpg", "rb"),
        caption = "Here is the Dessert menu!!!", reply_markup = dessert)


@dp.callback_query_handler(text = "pizza")
async def pizza_menu(call: types.CallbackQuery):
    """MENU FOR PIZZA!!!"""
    await call.message.answer("Here is the Pizza Menu!!!", reply_markup = pizza)


@dp.callback_query_handler(text = "pepperoni")
async def order_pepperoni(call: types.CallbackQuery):
    """Ordering Pepperoni"""
    await call.message.answer_photo(
        photo = open("images/pepperoni.jpg", "rb"),
        caption = """Price is 65 000
Pizza Pepperoni! (33 cm) 
Pizza Tomato Sauce
Cheese 110 gr
How many?""", reply_markup = pizza_quantity)


@dp.callback_query_handler(text = "pineapple")
async def order_pepperoni(call: types.CallbackQuery):
    """Ordering Pizza with Pineapple"""
    await call.message.answer_photo(
        photo = open("images/pineapple.jpg", "rb"),
        caption = """Price is 65 000
Pizza Pepperoni! (33 cm) 
Pizza Tomato Sauce
3 types of sausage (130gr)
Mushrooms
How many?""", reply_markup = pizza_quantity)


@dp.callback_query_handler(text = "margaritta")
async def order_margaritta(call: types.CallbackQuery):
    """Ordering Margaritta"""
    await call.message.answer_photo(
        photo = open("images/margaritta.jpg", "rb"),
        caption = """Price is 65 000
Pizza Pepperoni! (33 cm) 
Pizza Tomato Sauce
Cheese (100 gr.)
How many?""", reply_markup = pizza_quantity)


@dp.callback_query_handler(text = "from_quantity_to_pizza_menu")
async def pizza_menu(call: types.CallbackQuery):
    """MENU FOR DESSERT"""
    await call.message.answer("Here is the Dessert menu!!!", reply_markup = pizza)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)