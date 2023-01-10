from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

contact = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton(text = "Press this button to send your phone number", request_contact = True)
		], 
	], resize_keyboard = True
)


location = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton(text = "Press this button to send your location", request_location = True)
		], 
	], resize_keyboard = True
)

menu = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton(text = "Order 🍽")
		],
		[
			KeyboardButton(text = "Settings ⚙️"),
			KeyboardButton(text = "Support 📞")
		]
	], resize_keyboard = True
)

order = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "🌯🌯Lavash", callback_data = "lavash"),
			InlineKeyboardButton(text = "🌭🌭Hot-Dog", callback_data = "hot_dog")
		],
		[	
			InlineKeyboardButton(text = "🥪🥪Sandwich Club", callback_data = "sandwich_club"),
			InlineKeyboardButton(text = "🌮🌮Shaurma", callback_data = "shaurma")
		],
		[	
			InlineKeyboardButton(text = "🍔🍔Burger", callback_data = "burger"),
			InlineKeyboardButton(text = "🍱🍱Donar", callback_data = "donar")
		],
		[	
			InlineKeyboardButton(text = "🍟🍟Fries", callback_data = "fries"),
			InlineKeyboardButton(text = "🥤🥤Drinks", callback_data = "drinks")
		],
		[	
			InlineKeyboardButton(text = "🍰🍰Dessert", callback_data = "dessert"),
			InlineKeyboardButton(text = "🍕🍕Pizza", callback_data = "pizza")
		]
	]
)

lavash = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "🥩Beef", callback_data = "beef_lavash"),
			InlineKeyboardButton(text = "🍗Chicken", callback_data = "chicken_lavash")
		],
		[
			InlineKeyboardButton(text = "🥩🌶Spicy Beef", callback_data = "spicy_beef_lavash"),
			InlineKeyboardButton(text = "🍗🌶Spicy Chicken", callback_data = "spicy_chicken_lavash")
		],
		[
			InlineKeyboardButton(text = "🥩🧀Cheesy Beef", callback_data = "cheesy_beef_lavash"),
			InlineKeyboardButton(text = "🍗🧀Cheesy Chicken", callback_data = "cheesy_chicken_lavash")
		],
		[
			InlineKeyboardButton(text = "🥬Fitter", callback_data = "fitter")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back1")
		]
	]
)

beef_lavash_size = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Mini👍", callback_data = "beef_lavash_mini"),
			InlineKeyboardButton(text = "Classic👍", callback_data = "beef_lavash_classic")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_size_to_lavash_menu")
		]
	]
)

beef_lavash_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "beef:from_quantity_to_size_menu")
		]
	]
)

chicken_lavash_size = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Mini👍", callback_data = "chicken_lavash_mini"),
			InlineKeyboardButton(text = "Classic👍", callback_data = "chicken_lavash_classic")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_size_to_lavash_menu")
		]
	]
)

chicken_lavash_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "chicken:from_quantity_to_size_menu")
		]
	]
)

spicy_beef_lavash_size = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Mini👍", callback_data = "spicy_beef_lavash_mini"),
			InlineKeyboardButton(text = "Classic👍", callback_data = "spicy_beef_lavash_classic")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_size_to_lavash_menu")
		]
	]
)

spicy_beef_lavash_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "spicy_beef:from_quantity_to_size_menu")
		]
	]
)

spicy_chicken_lavash_size = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Mini👍", callback_data = "spicy_chicken_lavash_mini"),
			InlineKeyboardButton(text = "Classic👍", callback_data = "spicy_chicken_lavash_classic")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_size_to_lavash_menu")
		]
	]
)

spicy_chicken_lavash_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "spicy_chicken:from_quantity_to_size_menu")
		]
	]
)

cheesy_beef_lavash_size = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Mini👍", callback_data = "cheesy_beef_lavash_mini"),
			InlineKeyboardButton(text = "Classic👍", callback_data = "cheesy_beef_lavash_classic")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_size_to_lavash_menu")
		]
	]
)

cheesy_beef_lavash_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "cheesy_beef:from_quantity_to_size_menu")
		]
	]
)

cheesy_chicken_lavash_size = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Mini👍", callback_data = "cheesy_chicken_lavash_mini"),
			InlineKeyboardButton(text = "Classic👍", callback_data = "cheesy_chicken_lavash_classic")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_size_to_lavash_menu")
		]
	]
)

cheesy_chicken_lavash_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "cheesy_chicken:from_quantity_to_size_menu")
		]
	]
)

fitter_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_quantity_to_lavash_menu")
		]
	]
)

hot_dog = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "🌭🌭Baget Double", callback_data = "hot-dog-baget-double"),
			InlineKeyboardButton(text = "🌭Classic", callback_data = "classic-hot-dog")
		],
		[
			InlineKeyboardButton(text = "👑 Royal", callback_data = "royal-hot-dog"),
			InlineKeyboardButton(text = "🍗 Chicken", callback_data = "chicken-hot-dog")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back1")
		]
	]
)

hot_dog_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_quantity_to_hot_dog_menu")
		]
	]
)

sandwich = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "🥪Classic", callback_data = "classic-sandwich"),
			InlineKeyboardButton(text = "🍗Chicken", callback_data = "chicken-sandwich")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back1")
		]
	]
)

sanwich_club_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_quantity_to_sandwich_menu")
		]
	]
)

shaurma = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "🥩Beef", callback_data = "beef_shaurma"),
			InlineKeyboardButton(text = "🍗Chicken", callback_data = "chicken_shaurma")
		],
		[
			InlineKeyboardButton(text = "🥩🌶Spicy Beef", callback_data = "spicy_beef_shaurma"),
			InlineKeyboardButton(text = "🍗🌶Spicy Chicken", callback_data = "spicy_chicken_shaurma")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back1")
		]
	]
)

