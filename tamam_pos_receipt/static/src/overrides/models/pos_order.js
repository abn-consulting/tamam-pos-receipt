import { PosOrder } from "@point_of_sale/app/models/pos_order";
import { patch } from "@web/core/utils/patch";

patch(PosOrder.prototype, {
    export_for_printing(baseUrl, headerData) {
        const data = super.export_for_printing(...arguments);
        return {
            ...data,
            till_number: this.config.till_number || false,
            pos_config_name: this.config.name || false,
        };
    },
});
