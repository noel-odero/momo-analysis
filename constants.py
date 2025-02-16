TABLE_CONFIG = {
    'incoming_money': 'You have received',
    'payment_to_code_holders': 'Your payment of',
    'transfers_to_mobile_numbers': 'transferred to',
    'bank_transfers': 'You have transferred',
    'internet_voice_bundle': 'Bundles and Packs',
    'cash_power_bill_payments': 'MTN Cash Power',
    'transtxns_initiate_by_third_parties': 'Message from debit receiver',
    'withdrawals_from_agents': 'withdrawn',
    'airtime': 'to Airtime with token',
}

TABLE_SCHEMA = {
    'incoming_money': ['amount_received', 'sender', 'date', 'time', 'new_balance', 'transaction_id'],
    'payment_to_code_holders': ['amount_paid', 'recipient', 'date', 'time', 'new_balance', 'transaction_id', 'payment_code'],
    'transfers_to_mobile_numbers': ['amount_transferred', 'recipient', 'recipient_number', 'date', 'time', 'fee', 'new_balance', 'transaction_id'],
    'bank_transfers': ['amount_transferred', 'recipient', 'date', 'time', 'fee', 'new_balance', 'transaction_id', 'bank_name'],
    'internet_voice_bundle': ['date', 'time', 'new_balance', 'transaction_id', 'amount'],
    'cash_power_bill_payments': ['date', 'time', 'new_balance', 'transaction_id', 'amount', 'token'],
    'transtxns_initiate_by_third_parties': ['date', 'time', 'new_balance', 'transaction_amount', 'transaction_initiator', 'financial_transaction_id', 'external_transaction_id'],
    'withdrawals_from_agents': ['date', 'time', 'new_balance', 'transaction_id', 'amount', 'agent_name', 'agent_number', 'fee'],
    'airtime': ['date', 'time', 'new_balance', 'transaction_id', 'amount'],
}