odoo.define('odoo_crm_custom.conditional_field', function (require) {
    "use strict";


    var FieldText = require('web.basic_fields').FieldText;
    var FieldDate = require('web.basic_fields').FieldDate;
    var fieldRegistry = require('web.field_registry');


    // Widget for the field x_operation_details
    var CondtionalTextField = FieldText.extend({
        start: function () {
            this._super.apply(this, arguments);
            this._toggle_visibility();
            return Promise.resolve();
        },
        _toggle_visibility: function () {
            var value = this.recordData.x_has_been_operated;
            if (value) {
                this.$el.show();
            } else {
                this.$el.hide();
            }
        } 
    });


    // Widget for the field x_appointment_date
    var ConditionalDateField = FieldDate.extend({
        start: function () {
            this._super.apply(this, arguments);
            this._toggle_visibility();
            return Promise.resolve();
        },
        _toggle_visibility: function () {
            var value = this.recordData.x_has_appointment;
            if (value) {
                this.$el.show();
            } else {
                this.$el.hide();
            }
        } 
    });

    fieldRegistry.add('conditional_text', CondtionalTextField);
    fieldRegistry.add('conditional_date', ConditionalDateField);

});
