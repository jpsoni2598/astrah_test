# Astrah Test Module

Odoo 19 custom module created as part of the Astrah OS technical evaluation.

### ✔ Custom Model
A new model `astrah.lead` is added with the following fields:
- `name` (Char, required)
- `customer_name` (Char)
- `value` (Float)
- `priority` (Selection: Low/Medium/High)
- `description` (Text)

### ✔ Menu + Action + Views
You can access the module via:
CRM → Astrah Test Leads

From this menu, a tree view opens and records can be created and edited in the form view.


### ✔ Tailwind CSS Integration
The form view has been styled using Tailwind utility classes including:
- Grid layout (`grid`, `grid-cols-*`)
- Spacing (`mt-*`, `gap-*`, `px-*`)
- Typography (`text-*`, `font-*`)

Tailwind CSS has been initialized **locally** inside the module and bundled into Odoo backend assets.

---

## Tailwind Build Instructions

If new classes are added in the XML views, regenerate the Tailwind bundle:

```bash
# Install dependencies (first time only)
npm install -D tailwindcss @tailwindcss/cli

# Rebuild Tailwind output when XML/CSS changes
npx @tailwindcss/cli \
  -i ./static/src/css/tailwind.input.css \
  -o ./static/src/css/tailwind.bundle.css \
  --minify