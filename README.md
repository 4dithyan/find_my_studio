# Studio Booking System

A comprehensive Django-based web application for booking photography studios. This platform connects customers with photography studios, allowing seamless booking, package selection, and payment processing.

## Features

- **Multi-role authentication system**: Admin, Studio Owners, and Customers
- **Studio registration and verification**: Secure registration process with admin verification
- **Portfolio management**: Studios can showcase their work with multiple images per portfolio item
- **Package creation and management**: Studios can create and manage service packages with pricing
- **Booking system**: Customers can browse studios, view portfolios, select packages, and make bookings
- **Payment processing**: Integrated payment system with commission handling
- **Review and feedback system**: Customers can leave reviews and ratings
- **Geographic organization**: Organized by districts and locations
- **Analytics dashboard**: For admins to monitor activity and payments
- **Email notifications**: Automated email confirmations for various actions

## How the Website Works

### User Roles and Functions

1. **Admin Panel**:
   - Manage districts, locations, and categories
   - Verify studio registrations (Accept/Reject)
   - View all payments and generate reports
   - Monitor overall system activity

2. **Studio Owners**:
   - Register studio with profile, images, and ID proof
   - Add and manage portfolio works with multiple images
   - Create and manage service packages
   - Accept/reject booking requests
   - View payment history for their studio
   - Update studio information

3. **Customers**:
   - Register and create profile
   - Browse studios by location and category
   - View portfolios and packages
   - Book services and make payments
   - Leave feedback and ratings
   - Track booking status

### Workflow

1. **Studio Registration**: Studio owner fills registration form with details, uploads ID proof and studio image
2. **Admin Verification**: Admin reviews studio registrations and accepts/rejects them
3. **Customer Registration**: Customer fills registration form with personal details
4. **Browse Studios**: Customer selects district → location → studio
5. **View Services**: Customer browses categories → works → packages
6. **Book Package**: Customer selects package and fills booking details
7. **Request Status**: Studio accepts/rejects the booking request
8. **Payment**: Customer makes payment (initial 50% + additional charges if any)
9. **Confirmation**: Booking confirmed after payment

### Technical Architecture

The application consists of four main Django apps:

1. **Adminapp**: Administrative panel for managing districts, locations, categories, and studio verification
2. **Guestapp**: Handles user registration, login, and authentication for all user types
3. **Studioapp**: Studio dashboard for managing works, packages, and bookings
4. **Customerapp**: Customer interface for browsing studios, packages, and making bookings

### Database Structure

- **Authentication**: tbl_login manages user authentication and roles
- **Geographic**: tbl_district and tbl_location organize studios geographically
- **Services**: Tbl_category manages photography service categories
- **Users**: Tbl_studio and Tbl_customer store user profiles
- **Content**: Tbl_work, Tbl_workimage, and Tbl_package manage studio portfolios and packages
- **Transactions**: Tbl_request, Tbl_payment, and Tbl_feedback handle bookings and payments

## Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up the MySQL database:
   - Create a database named `findmystudio`
   - Import the `findmystudio.sql` file to populate the database
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```
   python manage.py runserver
   ```

## Configuration

The application uses MySQL database configured in settings.py. Ensure your MySQL server is running before starting the application.

## Contact

For support or inquiries, contact:
- Email: mailforadithyan@gmail.com
- Phone: 9778238064

## License

This project is licensed under the MIT License.