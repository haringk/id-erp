frappe.ui.form.on('Sales Order', {
    refresh: function(frm) {
        frm.fields_dict.items.grid.add_custom_button(__('Add Optional'), function() {
            frappe.msgprint(__('Implement optional selection here'));  
        });
    }
});
