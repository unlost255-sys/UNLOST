# UNLOST - Lost and Found Management System

UNLOST is a centralized platform for reporting and recovering lost items on campus.

## Setup Instructions

### Prerequisites
- Python 3.x installed
- pip (Python package manager)

### Installation

1.  Navigate to the project directory:
    ```bash
    cd C:\Users\DAKSH\OneDrive\Documents\SD\UNLOST
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Initialize Database with Dummy Data (Optional):**
    ```bash
    python create_dummy_data.py
    ```

2.  **Start the Server:**
    ```bash
    python app.py
    ```

3.  **Access the Website:**
    Open your browser and verify the site at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Features
- **Report Lost/Found Items:** Submit details including images.
- **Search & Filter:** Find items by category, status, or date.
- **Responsive Design:** Works on mobile and desktop.
- **Contact Info:** Securely view contact details for items.
