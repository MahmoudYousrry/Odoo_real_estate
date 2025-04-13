### 🏢 Real Estate Management Module for Odoo 18

A custom **Odoo 18** module designed to streamline real estate management operations. This module provides a robust and flexible platform for handling properties, owners, sales, partnerships, tags, and property history tracking — all integrated seamlessly with the Odoo ERP system.

---

## 🚀 Features

- 🏘️ **Property Management**Create, view, update, and manage property details easily.
- 📈 **Property Sales Tracking**Track and manage property sales and sales orders.
- 👤 **Owner & Partner Management**Associate properties with owners and manage partner relationships.
- 📜 **Property History**Keep detailed logs of property history and status changes.
- 🏷️ **Tag System**Tag properties to enable quick categorization and search.
- 🧙 **Wizards**Interactive wizards like `Change State Wizard` to perform state transitions for properties efficiently.
- 📊 **Reports**Generate property reports with integrated XML templates.
- 🔐 **Security & Access Control**Define roles and permissions using CSV and XML security configurations.
- 🌐 **REST API Support**Expose APIs for external integrations via the `controllers` directory.
- 🧪 **Testing Support**Unit tests included to verify functionality (`tests/test_property.py`).


---
## 📁 Project Structure

```plaintext
real_estate/
├── controllers/    # REST API Controllers
├── data/           # Static data files (e.g., sequences)
├── i18n/           # Translation files
├── models/         # Business logic (Python models)
├── reports/        # QWeb XML Reports
├── security/       # Access control and security rules
├── static/         # Static files (images, JS, CSS)
├── tests/          # Unit tests
├── views/          # XML views and menus
└── wizard/         # Wizard logic and views
```

## 📦 Installation

1. Clone this repository into your Odoo custom addons path:

```shellscript
git clone https://github.com/your-username/real_estate.git
```


2. Restart the Odoo server:

```shellscript
./odoo-bin -d your-database -u real_estate
```


3. Activate Developer Mode in Odoo UI.
4. Install the Real Estate module from the Apps menu.


## 🛠️ Requirements

- Odoo 18
- Python 3.10+
- Required Python packages (managed by Odoo's environment)



## 📜 License

This project is licensed under the MIT License. See the LICENSE file for more details.



## 🌍 Localization

Currently supports English (default). Additional translations can be added in the i18n folder.
