# Market-recommendation-system


An AI-powered recommendation engine for online marketplaces that learns from user behavior and provides personalized product suggestions.

## Overview

This system implements a multi-dimensional recommendation algorithm that combines demographic profiling with behavioral learning. The engine uses purchase patterns and sophisticated scoring mechanisms to adapt to user preferences over time, without relying on browsing history.

## Features

- **Smart Recommendations:** Multi-dimensional scoring system that learns from user purchases
- **Adaptive Learning:** System reduces stereotype influence as it learns actual user preferences
- **1000+ Products:** Comprehensive catalog across 29 product categories
- **User Profiles:** Dynamic preference tracking with age, gender, and location factors
- **Purchase History:** Complete transaction tracking and analytics
- **Seller Marketplace:** Users can list their own products for sale
- **Privacy-Focused:** No browsing history tracking - only actual purchases inform recommendations

## Installation

### Prerequisites
- Python 3.7 or higher

### Setup
```bash
# Clone the repository
git clone https://github.com/IanKon/Market-recommendation-system.git
cd Market-recommendation-system

# Install dependencies
pip install openpyxl

# Run the system
python3 recommendation_system.py
```

## Usage

### Main Menu Options
1. **Register** - Create a new user account
2. **Login** - Access existing account
3. **Browse Products** - View personalized recommendations
4. **Search** - Find specific products
5. **My Profile** - View preference evolution and statistics
6. **Purchase History** - Track all past purchases
7. **Add Product** - List items for sale
8. **Manage Listings** - Edit your product listings

### Running the Demo
```bash
python3 demo.py
```
See an automated demonstration of the system learning from user purchases.

## How It Works

### Recommendation Algorithm

The system uses a multi-layered scoring approach:

1. **Initial Profile Generation**
   - Creates demographic-based preferences (age, location)
   - Generates initial scores for 29 product categories
   - Establishes baseline criteria preferences (quality, price, delivery)

2. **Behavioral Learning**
   - Updates preferences based on actual purchases
   - Strengthens connections between related products via tags
   - Gradually reduces demographic influence as behavior data accumulates

3. **Score Calculation**
   ```
   Final Score = demographic_score × initial_influence +
                 behavioral_score × (1 - initial_influence) +
                 tag_bonus + seasonal_bonus + exploration_bonus
   ```

4. **Diversity Mechanisms**
   - Exploration bonus prevents echo chambers
   - Tag-based connections suggest related products
   - Seasonal adjustments for time-relevant recommendations

### Learning Process

- **Initial Influence** starts at 100% (demographic-based)
- Decreases by 5% with each purchase
- Reaches minimum of 10% after 18 purchases
- Ensures system always maintains some demographic context while primarily using behavioral data

## Product Categories

29 distinct categories including:
- Gaming
- Sports and Health
- Clothing and Footwear
- Electronics
- Home and Living
- Tools and Repair
- Auto Products
- Pet Products
- Kitchen Products
- And 20 more...

## Data Structure

### User Profile
```json
{
  "username": "string",
  "age": "integer",
  "gender": "string",
  "location": "string",
  "balance": "float",
  "sphere_scores": {},
  "criteria_scores": {},
  "tag_scores": {},
  "purchase_history": [],
  "initial_influence": "float"
}
```

### Product
```json
{
  "id": "integer",
  "name": "string",
  "sphere": "string",
  "type": "string",
  "price": "float",
  "quality": "premium|medium|budget",
  "price_level": "expensive|average|cheap",
  "delivery": "1day|2-3days|4+days",
  "tags": [],
  "owner": "string"
}
```

## File Structure

```
project/
├── recommendation_system.py    # Main system implementation
├── demo.py                     # Demonstration script
├── products.json               # Product database
├── users.json                  # User accounts
└── transactions.json           # Transaction history
```

## Technical Details

### Performance
- Recommendation generation: <100ms for 30 products
- Profile update: <10ms per purchase
- Memory usage: ~50MB for full catalog

### Key Algorithms
- **Normalization:** Prevents score inflation over time
- **Exploration Bonus:** Ensures recommendation diversity
- **Tag Matching:** Creates connections between related products
- **Seasonal Effects:** Time-based category boosts

## Design Philosophy

### Privacy-Focused
No browsing history tracking - only actual purchases inform the system. This respects user privacy while focusing on genuine purchasing intent.

### Gender-Neutral
Algorithm treats all users equally regardless of gender, focusing on individual behavior over demographic stereotypes.

### Adaptive Learning
System starts with demographic assumptions but quickly adapts to actual user behavior, ensuring personalized recommendations without extensive initial data.

## Technology Stack

- **Language:** Python 3.12
- **Data Storage:** JSON
- **Dependencies:** openpyxl (for Excel import)
- **Interface:** Terminal-based CLI

## Author

**Ian Kononenko**

## License

Available for educational and personal use.
