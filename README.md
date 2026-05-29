# Tamam POS Receipt

This addon customizes the Odoo 19 restaurant POS receipt with a small, targeted set of changes:

- adds `Receipt no` before the tracking number
- keeps the receipt number smaller and non-bold
- centers the `Pro forma receipt` label
- adds a POS-specific `Till Number` field
- prints the till number above the standard POS footer text
- keeps the standard receipt footer placeholder for the custom message
- centers the POS name at the bottom
- removes `Powered by Odoo`

## Configuration

1. Install the addon.
2. Open `Point of Sale > Configuration > Settings`.
3. Select the target POS at the top of the settings page.
4. In `Bills & Receipts`, set `Till Number`.
5. If needed, enable `Custom Header & Footer` and use the standard `Footer` field for the message below the till number.

The till number is stored per POS configuration.
