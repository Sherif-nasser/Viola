frappe.ui.form.on('Stock Entry', {
    // refresh:function(frm){
    //     console.log(frm.doc.name);
    // },
    before_save:function(frm){
        if (frm.doc.transaction_type = 'Receipt'){
            frm.set_value("transaction_type_2","Return")
        }
        if (frm.doc.transaction_type = 'Return'){
            frm.set_value("transaction_type_2","Receipt")
        }
        if (frm.doc.transaction_type = 'To Branch'){
            frm.set_value("transaction_type_2","From Branch")
        }
        if (frm.doc.transaction_type = 'From Branch'){
            frm.set_value("transaction_type_2","To Branch")
        }
        // var source = frm.doc.from_warehouse;
        // console.log(source);
        // frm.set_value("from_warehouse",source);
    },
    on_submit:function(frm){
        
        frappe.call({
            method:"viola.violaController.viola.update_stock_ledger",
            args:{
             entry_name : frm.doc.name,
             source_WH: frm.doc.from_warehouse,
             target_WH:frm.doc.to_warehouse,
             source_TT : frm.doc.transaction_type,
             target_TT: frm.doc.transaction_type_2
            },
            callback: function(r) {
                console.log(r.message);
            },
        })
    }
});