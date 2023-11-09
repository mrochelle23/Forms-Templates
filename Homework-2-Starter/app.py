import random
from flask import Flask, request, render_template


app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/>
        What kind of toppings do you want?<br/>
        <input type="text" name="toppings"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    users_froyo_toppings = request.args.get('toppings')
    return f'You ordered {users_froyo_flavor} flavored Fro-Yo with {users_froyo_toppings}!'

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return render_template('froyo_form.html')

@app.route('/favorites_results', methods=['GET'])
def favorites_results():
    """Shows the user a nice message using their form results."""
    context = {
        "color": request.args.get("color"),
        "animal": request.args.get("animal"),
        "city": request.args.get("city")
    }
    return render_template('froyo_results.html', **context)

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        Enter your secret message<br/>
        <input type="text" name="message"><br/> <br/>
        <input type="submit" name="Submit">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    users_secret_message = request.form.get('message')
    sorted_message = sort_letters(users_secret_message)
    return f'Here is your secret message {sorted_message}'

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    operand1 = int(request.args.get("operand1"))
    operand2 = int(request.args.get("operand2"))
    operation = request.args.get("operation")
    if operation == 'add':
        result = operand1 + operand2
        math_operation = "add"
        symbol = "+"
    elif operation == 'subtract':
        result = operand1 - operand2
        math_operation = "subtract"
        symbol = "-"
    elif operation == 'multiply':
        result = operand1 * operand2
        math_operation = "multiply"
        symbol = "*"
    elif operation == 'divide':
        result = operand1 / operand2
        math_operation = "divide"
        symbol = "/"
    context = {
        'operand1': operand1,
        'operand2': operand2,
        'symbol': symbol,
        'math_operation': math_operation,
        'result': result
    }
    return render_template('calculator_results.html', **context)

HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""
    # TODO: Get the sign the user entered in the form, based on their birthday
    horoscope_sign = request.args.get("horoscope_sign")

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    users_personality = HOROSCOPE_PERSONALITIES.get(horoscope_sign)

    # TODO: Generate a random number from 1 to 99
    lucky_number = random.randint(1, 99)

    context = {
        'horoscope_sign': horoscope_sign,
        'personality': users_personality, 
        'lucky_number': lucky_number,
        "name": request.args.get("name")
    }
    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
