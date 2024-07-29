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
if st.button('Calculate Current Ratio', key='current_ratio_btn'):
    current_ratio = calculate_current_ratio(current_assets, current_liabilities)
    st.write(f'Current Ratio: {current_ratio:.2f}')

# Quick Ratio
st.subheader('Quick Ratio')
quick_assets = st.number_input('Current Assets', min_value=0.0, key='quick_assets')
inventory = st.number_input('Inventory', min_value=0.0, key='inventory')
quick_liabilities = st.number_input('Current Liabilities', min_value=0.0, key='quick_liabilities')
if st.button('Calculate Quick Ratio', key='quick_ratio_btn'):
    quick_ratio = calculate_quick_ratio(quick_assets, inventory, quick_liabilities)
    st.write(f'Quick Ratio: {quick_ratio:.2f}')

# Cash Ratio
st.subheader('Cash Ratio')
cash_and_equivalents = st.number_input('Cash and Cash Equivalents', min_value=0.0, key='cash_and_equivalents')
cash_liabilities = st.number_input('Current Liabilities', min_value=0.0, key='cash_liabilities')
if st.button('Calculate Cash Ratio', key='cash_ratio_btn'):
    cash_ratio = calculate_cash_ratio(cash_and_equivalents, cash_liabilities)
    st.write(f'Cash Ratio: {cash_ratio:.2f}')

# Profitability Ratios
st.header('Profitability Ratios')

# Gross Profit Margin
st.subheader('Gross Profit Margin')
gross_profit = st.number_input('Gross Profit', min_value=0.0, key='gross_profit')
revenue = st.number_input('Revenue', min_value=0.0, key='revenue')
if st.button('Calculate Gross Profit Margin', key='gross_profit_margin_btn'):
    gross_profit_margin = calculate_gross_profit_margin(gross_profit, revenue)
    st.write(f'Gross Profit Margin: {gross_profit_margin:.2f}%')

# Operating Profit Margin
st.subheader('Operating Profit Margin')
operating_income = st.number_input('Operating Income', min_value=0.0, key='operating_income')
revenue_op = st.number_input('Revenue', min_value=0.0, key='revenue_op')
if st.button('Calculate Operating Profit Margin', key='operating_profit_margin_btn'):
    operating_profit_margin = calculate_operating_profit_margin(operating_income, revenue_op)
    st.write(f'Operating Profit Margin: {operating_profit_margin:.2f}%')

# Net Profit Margin
st.subheader('Net Profit Margin')
net_income = st.number_input('Net Income', min_value=0.0, key='net_income')
revenue_np = st.number_input('Revenue', min_value=0.0, key='revenue_np')
if st.button('Calculate Net Profit Margin', key='net_profit_margin_btn'):
    net_profit_margin = calculate_net_profit_margin(net_income, revenue_np)
    st.write(f'Net Profit Margin: {net_profit_margin:.2f}%')

# Return on Assets (ROA)
st.subheader('Return on Assets (ROA)')
net_income_roa = st.number_input('Net Income', min_value=0.0, key='net_income_roa')
total_assets_roa = st.number_input('Total Assets', min_value=0.0, key='total_assets_roa')
if st.button('Calculate ROA', key='roa_btn'):
    roa = calculate_roa(net_income_roa, total_assets_roa)
    st.write(f'Return on Assets (ROA): {roa:.2f}%')

# Return on Equity (ROE)
st.subheader('Return on Equity (ROE)')
net_income_roe = st.number_input('Net Income', min_value=0.0, key='net_income_roe')
shareholders_equity_roe = st.number_input('Shareholders’ Equity', min_value=0.0, key='shareholders_equity_roe')
if st.button('Calculate ROE', key='roe_btn'):
    roe = calculate_roe(net_income_roe, shareholders_equity_roe)
    st.write(f'Return on Equity (ROE): {roe:.2f}%')

# Leverage Ratios
st.header('Leverage Ratios')

# Debt-to-Equity Ratio
st.subheader('Debt-to-Equity Ratio')
total_liabilities = st.number_input('Total Liabilities', min_value=0.0, key='total_liabilities')
shareholders_equity_de = st.number_input('Shareholders’ Equity', min_value=0.0, key='shareholders_equity_de')
if st.button('Calculate Debt-to-Equity Ratio', key='debt_to_equity_ratio_btn'):
    debt_to_equity_ratio = calculate_debt_to_equity_ratio(total_liabilities, shareholders_equity_de)
    st.write(f'Debt-to-Equity Ratio: {debt_to_equity_ratio:.2f}')