beef_shaurma_size = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Mini👍", callback_data = "beef_shaurma_mini"),
			InlineKeyboardButton(text = "Classic👍", callback_data = "beef_shaurma_classic")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_size_to_shaurma_menu")
		]
	]
)

beef_shaurma_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "beef_shaurma:from_quantity_to_size_menu")
		]
	]
)

chicken_shaurma_size = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Mini👍", callback_data = "chicken_shaurma_mini"),
			InlineKeyboardButton(text = "Classic👍", callback_data = "chicken_shaurma_classic")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_size_to_shaurma_menu")
		]
	]
)

chicken_shaurma_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "chicken_shaurma:from_quantity_to_size_menu")
		]
	]
)

spicy_beef_shaurma_size = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Mini👍", callback_data = "spicy_beef_shaurma_mini"),
			InlineKeyboardButton(text = "Classic👍", callback_data = "spicy_beef_shaurma_classic")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_size_to_shaurma_menu")
		]
	]
)

spicy_beef_shaurma_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "spicy_beef_shaurma:from_quantity_to_size_menu")
		]
	]
)

spicy_chicken_shaurma_size = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Mini👍", callback_data = "spicy_chicken_shaurma_mini"),
			InlineKeyboardButton(text = "Classic👍", callback_data = "spicy_chicken_shaurma_classic")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_size_to_shaurma_menu")
		]
	]
)

spicy_chicken_shaurma_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "spicy_chicken_shaurma:from_quantity_to_size_menu")
		]
	]
)

burger = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "🥩Hamburger", callback_data = "hamburger"),
			InlineKeyboardButton(text = "🥩🧀Cheeseburger", callback_data = "cheeseburger")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back1")
		]
	]
)

burger_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_quantity_to_burger_menu")
		]
	]
)

donar = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "🥩Beef", callback_data = "beef_donar"),
			InlineKeyboardButton(text = "🍗Chicken", callback_data = "chicken_donar")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back1")
		]
	]
)

donar_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_quantity_to_donar_menu")
		]
	]
)

fries = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "15gr. Fries", callback_data = "15gr_fries"),
			InlineKeyboardButton(text = "Rustic potatoes", callback_data = "rustic_potatoes")
		],
		[
			InlineKeyboardButton(text = "Small Rice", callback_data = "small_rice"),
			InlineKeyboardButton(text = "Large Rice", callback_data = "large_rice")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back1")
		]
	]
)

fries_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_quantity_to_fries_menu")
		]
	]
)

drinks = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Tea and Coffee", callback_data = "tea-and-coffee"),
			InlineKeyboardButton(text = "Cold drinks", callback_data = "cold-drinks")
		],
		[
			InlineKeyboardButton(text = "Fresh drinks and juices", callback_data = "drinks-and-juices")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back1")
		]		
	]
)

cof_tea = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Coffee", callback_data = "coffee"),
			InlineKeyboardButton(text = "Tea", callback_data = "tea")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_coffee_to_drinks")
		]
	]
)

coffees = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Americano", callback_data = "americano"),
			InlineKeyboardButton(text = "Capuccino", callback_data = "capuccino")
		],
		[
			InlineKeyboardButton(text = "Coffe 3v1", callback_data = "coffe_3v1"),
			InlineKeyboardButton(text = "Latte", callback_data = "latte")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from-coffees-to-cofee-and-tea")
		]		
	]
)

coffee_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_quantity_to_coffee_menu")
		]
	]
)

teas = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Green Tea", callback_data = "green_tea"),
			InlineKeyboardButton(text = "Black Tea", callback_data = "black_tea")
		],
		[
			InlineKeyboardButton(text = "Lemon Tea", callback_data = "lemon_tea")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from-teas-to-cofee-and-tea")
		]		
	]
)

tea_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_quantity_to_tea_menu")
		]
	]
)

cold_drinks = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Fanta", callback_data = "fanta"),
			InlineKeyboardButton(text = "Sprite", callback_data = "sprite")
		],
		[
			InlineKeyboardButton(text = "Coca-Cola", callback_data = "coca-cola"),
			InlineKeyboardButton(text = "Nestle", callback_data = "nestle")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from-cold-drinks-to-drinks")
		]		
	]
)

cold_drinks_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_quantity_to_cold_drinks_menu")
		]
	]
)

fresh_drinks = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Bliss Juice 1l", callback_data = "bliss"),
			InlineKeyboardButton(text = "Apple and Carrot Fresh", callback_data = "fresh")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from-fresh-drinks-to-drinks")
		]		
	]
)

fresh_drinks_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_quantity_to_fresh_drinks_menu")
		]
	]
)

dessert = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Asalim", callback_data = "asalim"),
			InlineKeyboardButton(text = "Strawberry", callback_data = "strawberry")
		],
		[
			InlineKeyboardButton(text = "Choco", callback_data = "choco")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back1")
		]		
	]
)

dessert_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_quantity_to_dessert_menu")
		]
	]
)

pizza = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Pepperoni", callback_data = "pepperoni"),
			InlineKeyboardButton(text = "With Pineapple", callback_data = "pineapple")
		],
		[
			InlineKeyboardButton(text = "Margaritta", callback_data = "margaritta")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back1")
		]		
	]
)

pizza_quantity = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "quantity_1"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "quantity_2"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "quantity_3")
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "quantity_4"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "quantity_5"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "quantity_6")
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "quantity_7"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "quantity_8"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "quantity_9")
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "from_quantity_to_pizza_menu")
		]
	]
)