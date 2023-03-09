import frappe


@frappe.whitelist()
def update_stock_ledger(entry_name,source_TT=None,target_TT=None,source_WH=None,target_WH=None):
    StockLedgers = frappe.get_all("Stock Ledger Entry", filters = {"voucher_no":entry_name})
    print(source_WH)
    if source_TT and target_TT is not None:
        for ledger in StockLedgers:
            if source_WH == None or target_WH == None:
                frappe.set_value("Stock Ledger Entry",ledger.name,"transaction_type",source_TT)
            else:
                record = frappe.get_doc("Stock Ledger Entry",ledger.name)
                if record.warehouse == source_WH:
                    frappe.set_value("Stock Ledger Entry",ledger.name,"transaction_type",source_TT)
                if record.warehouse == target_WH:
                    frappe.set_value("Stock Ledger Entry",ledger.name,"transaction_type",target_TT)
    return StockLedgers