# Debt Ratio
st.subheader('Debt Ratio')
total_liabilities_dr = st.number_input('Total Liabilities', min_value=0.0, key='total_liabilities_dr')
total_assets_dr = st.number_input('Total Assets', min_value=0.0, key='total_assets_dr')
if st.button('Calculate Debt Ratio', key='debt_ratio_btn'):
    debt_ratio = calculate_debt_ratio(total_liabilities_dr, total_assets_dr)
    st.write(f'Debt Ratio: {debt_ratio:.2f}')

# Interest Coverage Ratio
st.subheader('Interest Coverage Ratio')
operating_income_ic = st.number_input('Operating Income', min_value=0.0, key='operating_income_ic')
interest_expense_ic = st.number_input('Interest Expense', min_value=0.0, key='interest_expense_ic')
if st.button('Calculate Interest Coverage Ratio', key='interest_coverage_ratio_btn'):
    interest_coverage_ratio = calculate_interest_coverage_ratio(operating_income_ic, interest_expense_ic)
    st.write(f'Interest Coverage Ratio: {interest_coverage_ratio:.2f}')

# Efficiency Ratios
st.header('Efficiency Ratios')

# Asset Turnover Ratio
st.subheader('Asset Turnover Ratio')
revenue_at = st.number_input('Revenue', min_value=0.0, key='revenue_at')
total_assets_at = st.number_input('Total Assets', min_value=0.0, key='total_assets_at')
if st.button('Calculate Asset Turnover Ratio', key='asset_turnover_ratio_btn'):
    asset_turnover_ratio = calculate_asset_turnover_ratio(revenue_at, total_assets_at)
    st.write(f'Asset Turnover Ratio: {asset_turnover_ratio:.2f}')

# Inventory Turnover Ratio
st.subheader('Inventory Turnover Ratio')
cogs_it = st.number_input('Cost of Goods Sold (COGS)', min_value=0.0, key='cogs_it')
average_inventory_it = st.number_input('Average Inventory', min_value=0.0, key='average_inventory_it')
if st.button('Calculate Inventory Turnover Ratio', key='inventory_turnover_ratio_btn'):
    inventory_turnover_ratio = calculate_inventory_turnover_ratio(cogs_it, average_inventory_it)
    st.write(f'Inventory Turnover Ratio: {inventory_turnover_ratio:.2f}')

# Receivables Turnover Ratio
st.subheader('Receivables Turnover Ratio')
revenue_rt = st.number_input('Revenue', min_value=0.0, key='revenue_rt')
average_accounts_receivable_rt = st.number_input('Average Accounts Receivable', min_value=0.0, key='average_accounts_receivable_rt')
if st.button('Calculate Receivables Turnover Ratio', key='receivables_turnover_ratio_btn'):
    receivables_turnover_ratio = calculate_receivables_turnover_ratio(revenue_rt, average_accounts_receivable_rt)
    st.write(f'Receivables Turnover Ratio: {receivables_turnover_ratio:.2f}')

# Market Valuation Ratios
st.header('Market Valuation Ratios')

# Price-to-Earnings (P/E) Ratio
st.subheader('Price-to-Earnings (P/E) Ratio')
market_price_per_share_pe = st.number_input('Market Price per Share', min_value=0.0, key='market_price_per_share_pe')
earnings_per_share_pe = st.number_input('Earnings per Share (EPS)', min_value=0.0, key='earnings_per_share_pe')
if st.button('Calculate P/E Ratio', key='pe_ratio_btn'):
    pe_ratio = calculate_pe_ratio(market_price_per_share_pe, earnings_per_share_pe)
    st.write(f'P/E Ratio: {pe_ratio:.2f}')

# Price-to-Book (P/B) Ratio
st.subheader('Price-to-Book (P/B) Ratio')
market_price_per_share_pb = st.number_input('Market Price per Share', min_value=0.0, key='market_price_per_share_pb')
book_value_per_share_pb = st.number_input('Book Value per Share', min_value=0.0, key='book_value_per_share_pb')
if st.button('Calculate P/B Ratio', key='pb_ratio_btn'):
    pb_ratio = calculate_pb_ratio(market_price_per_share_pb, book_value_per_share_pb)
    st.write(f'P/B Ratio: {pb_ratio:.2f}')

# Dividend Yield
st.subheader('Dividend Yield')
annual_dividends_per_share_dy = st.number_input('Annual Dividends per Share', min_value=0.0, key='annual_dividends_per_share_dy')
market_price_per_share_dy = st.number_input('Market Price per Share', min_value=0.0, key='market_price_per_share_dy')
if st.button('Calculate Dividend Yield', key='dividend_yield_btn'):
    dividend_yield = calculate_dividend_yield(annual_dividends_per_share_dy, market_price_per_share_dy)
    st.write(f'Dividend Yield: {dividend_yield:.2f}')

