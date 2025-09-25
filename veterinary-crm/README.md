# Veterinary CRM System

A comprehensive Customer Relationship Management (CRM) system designed specifically for veterinary practices. This web application allows veterinary clinics to manage customer information, pet records, and maintain organized databases of their clients and their beloved pets.

## Features

### Customer Management
- **Add New Customers**: Register new clients with complete contact information
- **Edit Customer Details**: Update customer information as needed
- **Customer Profiles**: Comprehensive view of customer details and their pets
- **Search Functionality**: Quickly find customers using the search feature
- **Delete Customers**: Remove customer records (with confirmation)

### Pet Management
- **Pet Registration**: Add pets with detailed information including:
  - Name, species, breed
  - Age, weight, color, gender
  - Microchip ID
  - Medical notes and special instructions
- **Pet Profiles**: Individual pet records with complete history
- **Edit Pet Information**: Update pet details as they grow and change
- **Multiple Pets per Customer**: Support for customers with multiple pets

### Database Features
- **SQLite Database**: Lightweight, file-based database for easy deployment
- **Relational Data**: Proper relationships between customers and pets
- **Data Integrity**: Foreign key constraints and validation
- **Timestamps**: Automatic creation and update timestamps

### User Interface
- **Modern Design**: Clean, responsive Bootstrap-based interface
- **Mobile Friendly**: Works on desktop, tablet, and mobile devices
- **Intuitive Navigation**: Easy-to-use navigation with clear visual hierarchy
- **Dashboard**: Overview of total customers, pets, and recent activity
- **Form Validation**: Client-side and server-side validation

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLAlchemy ORM with SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5
- **Icons**: Font Awesome
- **Responsive Design**: Mobile-first approach

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone or download the project**
   ```bash
   cd /Users/rosszeiger/CascadeProjects/veterinary-crm
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your web browser and navigate to `http://localhost:5000`

## Usage

### Getting Started

1. **Dashboard**: The main dashboard provides an overview of your customer base and recent activity
2. **Add Customer**: Click "Add New Customer" to register a new client
3. **Add Pets**: Once a customer is created, add their pets from the customer detail page
4. **Search**: Use the search functionality to quickly find customers
5. **Edit/Update**: Click edit buttons to modify customer or pet information

### Customer Workflow

1. **New Customer Registration**:
   - Navigate to "Add Customer"
   - Fill in required fields (name, email, phone)
   - Optionally add address
   - Save the customer

2. **Adding Pets**:
   - Go to the customer's detail page
   - Click "Add Pet"
   - Fill in pet information (name and species are required)
   - Add optional details like breed, age, weight, etc.
   - Save the pet record

3. **Managing Records**:
   - View all customers from the "Customers" page
   - Search for specific customers or pets
   - Edit information as needed
   - Delete records with confirmation prompts

## Database Schema

### Customers Table
- `id`: Primary key
- `first_name`: Customer's first name
- `last_name`: Customer's last name
- `email`: Email address (unique)
- `phone`: Phone number
- `address`: Physical address (optional)
- `created_at`: Registration timestamp
- `updated_at`: Last modification timestamp

### Pets Table
- `id`: Primary key
- `name`: Pet's name
- `species`: Type of animal (Dog, Cat, Bird, etc.)
- `breed`: Breed information (optional)
- `age`: Age in years (optional)
- `weight`: Weight in pounds (optional)
- `color`: Pet's color (optional)
- `gender`: Male/Female/Unknown (optional)
- `microchip_id`: Microchip identifier (optional)
- `notes`: Medical/behavioral notes (optional)
- `customer_id`: Foreign key to customers table
- `created_at`: Registration timestamp
- `updated_at`: Last modification timestamp

## API Endpoints

The application also provides JSON API endpoints:

- `GET /api/customers` - Get all customers
- `GET /api/customer/<id>` - Get specific customer with pets
- `GET /api/pets` - Get all pets

## Security Considerations

- Input validation on all forms
- SQL injection protection through SQLAlchemy ORM
- XSS protection through Jinja2 template escaping
- CSRF protection (can be enhanced with Flask-WTF)

## Customization

### Adding New Pet Species
Edit the species dropdown in `add_pet.html` and `edit_pet.html` templates.

### Styling Changes
Modify `static/css/style.css` to customize the appearance.

### Additional Fields
Add new fields to the database models in `models.py` and update the corresponding templates.

## Troubleshooting

### Common Issues

1. **Database not found**: The SQLite database is created automatically on first run
2. **Port already in use**: Change the port in `app.py` or stop other applications using port 5000
3. **Template not found**: Ensure all template files are in the `templates/` directory
4. **Static files not loading**: Check that static files are in the `static/` directory

### Development Mode

The application runs in debug mode by default, which provides:
- Automatic reloading on code changes
- Detailed error messages
- Interactive debugger

For production deployment, set `debug=False` in `app.py`.

## Future Enhancements

Potential features for future versions:
- Appointment scheduling
- Medical history tracking
- Vaccination records
- Photo uploads for pets
- Email notifications
- Reporting and analytics
- Multi-user support with authentication
- Backup and restore functionality

## Contributing

This is a basic CRM system that can be extended based on specific veterinary practice needs. Feel free to modify and enhance the codebase.

## License

This project is open source and available under the MIT License.

## Support

For questions or issues, please refer to the code comments and documentation within the application files.
