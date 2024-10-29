# Jinja2 Flask Forms Template Application

This project is a simple Flask web application that demonstrates handling forms to collect user input and displaying results based on that input. The application includes various features, including a Fro-Yo order form, favorite selections, a secret message sorter, a calculator, and a horoscope personality lookup.

## Features
- **Homepage** with handy links.
- **Fro-Yo Order Form** to choose flavor and toppings.
- **Favorites Form** to select favorite color, animal, and city.
- **Secret Message Form** to enter a secret message and receive a sorted version.
- **Calculator** for basic arithmetic operations (addition, subtraction, multiplication, division).
- **Horoscope Form** to select a horoscope sign and display personality traits and a lucky number.

## File Structure
```
FlaskFormsTemplate/
├── app.py
├── test_app.py
└── templates/
    ├── calculator_form.html
    ├── calculator_results.html
    ├── froyo_form.html
    ├── horoscope_form.html
    └── horoscope_results.html
```

## Templates

### 1. `calculator_form.html`
This template displays a form for users to input two numbers and select an arithmetic operation.

```html
<!DOCTYPE html>
<html>
    <body>
        <form action="/calculator_results" method="GET">
            Please enter 2 numbers and select an operator.<br/><br/>
            <input type="number" name="operand1">
            <select name="operation">
                <option value="add">+</option>
                <option value="subtract">-</option>
                <option value="multiply">*</option>
                <option value="divide">/</option>
            </select>
            <input type="number" name="operand2">
            <input type="submit" value="Submit!">
        </form>
    </body>
</html>
```

### 2. `calculator_results.html`
This template shows the result of the arithmetic operation chosen by the user.

```html
<!DOCTYPE html>
<html>
    <body>
        <p>You chose to {{math_operation}} {{operand1}} and {{operand2}}. Your result is: {{result}}</p>
    </body>
</html>
```

### 3. `froyo_form.html`
This template collects the user's favorite color, animal, and city.

```html
<!DOCTYPE html>
<html>
    <body>
        <form action="/favorite_results" method="GET">
            What is your favorite color?<br/>
            <input type="text" name="color"><br/>
            What is your favorite animal?<br/>
            <input type="text" name="animal"><br/>
            What is your favorite city?<br/>
            <input type="text" name="city"><br/>
            <input type="submit" value="Submit!">
        </form>
    </body>
</html>
```

### 4. `horoscope_form.html`
This template allows users to input their name and select their horoscope sign.

```html
<!DOCTYPE html>
<html>
    <body>
        <form action="/horoscope_results" method="GET">
            What is your name?
            <input type="text" name="name"><br><br>
            Select your Horoscope Sign<br>
            <select name="horoscope_sign">
                <option value="capricorn">December 22 - January 19 | ♑️</option>
                <option value="aquarius">January 20 - February 18 | ♒️</option>
                <option value="pisces">February 19 - March 20 | ♓️</option>
                <option value="aries">March 21 - April 19 | ♈️</option>
                <option value="taurus">April 20 - May 20 | ♉️</option>
                <option value="gemini">May 21 - June 21 | ♊️</option>
                <option value="cancer">June 22 - July 22 | ♋️</option>
                <option value="leo">July 23 - August 22 | ♌️</option>
                <option value="virgo">August 23 - September 22 | ♍️</option>
                <option value="libra">September 23 - October 22 | ♎️</option>
                <option value="scorpio">October 23 - November 21 | ♏️</option>
                <option value="sagittarius">November 22 - December 21 | ♐️</option>
            </select><br><br>
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
```

### 5. `horoscope_results.html`
This template displays the user's horoscope sign, personality traits, and a lucky number.

```html
<!DOCTYPE html>
<html>
    <body>
        <h1>Hello {{name.capitalize()}}</h1>
        <h3>You are a <strong>{{horoscope_sign.capitalize()}}</strong></h3>
        <h3>Your personality according to your horoscope is: {{personality}}</h3>
        <h3>Your lucky number is: {{lucky_number}}</h3>
    </body>
</html>
```

## Running the Application
To run the application, ensure you have Flask installed, then execute the following command in your terminal:

```bash
python app.py
```

Access the application in your web browser at `http://127.0.0.1:5000/`.

## Running Tests
To run the tests, ensure you have `unittest` installed, then execute the following command in your terminal:

```bash
python test_app.py
```
