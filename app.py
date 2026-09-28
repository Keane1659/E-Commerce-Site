import streamlit as st

st.set_page_config(page_title="CuteSenses", page_icon="🐾", layout="wide")

products = [
    {"id": 1, "name": "Cozy Knit Sweater", "category": "Clothing", "price": 39.99, "rating": 4.9, "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=900&q=80", "description": "Soft and warm knitwear for everyday comfort and cute style."},
    {"id": 2, "name": "Pastel Hoodie", "category": "Clothing", "price": 42.50, "rating": 4.8, "image": "https://images.unsplash.com/photo-1529139574466-a303027c1d8b?auto=format&fit=crop&w=900&q=80", "description": "A relaxed, cozy layer with a cheerful pastel finish."},
    {"id": 3, "name": "Classic Knit Cardigan", "category": "Clothing", "price": 47.00, "rating": 4.9, "image": "https://images.unsplash.com/photo-1483985988355-763728e1935b?auto=format&fit=crop&w=900&q=80", "description": "A sweet layering staple for chilly days and soft looks."},

    {"id": 4, "name": "Cottage Crochet Tote", "category": "Crochet", "price": 28.50, "rating": 4.8, "image": "https://images.unsplash.com/photo-1524384308090-7084c769cfe3?auto=format&fit=crop&w=900&q=80", "description": "Handmade crochet tote with a charming pastel finish."},
    {"id": 5, "name": "Mini Crochet Basket", "category": "Crochet", "price": 24.25, "rating": 4.7, "image": "https://images.unsplash.com/photo-1517849845537-4d257902454a?auto=format&fit=crop&w=900&q=80", "description": "A handwoven basket with a cozy handmade look."},
    {"id": 6, "name": "Shell Crochet Pouch", "category": "Crochet", "price": 19.99, "rating": 4.8, "image": "https://images.unsplash.com/photo-1533073526757-2c8ca1df9f1c?auto=format&fit=crop&w=900&q=80", "description": "A compact pouch that brings texture and charm to your essentials."},

    {"id": 7, "name": "Mini Dog Plush", "category": "Accessories", "price": 22.00, "rating": 4.9, "image": "https://images.unsplash.com/photo-1517849845537-4d257902454a?auto=format&fit=crop&w=900&q=80", "description": "Sweet black-and-white plush with floppy ears and extra charm."},
    {"id": 8, "name": "Silk Scrunchie Set", "category": "Accessories", "price": 15.75, "rating": 4.7, "image": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=900&q=80", "description": "Soft pastel scrunchies that add a cute accent to any outfit."},
    {"id": 9, "name": "Petal Hair Clip", "category": "Accessories", "price": 12.50, "rating": 4.8, "image": "https://images.unsplash.com/photo-1521590832167-7a2d3a5d3b57?auto=format&fit=crop&w=900&q=80", "description": "A tiny floral clip that brings playful detail to your look."},

    {"id": 10, "name": "Lucky Coin Charm", "category": "Coins", "price": 18.00, "rating": 4.7, "image": "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?auto=format&fit=crop&w=900&q=80", "description": "A playful coin-inspired charm with sweet sentimental energy."},
    {"id": 11, "name": "Moon Coin Token", "category": "Coins", "price": 16.50, "rating": 4.8, "image": "https://images.unsplash.com/photo-1520637836862-4d197d17c90a?auto=format&fit=crop&w=900&q=80", "description": "A metallic keepsake inspired by moonlit sparkle and charm."},
    {"id": 12, "name": "Paw Coin Pendant", "category": "Coins", "price": 20.25, "rating": 4.9, "image": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=900&q=80", "description": "A tiny collectible pendant for lovers of cozy, playful décor."},

    {"id": 13, "name": "Bloom Carry Bag", "category": "Bags", "price": 29.99, "rating": 4.8, "image": "https://images.unsplash.com/photo-1590874103328-eac38a683ce7?auto=format&fit=crop&w=900&q=80", "description": "A roomy bag with a cheerful floral finish for everyday outings."},
    {"id": 14, "name": "Market Tote", "category": "Bags", "price": 26.75, "rating": 4.7, "image": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?auto=format&fit=crop&w=900&q=80", "description": "A sturdy tote for errands, books, and cute daily essentials."},
    {"id": 15, "name": "Pocket Crossbody", "category": "Bags", "price": 31.50, "rating": 4.9, "image": "https://images.unsplash.com/photo-1591951425328-48c1fe7179a8?auto=format&fit=crop&w=900&q=80", "description": "A compact crossbody for your wallet, lip balm, and little treasures."},

    {"id": 16, "name": "Floral Wall Hanging", "category": "Home Decor", "price": 31.25, "rating": 4.6, "image": "https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=900&q=80", "description": "A cheerful floral wall accent to brighten a cozy corner."},
    {"id": 17, "name": "Peach Table Runner", "category": "Home Decor", "price": 35.00, "rating": 4.8, "image": "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=900&q=80", "description": "A bright table accent to bring cozy charm to your room."},
    {"id": 18, "name": "Cozy Candle Tray", "category": "Home Decor", "price": 18.75, "rating": 4.8, "image": "https://images.unsplash.com/photo-1517705008128-361805f42e86?auto=format&fit=crop&w=900&q=80", "description": "A warm, decorative tray for candles, notes, and little keepsakes."},
]

if "cart" not in st.session_state:
    st.session_state.cart = {}

if "selected_category" not in st.session_state:
    st.session_state.selected_category = "Clothing"

categories = ["Clothing", "Crochet", "Accessories", "Coins", "Bags", "Home Decor"]


def add_to_cart(product_id, quantity=1):
    key = str(product_id)
    st.session_state.cart[key] = st.session_state.cart.get(key, 0) + quantity


def update_quantity(product_id, delta):
    key = str(product_id)
    new_qty = st.session_state.cart.get(key, 0) + delta
    if new_qty <= 0:
        st.session_state.cart.pop(key, None)
    else:
        st.session_state.cart[key] = new_qty


st.markdown(
    """
    <style>
        :root {
            --pink: #f8b7c8;
            --pink-deep: #c43d5e;
            --gray-700: #3d3d3d;
            --gray-500: #6b7280;
            --gray-200: #e5e7eb;
            --white: #ffffff;
        }

        .stApp {
            background: linear-gradient(180deg, #ffffff 0%, #fff7fa 100%);
            color: var(--gray-700);
        }

        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 2rem;
        }

        .brand-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            background: linear-gradient(90deg, #fff3f7 0%, #ffffff 100%);
            border: 1px solid var(--gray-200);
            border-radius: 18px;
            padding: 0.8rem 1rem;
            margin-bottom: 1rem;
        }

        .brand-left {
            display: flex;
            align-items: center;
            gap: 0.8rem;
        }

        .logo-badge {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background: #ffffff;
            border: 3px solid #111111;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 12px 22px rgba(0, 0, 0, 0.14);
        }

        .logo-badge img {
            width: 118%;
            height: 118%;
            object-fit: cover;
            display: block;
            border-radius: 50%;
            filter: grayscale(100%) contrast(1.35) brightness(0.95);
            transform: scale(1.08);
        }

        .brand-name {
            margin: 0;
            font-size: 2.3rem;
            font-weight: 900;
            letter-spacing: 0.07em;
            text-transform: uppercase;
            color: var(--pink-deep) !important;
        }

        .brand-tag {
            font-size: 0.68rem;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            color: var(--gray-500);
        }

        .category-row {
            display: grid;
            grid-template-columns: repeat(6, minmax(0, 1fr));
            gap: 0.7rem;
            margin: 0.8rem 0 1rem;
        }

        .stButton > button {
            width: 100%;
            min-height: 62px;
            border-radius: 12px;
            border: 1px solid var(--gray-200);
            background: #ffffff;
            color: var(--gray-700);
            font-weight: 800;
            font-size: 1rem;
            transition: all 0.2s ease;
            box-shadow: none;
        }

        .stButton > button:hover {
            border-color: #efb5c7;
            color: var(--pink-deep);
            background: #fffafc;
        }

        .product-card {
            background: var(--white);
            border: 1px solid var(--gray-200);
            border-radius: 18px;
            padding: 1rem;
            height: 100%;
            box-shadow: 0 8px 20px rgba(0,0,0,0.04);
        }

        .cart-card {
            background: var(--white);
            border: 1px solid var(--gray-200);
            border-radius: 18px;
            padding: 1rem;
            box-shadow: 0 8px 20px rgba(0,0,0,0.04);
            position: sticky;
            top: 1rem;
        }

        .st-expander {
            border: 1px solid var(--gray-200);
            border-radius: 14px;
            background: #ffffff;
        }

        .st-expander header {
            background: #fff5f9;
            color: var(--pink-deep);
            font-weight: 700;
        }

        .cart-qty-button {
            background: #ffffff !important;
            color: var(--gray-700) !important;
            border: 1px solid var(--gray-200) !important;
            border-radius: 8px !important;
            min-width: 2.2rem !important;
            height: 2.2rem !important;
            padding: 0 !important;
            font-size: 1rem !important;
            font-weight: 700 !important;
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
        }

        .cart-qty-button:hover {
            border-color: #efb5c7 !important;
            color: var(--pink-deep) !important;
            background: #fffafc !important;
        }

        div[data-testid="stFormSubmitButton"] button {
            background: #ffffff !important;
            color: #3d3d3d !important;
            border: 1px solid #e5e7eb !important;
            border-radius: 8px !important;
            min-width: 2.2rem !important;
            height: 2.2rem !important;
            padding: 0 !important;
            font-size: 1rem !important;
            font-weight: 700 !important;
        }

        div[data-testid="stFormSubmitButton"] button:hover {
            background: #fffafc !important;
            color: var(--pink-deep) !important;
            border-color: #efb5c7 !important;
        }

        div[data-testid="stImage"] {
            overflow: hidden;
            border-radius: 14px;
        }

        div[data-testid="stImage"] img {
            border-radius: 14px;
            display: block;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="brand-bar">
        <div class="brand-left">
            <div class="logo-badge">
                <img src="https://img.magnific.com/premium-vector/dog-logo-design-icon-symbol-vector-illustration_1123785-3846.jpg" alt="CuteSenses logo" />
            </div>
            <div>
                <div class="brand-name">CuteSenses</div>
                <div class="brand-tag">sweet finds for everyday joy</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

cat_cols = st.columns(len(categories))
for idx, category in enumerate(categories):
    with cat_cols[idx]:
        selected = category == st.session_state.selected_category
        button_label = category
        if st.button(button_label, key=f"cat_{category}", use_container_width=True, type="secondary"):
            st.session_state.selected_category = category

filtered_products = [p for p in products if p["category"] == st.session_state.selected_category]

catalog_col, cart_col = st.columns([3, 1.25])

with catalog_col:
    st.subheader(f"{st.session_state.selected_category}")
    product_cols = st.columns(3)
    for idx, product in enumerate(filtered_products):
        with product_cols[idx % 3]:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            st.image(product["image"], width=260)
            st.markdown(f"### {product['name']}")
            st.caption(product["description"])
            st.write(f"⭐ {product['rating']}   •   ${product['price']:.2f}")
            if st.button("Purchase", key=f"purchase_{product['id']}", use_container_width=True):
                add_to_cart(product["id"], 1)
                st.toast(f"{product['name']} added to your cart")
            st.markdown("</div>", unsafe_allow_html=True)

with cart_col:
    st.markdown('<div class="cart-card">', unsafe_allow_html=True)
    with st.expander("🛒 Shopping cart", expanded=True):
        if st.session_state.cart:
            total = 0.0
            for product in products:
                qty = st.session_state.cart.get(str(product["id"]), 0)
                if qty > 0:
                    item_total = qty * product["price"]
                    total += item_total

                    left_col, qty_col = st.columns([2.2, 0.8])
                    left_col.write(product["name"])

                    with st.form(key=f"cart_qty_{product['id']}", clear_on_submit=False):
                        qty_controls = st.columns([1, 1.2, 1])
                        with qty_controls[0]:
                            minus_clicked = st.form_submit_button("-", use_container_width=True, type="secondary")
                        with qty_controls[1]:
                            st.write(f"Qty: {qty}")
                        with qty_controls[2]:
                            plus_clicked = st.form_submit_button("+", use_container_width=True, type="secondary")

                        if minus_clicked:
                            update_quantity(product["id"], -1)
                        if plus_clicked:
                            add_to_cart(product["id"], 1)

                    st.write(f"${item_total:.2f}")
                    st.markdown("---")

            st.markdown(f"### Total: ${total:.2f}")
            st.button("Checkout", type="primary")
        else:
            st.info("Your cart is empty. Purchase an item to add it here.")
    st.markdown("</div>", unsafe_allow_html=True)
