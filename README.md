# CuteSenses

CuteSenses is a boutique-style e-commerce storefront built with Python and Streamlit. The site showcases a curated collection of handmade and lifestyle products organized into categories such as Clothing, Crochet, Accessories, Coins, Bags, and Home Decor. It includes a branded storefront header, product cards, category navigation, and a shopping cart panel with quantity controls.

This project was developed as a school assignment to demonstrate a clean, user-friendly storefront experience with interactive product browsing and cart functionality.

## Features

- Responsive storefront layout with a boutique branding style
- Category navigation across multiple product sections
- Product cards with images, descriptions, ratings, and prices
- Add-to-cart functionality with quantity updates
- Shopping cart summary with total calculation
- Minimal, modern design with soft pink and white styling

## Tech Stack

- Python 3
- Streamlit

## Project Structure

- `app.py` — main storefront application logic and UI
- `requirements.txt` — project dependencies

## Installation

1. Open a terminal in the project folder.
2. Create and activate a virtual environment if you want an isolated setup:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. If Streamlit is not included in your environment, install it manually:

   ```bash
   pip install streamlit
   ```

## Usage

Run the app from the project directory:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

### Using the Storefront

- Browse products by selecting a category at the top of the page.
- Click "Purchase" on any product to add it to the shopping cart.
- Use the minus and plus controls in the cart to adjust item quantity.
- View the subtotal and total before checkout.

## Notes

This project is designed as a simple front-end storefront demo and is ideal for learning Streamlit UI patterns, session state, and interactive e-commerce layout design.

## License

This project is for educational purposes.
