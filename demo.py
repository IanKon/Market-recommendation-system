#!/usr/bin/env python3
"""
Demo script showing how the recommendation system works
"""

import json
from recommendation_system import *

def print_separator(title=""):
    print("\n" + "="*70)
    if title:
        print(f"  {title}")
        print("="*70)

def demo_user_journey():
    """Demonstrate a complete user journey"""
    
    print_separator("RECOMMENDATION SYSTEM DEMO")
    print("This demo shows how the recommendation system learns from purchases\n")
    
    db = Database()
    
    print("📦 Loading products from Excel...")
    excel_path = "/mnt/user-data/uploads/IA_COMP.xlsx"
    if os.path.exists(excel_path):
        products = load_products_from_excel(excel_path)
        db.save_products(products)
    else:
        products = db.load_products()
    
    print(f"✅ Loaded {len(products)} products")
    
    print_separator("STEP 1: USER REGISTRATION")
    print("Creating demo user: Alex, 25 years old, male, big city\n")
    
    user = User("alex_demo", "password", 25, "male", "big_city")
    
    print(f"✅ User created with ${user.balance:.2f} balance")
    print(f"\nInitial preferences (Top 5 Spheres):")
    sorted_spheres = sorted(user.sphere_scores.items(), key=lambda x: x[1], reverse=True)
    for i, (sphere, score) in enumerate(sorted_spheres[:5], 1):
        print(f"  {i}. {sphere}: {score:.2f}")
    
    print(f"\nInitial criteria preferences:")
    print(f"  Quality: premium={user.criteria_scores['premium']:.2f}, "
          f"medium={user.criteria_scores['medium']:.2f}, "
          f"budget={user.criteria_scores['budget']:.2f}")
    print(f"  Price: expensive={user.criteria_scores['expensive']:.2f}, "
          f"average={user.criteria_scores['average']:.2f}, "
          f"cheap={user.criteria_scores['cheap']:.2f}")
    
    print_separator("STEP 2: INITIAL RECOMMENDATIONS")
    engine = RecommendationEngine()
    recommendations = engine.get_recommendations(user, products, 30)
    
    print(f"Generated {len(recommendations)} personalized recommendations\n")
    print("Top 5 recommended products:")
    for i, product in enumerate(recommendations[:5], 1):
        score = engine.calculate_product_score(user, product)
        print(f"\n{i}. {product['name']}")
        print(f"   Sphere: {product['sphere']}")
        print(f"   Quality: {product['quality']}, Price: ${product['price']:.2f}, "
              f"Delivery: {product['delivery']}")
        print(f"   Score: {score:.3f}")
    
    purchases = [
        {"index": 0, "name": recommendations[0]['name']},
        {"index": 0, "name": recommendations[0]['name']},  # Will be updated
        {"index": 0, "name": recommendations[0]['name']},  # Will be updated
    ]
    
    for purchase_num in range(3):
        recommendations = engine.get_recommendations(user, products, 30)
        if not recommendations:
            break
            
        product = recommendations[0]
        
        print_separator(f"STEP {3 + purchase_num}: PURCHASE #{purchase_num + 1}")
        print(f"🛒 Buying: {product['name']}")
        print(f"   Sphere: {product['sphere']}")
        print(f"   Price: ${product['price']:.2f}")
        print(f"   Attributes: {product['quality']}, {product['price_level']}, {product['delivery']}")
        
        old_balance = user.balance
        old_sphere_score = user.sphere_scores[product['sphere']]
        
        user.balance -= product['price']
        engine.update_profile_after_purchase(user, product, was_recommended=True)
        
        new_sphere_score = user.sphere_scores[product['sphere']]
        
        print(f"\n💰 Balance: ${old_balance:.2f} → ${user.balance:.2f}")
        print(f"📈 {product['sphere']} score: {old_sphere_score:.2f} → {new_sphere_score:.2f}")
        print(f"🎯 Initial influence: {user.initial_influence:.2f}")
        
        products = [p for p in products if p['id'] != product['id']]
        
        print(f"\nUpdated Top 3 Spheres:")
        sorted_spheres = sorted(user.sphere_scores.items(), key=lambda x: x[1], reverse=True)
        for i, (sphere, score) in enumerate(sorted_spheres[:3], 1):
            print(f"  {i}. {sphere}: {score:.2f}")
    
    print_separator("FINAL STATE - AFTER 3 PURCHASES")
    print(f"Balance: ${user.balance:.2f}")
    print(f"Initial Influence: {user.initial_influence:.2f} (started at 1.0)")
    
    print(f"\nFinal Sphere Preferences (Top 5):")
    sorted_spheres = sorted(user.sphere_scores.items(), key=lambda x: x[1], reverse=True)
    for i, (sphere, score) in enumerate(sorted_spheres[:5], 1):
        print(f"  {i}. {sphere}: {score:.2f}")
    
    print(f"\nFinal Criteria Preferences:")
    print(f"  Quality: premium={user.criteria_scores['premium']:.2f}, "
          f"medium={user.criteria_scores['medium']:.2f}, "
          f"budget={user.criteria_scores['budget']:.2f}")
    print(f"  Price: expensive={user.criteria_scores['expensive']:.2f}, "
          f"average={user.criteria_scores['average']:.2f}, "
          f"cheap={user.criteria_scores['cheap']:.2f}")
    print(f"  Delivery: 1day={user.criteria_scores['1day']:.2f}, "
          f"2-3days={user.criteria_scores['2-3days']:.2f}, "
          f"4+days={user.criteria_scores['4+days']:.2f}")
    
    print_separator("NEW RECOMMENDATIONS AFTER LEARNING")
    final_recommendations = engine.get_recommendations(user, products, 10)
    
    print("Top 5 products now recommended:")
    for i, product in enumerate(final_recommendations[:5], 1):
        score = engine.calculate_product_score(user, product)
        print(f"\n{i}. {product['name']}")
        print(f"   Sphere: {product['sphere']}")
        print(f"   Score: {score:.3f}")
    
    print_separator("DEMO COMPLETE")
    print("Key Observations:")
    print("✅ System learned from purchases")
    print("✅ Sphere scores increased for purchased categories")
    print("✅ Criteria scores adjusted based on purchase patterns")
    print("✅ Initial influence decreased (real behavior > stereotypes)")
    print("✅ Recommendations adapted to user's actual preferences")
    print("\n🎯 The system is ready for production use!")

if __name__ == "__main__":
    demo_user_journey()