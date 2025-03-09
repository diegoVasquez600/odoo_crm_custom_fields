odoo.define('odoo_crm_custom_fields.conditional_field', function (require) {
    "use strict";

    // Import base field widgets
    var FieldText = require('web.basic_fields').FieldText;
    var FieldDate = require('web.basic_fields').FieldDate;
    var fieldRegistry = require('web.field_registry');

    /**
     * Widget for x_operation_details (Text) depending on x_has_been_operated (Boolean).
     */
    var ConditionalTextField = FieldText.extend({
        /**
         * Called when the widget is first mounted.
         */
        start: function () {
            this._super.apply(this, arguments);
            // Show or hide the field based on the current value of x_has_been_operated
            this.toggle_visibility();
            return Promise.resolve();
        },

        /**
         * Called automatically by Odoo whenever a field in the same form changes.
         */
        _onFieldChanged: function (event) {
            // Let the parent handle the standard behavior
            this._super.apply(this, arguments);

            // If x_has_been_operated was changed, update visibility
            if (event.data.changes.x_has_been_operated !== undefined) {
                this.toggle_visibility();
            }
        },

        /**
         * Logic to show/hide the field depending on x_has_been_operated.
         */
        toggle_visibility: function () {
            // record.data contains the current record's data
            if (!this.record.data.x_has_been_operated) {
                this.$el.hide();
            } else {
                this.$el.show();
            }
        },
    });

    /**
     * Widget for x_appointment_date (Date) depending on x_has_appointment (Boolean).
     */
    var ConditionalDateField = FieldDate.extend({
        start: function () {
            this._super.apply(this, arguments);
            this.toggle_visibility();
            return Promise.resolve();
        },

        _onFieldChanged: function (event) {
            this._super.apply(this, arguments);
            // If x_has_appointment changed, update visibility
            if (event.data.changes.x_has_appointment !== undefined) {
                this.toggle_visibility();
            }
        },

        toggle_visibility: function () {
            if (!this.record.data.x_has_appointment) {
                this.$el.hide();
            } else {
                this.$el.show();
            }
        },
    });

    // Register the custom widgets in the field registry
    fieldRegistry.add('conditional_text', ConditionalTextField);
    fieldRegistry.add('conditional_date', ConditionalDateField);
});