# Investment Performance Ratios
st.header('Investment Performance Ratios')

# Sharpe Ratio
st.subheader('Sharpe Ratio')
portfolio_return_sr = st.number_input('Portfolio Return', min_value=0.0, key='portfolio_return_sr')
risk_free_rate_sr = st.number_input('Risk-Free Rate', min_value=0.0, key='risk_free_rate_sr')
std_deviation_portfolio_return_sr = st.number_input('Standard Deviation of Portfolio Return', min_value=0.0, key='std_deviation_portfolio_return_sr')
if st.button('Calculate Sharpe Ratio', key='sharpe_ratio_btn'):
    sharpe_ratio = calculate_sharpe_ratio(portfolio_return_sr, risk_free_rate_sr, std_deviation_portfolio_return_sr)
    st.write(f'Sharpe Ratio: {sharpe_ratio:.2f}')

# Jensen's Alpha
st.subheader("Jensen's Alpha")
portfolio_return_ja = st.number_input('Portfolio Return', min_value=0.0, key='portfolio_return_ja')
risk_free_rate_ja = st.number_input('Risk-Free Rate', min_value=0.0, key='risk_free_rate_ja')
beta_ja = st.number_input('Beta (β)', min_value=0.0, key='beta_ja')
market_return_ja = st.number_input('Market Return', min_value=0.0, key='market_return_ja')
if st.button('Calculate Jensen\'s Alpha', key='jensens_alpha_btn'):
    jensens_alpha = calculate_jensens_alpha(portfolio_return_ja, risk_free_rate_ja, beta_ja, market_return_ja)
    st.write(f"Jensen's Alpha: {jensens_alpha:.2f}")

# Activity Ratios
st.header('Activity Ratios')

# Accounts Receivable Turnover Ratio
st.subheader('Accounts Receivable Turnover Ratio')
net_credit_sales_art = st.number_input('Net Credit Sales', min_value=0.0, key='net_credit_sales_art')
average_accounts_receivable_art = st.number_input('Average Accounts Receivable', min_value=0.0, key='average_accounts_receivable_art')
if st.button('Calculate Accounts Receivable Turnover Ratio', key='accounts_receivable_turnover_ratio_btn'):
    accounts_receivable_turnover = calculate_accounts_receivable_turnover(net_credit_sales_art, average_accounts_receivable_art)
    st.write(f'Accounts Receivable Turnover: {accounts_receivable_turnover:.2f}')

# Working Capital Ratio
st.subheader('Working Capital Ratio')
net_sales_wcr = st.number_input('Net Sales', min_value=0.0, key='net_sales_wcr')
working_capital_wcr = st.number_input('Working Capital', min_value=0.0, key='working_capital_wcr')
if st.button('Calculate Working Capital Ratio', key='working_capital_ratio_btn'):
    working_capital_ratio = calculate_working_capital_ratio(net_sales_wcr, working_capital_wcr)
    st.write(f'Working Capital Ratio: {working_capital_ratio:.2f}')

# Asset Turnover Ratio
st.subheader('Asset Turnover Ratio')
sales_atr = st.number_input('Sales', min_value=0.0, key='sales_atr')
average_total_assets_atr = st.number_input('Average Total Assets', min_value=0.0, key='average_total_assets_atr')
if st.button('Calculate Asset Turnover Ratio', key='asset_turnover_ratio_sales_btn'):
    asset_turnover_ratio_sales = calculate_asset_turnover_ratio_sales(sales_atr, average_total_assets_atr)
    st.write(f'Asset Turnover Ratio: {asset_turnover_ratio_sales:.2f}')

# Days Payable Outstanding Ratio
st.subheader('Days Payable Outstanding Ratio')
accounts_payable_dpo = st.number_input('Accounts Payable', min_value=0.0, key='accounts_payable_dpo')
cost_of_sales_dpo = st.number_input('Cost of Sales', min_value=0.0, key='cost_of_sales_dpo')
number_of_days_dpo = st.number_input('Number of Days', min_value=1.0, key='number_of_days_dpo')
if st.button('Calculate Days Payable Outstanding Ratio', key='days_payable_outstanding_ratio_btn'):
    days_payable_outstanding = calculate_days_payable_outstanding(accounts_payable_dpo, cost_of_sales_dpo, number_of_days_dpo)
    st.write(f'Days Payable Outstanding: {days_payable_outstanding:.2f} days')

# Running the app
if __name__ == '__main__':
    st.title("Financial Ratio Calculator")
