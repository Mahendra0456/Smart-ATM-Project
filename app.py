import streamlit as st

# ---------- Page Config ----------
st.set_page_config(page_title="Smart ATM", layout="centered")

# ---------- Custom CSS ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #1e3c72, #2a5298);
    color: white;
}

.block-container {
    max-width: 700px;
    margin: auto;
    padding-top: 6rem;
    text-align: center;
}

.main-title {
    font-size: 48px;
    font-weight: bold;
    margin-bottom: 10px;
}

.sub-title {
    font-size: 24px;
    margin-bottom: 40px;
}

.stButton>button {
    width: 220px;
    height: 60px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
    background-color: #4da3ff;
    color: white;
    border: none;
}

.stButton>button:hover {
    background-color: #6bb8ff;
}

/* 👇 INPUT TEXT BLACK */
input {
    background-color: white !important;
    color: black !important;
}

label {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)


# ---------- Session ----------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "balance" not in st.session_state:
    st.session_state.balance = 5000.0
if "show_deposit" not in st.session_state:
    st.session_state.show_deposit = False
if "show_withdraw" not in st.session_state:
    st.session_state.show_withdraw = False

# ---------- Login ----------
def login():
    st.markdown('<div class="main-title">🏦 SMART ATM</div>', unsafe_allow_html=True)
    pin = st.text_input("Enter your 4-digit PIN", type="password")

    if st.button("Login"):
        if pin == "1234":
            st.session_state.authenticated = True
        else:
            st.error("Incorrect PIN")

# ---------- ATM Menu ----------
def atm_menu():
    st.markdown('<div class="main-title">💳 ATM Processing Screen</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Choose One Option To Continue</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        if st.button("🪙 Check Balance"):
            st.success(f"Your Balance: ₹{st.session_state.balance:.2f}")

        if st.button("➕ Deposit"):
            st.session_state.show_deposit = True
            st.session_state.show_withdraw = False

    with col2:
        if st.button("💸 Withdraw"):
            st.session_state.show_withdraw = True
            st.session_state.show_deposit = False

        if st.button("🚪 Logout"):
            st.session_state.authenticated = False

    # -------- Deposit Section --------
    if st.session_state.show_deposit:
        amount = st.number_input("Enter Deposit Amount", min_value=0.0, step=100.0)
        if st.button("Confirm Deposit"):
            st.session_state.balance += amount
            st.success("Deposit Successful")
            st.session_state.show_deposit = False

    # -------- Withdraw Section --------
    if st.session_state.show_withdraw:
        amount = st.number_input("Enter Withdraw Amount", min_value=0.0, step=100.0)
        if st.button("Confirm Withdrawal"):
            if amount <= st.session_state.balance:
                st.session_state.balance -= amount
                st.success("Withdrawal Successful")
            else:
                st.error("Insufficient Balance")
            st.session_state.show_withdraw = False


# ---------- Main ----------
if not st.session_state.authenticated:
    login()
else:
    atm_menu()
