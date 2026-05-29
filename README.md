# Tamam POS Receipt Repo

This repository contains the Odoo addon in [`tamam_pos_receipt/`](./tamam_pos_receipt).

The module customizes the Odoo 19 POS receipt for Tamam by:

- adding `Receipt no` before the receipt number
- centering `Pro forma receipt`
- adding a POS-specific till number field
- printing the standard Odoo footer message below the till number
- centering the POS name
- removing `Powered by Odoo`

Deploy the addon folder `tamam_pos_receipt` to Odoo.sh through your project repository or as a Git submodule.
