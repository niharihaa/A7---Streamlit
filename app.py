import streamlit as st

# Functions for ratio calculations

def calculate_current_ratio(current_assets, current_liabilities):
    return current_assets / current_liabilities

def calculate_quick_ratio(current_assets, inventory, current_liabilities):
    return (current_assets - inventory) / current_liabilities

def calculate_cash_ratio(cash_and_equivalents, current_liabilities):
    return cash_and_equivalents / current_liabilities

def calculate_gross_profit_margin(gross_profit, revenue):
    return (gross_profit / revenue) * 100

def calculate_operating_profit_margin(operating_income, revenue):
    return (operating_income / revenue) * 100

def calculate_net_profit_margin(net_income, revenue):
    return (net_income / revenue) * 100

def calculate_roa(net_income, total_assets):
    return (net_income / total_assets) * 100

def calculate_roe(net_income, shareholders_equity):
    return (net_income / shareholders_equity) * 100

def calculate_debt_to_equity_ratio(total_liabilities, shareholders_equity):
    return total_liabilities / shareholders_equity

def calculate_debt_ratio(total_liabilities, total_assets):
    return total_liabilities / total_assets

def calculate_interest_coverage_ratio(operating_income, interest_expense):
    return operating_income / interest_expense

def calculate_asset_turnover_ratio(revenue, total_assets):
    return revenue / total_assets

def calculate_inventory_turnover_ratio(cogs, average_inventory):
    return cogs / average_inventory

def calculate_receivables_turnover_ratio(revenue, average_accounts_receivable):
    return revenue / average_accounts_receivable

def calculate_pe_ratio(market_price_per_share, earnings_per_share):
    return market_price_per_share / earnings_per_share

def calculate_pb_ratio(market_price_per_share, book_value_per_share):
    return market_price_per_share / book_value_per_share

def calculate_dividend_yield(annual_dividends_per_share, market_price_per_share):
    return annual_dividends_per_share / market_price_per_share

def calculate_sharpe_ratio(portfolio_return, risk_free_rate, std_deviation_portfolio_return):
    return (portfolio_return - risk_free_rate) / std_deviation_portfolio_return

def calculate_jensens_alpha(portfolio_return, risk_free_rate, beta, market_return):
    return portfolio_return - (risk_free_rate + beta * (market_return - risk_free_rate))

def calculate_accounts_receivable_turnover(net_credit_sales, average_accounts_receivable):
    return net_credit_sales / average_accounts_receivable

def calculate_working_capital_ratio(net_sales, working_capital):
    return net_sales / working_capital

def calculate_asset_turnover_ratio_sales(sales, average_total_assets):
    return sales / average_total_assets

def calculate_days_payable_outstanding(accounts_payable, cost_of_sales, number_of_days):
    return accounts_payable / (cost_of_sales / number_of_days)

# Streamlit App

st.title('Financial Ratios Calculator')

# Liquidity Ratios
st.header('Liquidity Ratios')

# Current Ratio
st.subheader('Current Ratio')
current_assets = st.number_input('Current Assets', min_value=0.0, key='current_assets')
current_liabilities = st.number_input('Current Liabilities', min_value=0.0, key='current_liabilities')
if st.button('Calculate Current Ratio'):
    current_ratio = calculate_current_ratio(current_assets, current_liabilities)
    st.write(f'Current Ratio: {current_ratio:.2f}')

# Quick Ratio
st.subheader('Quick Ratio')
quick_assets = st.number_input('Current Assets', min_value=0.0, key='quick_assets')
inventory = st.number_input('Inventory', min_value=0.0, key='inventory')
quick_liabilities = st.number_input('Current Liabilities', min_value=0.0, key='quick_liabilities')
if st.button('Calculate Quick Ratio'):
    quick_ratio = calculate_quick_ratio(quick_assets, inventory, quick_liabilities)
    st.write(f'Quick Ratio: {quick_ratio:.2f}')

# Cash Ratio
st.subheader('Cash Ratio')
cash_and_equivalents = st.number_input('Cash and Cash Equivalents', min_value=0.0, key='cash_and_equivalents')
cash_liabilities = st.number_input('Current Liabilities', min_value=0.0, key='cash_liabilities')
if st.button('Calculate Cash Ratio'):
    cash_ratio = calculate_cash_ratio(cash_and_equivalents, cash_liabilities)
    st.write(f'Cash Ratio: {cash_ratio:.2f}')

# Profitability Ratios
st.header('Profitability Ratios')

# Gross Profit Margin
st.subheader('Gross Profit Margin')
gross_profit = st.number_input('Gross Profit', min_value=0.0, key='gross_profit')
revenue = st.number_input('Revenue', min_value=0.0, key='revenue')
if st.button('Calculate Gross Profit Margin'):
    gross_profit_margin = calculate_gross_profit_margin(gross_profit, revenue)
    st.write(f'Gross Profit Margin: {gross_profit_margin:.2f}%')

# Operating Profit Margin
st.subheader('Operating Profit Margin')
operating_income = st.number_input('Operating Income', min_value=0.0, key='operating_income')
revenue_op = st.number_input('Revenue', min_value=0.0, key='revenue_op')
if st.button('Calculate Operating Profit Margin'):
    operating_profit_margin = calculate_operating_profit_margin(operating_income, revenue_op)
    st.write(f'Operating Profit Margin: {operating_profit_margin:.2f}%')

# Net Profit Margin
st.subheader('Net Profit Margin')
net_income = st.number_input('Net Income', min_value=0.0, key='net_income')
revenue_np = st.number_input('Revenue', min_value=0.0, key='revenue_np')
if st.button('Calculate Net Profit Margin'):
    net_profit_margin = calculate_net_profit_margin(net_income, revenue_np)
    st.write(f'Net Profit Margin: {net_profit_margin:.2f}%')

# Return on Assets (ROA)
st.subheader('Return on Assets (ROA)')
net_income_roa = st.number_input('Net Income', min_value=0.0, key='net_income_roa')
total_assets_roa = st.number_input('Total Assets', min_value=0.0, key='total_assets_roa')
if st.button('Calculate ROA'):
    roa = calculate_roa(net_income_roa, total_assets_roa)
    st.write(f'Return on Assets (ROA): {roa:.2f}%')

# Return on Equity (ROE)
st.subheader('Return on Equity (ROE)')
net_income_roe = st.number_input('Net Income', min_value=0.0, key='net_income_roe')
shareholders_equity_roe = st.number_input('Shareholders’ Equity', min_value=0.0, key='shareholders_equity_roe')
if st.button('Calculate ROE'):
    roe = calculate_roe(net_income_roe, shareholders_equity_roe)
    st.write(f'Return on Equity (ROE): {roe:.2f}%')

# Leverage Ratios
st.header('Leverage Ratios')

# Debt-to-Equity Ratio
st.subheader('Debt-to-Equity Ratio')
total_liabilities = st.number_input('Total Liabilities', min_value=0.0, key='total_liabilities')
shareholders_equity_de = st.number_input('Shareholders’ Equity', min_value=0.0, key='shareholders_equity_de')
if st.button('Calculate Debt-to-Equity Ratio'):
    debt_to_equity_ratio = calculate_debt_to_equity_ratio(total_liabilities, shareholders_equity_de)
    st.write(f'Debt-to-Equity Ratio: {debt_to_equity_ratio:.2f}')

# Debt Ratio
st.subheader('Debt Ratio')
total_liabilities_dr = st.number_input('Total Liabilities', min_value=0.0, key='total_liabilities_dr')
total_assets_dr = st.number_input('Total Assets', min_value=0.0, key='total_assets_dr')
if st.button('Ca


