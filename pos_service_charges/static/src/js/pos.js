odoo.define('pos_service_charges', function (require) {
"use strict";

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const { useListener } = require('web.custom_hooks');
    const Registries = require('point_of_sale.Registries');

    class ServiceChargeButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this.onClick);
        }
        async onClick() {
            var self = this;
            const { confirmed, payload } = await this.showPopup('NumberPopup',{
                title: this.env._t('Discount Percentage'),
                startingValue: this.env.pos.config.default_charge,
            });
            if (confirmed) {
                const val = Math.round(Math.max(0,Math.min(100,parseFloat(payload))));
                await self.apply_service_charge(val);
            }
        }

        async apply_service_charge(pc) {
            var order    = this.env.pos.get_order();
            var lines    = order.get_orderlines();
            var product  = this.env.pos.db.get_product_by_id(this.env.pos.config.service_product_id[0]);
            if (product === undefined) {
                await this.showPopup('ErrorPopup', {
                    title : this.env._t("No Service product found"),
                    body  : this.env._t("The Service product seems misconfigured. Make sure it is flagged as 'Can be Sold' and 'Available in Point of Sale'."),
                });
                return;
            }

            // Remove existing discounts
            var i = 0;
            while ( i < lines.length ) {
                if (lines[i].get_product() === product) {
                    order.remove_orderline(lines[i]);
                } else {
                    i++;
                }
            }
	        var service = pc;
	        if(this.env.pos.config.charges_type == 'percent'){
	          var service =  pc / 100.0 * order.get_total_without_tax();
	        }

	        if( service > 0 ){
	            order.add_product(product, { price: service });
	        }
        }
    }
    ServiceChargeButton.template = 'ServiceChargeButton';

    ProductScreen.addControlButton({
        component: ServiceChargeButton,
        condition: function() {
            return this.env.pos.config.allow_service_charge && this.env.pos.config.service_product_id;
        },
    });

    Registries.Component.add(ServiceChargeButton);
});
