# Astrah Test – Odoo 19 Module

Custom module delivered for the Astrah OS paid test task. It demonstrates a clean ORM model, Tailwind-styled backend views, and an OWL component rendered inside the lead form via a backend widget.

## 1. Installation & Setup

1. Copy the `astrah_test` directory into your Odoo 19 `addons_path`.
2. (Optional but recommended) Remove `node_modules/` if you do not plan to rebuild the Tailwind bundle—it is only required for development.
3. Update the app list from **Apps → Update Apps List**.
4. Install **Astrah Test**.
5. Enable `--dev=assets` while developing so Tailwind/CSS rebuilds are reloaded automatically.

## 2. Module Structure

| Path | Purpose |
| --- | --- |
| `models/lead.py` | Declares `astrah.lead` with the required CRM-like fields. |
| `views/lead_form.xml` | Tree + form view with Tailwind layout and widget placeholder. |
| `views/menus.xml` | Adds **CRM → Astrah Test Leads** menu/action. |
| `static/src/css/tailwind.css` | Compiled Tailwind bundle loaded in `web.assets_backend`. |
| `static/src/css/tailwind.input.css` | Source file containing `@tailwind` directives; used only during builds. |
| `tailwind.config.cjs` | Build config that scans our XML/JS templates to include only the classes we use. |
| `static/src/js/test_component.js` | Registers the OWL component and exposes it as a form widget. |
| `static/src/xml/test_component.xml` | Component template displaying “Astrah Test Component Loaded”. |
| `security/ir.model.access.csv` | CRUD access for `astrah.lead` to `base.group_user`. |
| `README.md` | This document with installation, testing, and delivery notes. |

## 3. Tailwind Workflow

The client requested Tailwind to load through backend assets, but shipping the entire Tailwind CDN build would add unnecessary weight to every backend view. To keep the UI fast we only ship the classes that appear in our XML/OWL templates. The repo therefore contains two CSS files:

- `static/src/css/tailwind.css`: the trimmed, production-ready bundle that Odoo actually loads.
- `static/src/css/tailwind.input.css`: a tiny source file (`@import "tailwindcss"; @source "../**/*.xml";`) used alongside `tailwind.config.cjs` to regenerate the bundle when new Tailwind classes are introduced.

If you add more Tailwind utilities in XML/JS, run the command below from the module root to rebuild the optimized bundle:

```bash
npx tailwindcss -c tailwind.config.cjs \
  -i static/src/css/tailwind.input.css \
  -o static/src/css/tailwind.css \
  --minify
```

Keeping the config + input file in the repository documents how the bundle was produced and lets reviewers verify that the delivered `tailwind.css` is reproducible.

## 4. OWL Component Placement

The spec asked to “render the component inside the form view using `t-component`”. In practice, backend form views (the ones defined inside `ir.ui.view` XML records) do not parse OWL templates directly; only QWeb templates are evaluated with `t-component`. Attempting to drop `<t t-component="..."/>` inside the form would leave the markup untouched and nothing would render.

To satisfy the visual requirement inside the actual form we register our OWL component as a backend widget instead:

1. `static/src/js/test_component.js` registers `"astrah_test_ping_console"` in the `view_widgets` registry and points it to the OWL component.
2. `static/src/xml/test_component.xml` defines the template with the text “Astrah Test Component Loaded” and a “Ping Console” button (`t-on-click="pingConsole"`).
3. The form view inserts `<widget name="astrah_test_ping_console" class="d-inline-block"/>`, which is how backend forms load widget components. Clicking the button logs to the console as required.

This approach keeps the component inside the form view while respecting the technical limitations of `t-component`.