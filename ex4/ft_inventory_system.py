# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_inventory_system.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: stmaire <stmaire@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/17 14:47:21 by stmaire           #+#    #+#              #
#    Updated: 2026/02/17 18:00:56 by stmaire          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def ft_parsing_args() -> dict[str, int] | None:
    """Check the arguments received in command line and return a dictionnary"""
    if len(sys.argv) < 2:
        print("No argument provided. "
              "Usage: python3 ft_inventory_system.py <category1>:<quantity1> <category2>:<quantity2> ...")
        return
    
    inventory: dict[str, int] = {}
    args = sys.argv[1:]
    for arg in args:
        parts = arg.split(":")
        if len(parts) == 2:
            key = parts[0]
            try: 
                value = int(parts[1])
                if key in inventory:
                    inventory[key] += value
                else:
                    inventory[key] = value
            except ValueError as e:
                print(e)
                return None
        else:
            print("Invalid format")
            print("Usage: python3 ft_inventory_system.py <category1>:<quantity1> <category2>:<quantity2> ...")
            return None
    print(f"{inventory}")
    return inventory


def ft_sort_by_abundance(inventory: dict[str, int]) -> None:
    """Sort by value (bubble sort) and display in function of resources quantities"""
    
    print("\n=== Current Inventory ===")
    items = list(inventory.items()) #method will return each item in a dictionary, as tuples in a list.
    
    size = len(items)
    for i in range(size):
        for j in range(0, size - i - 1):
            if items[j][1] < items[j+1][1]:
                items[j], items[j+1] = items[j+1], items[j]

    total = 0
    for value in inventory.values():
        total += value

    for name, qty in items:
        if total > 0:
            percentage = (qty / total) * 100
        else:
            percentage = 0.0
        
        if qty == 1:
            unit_label = "unit"
        else:
            unit_label = "units"
        print(f"{name}: {qty} {unit_label} ({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")   
    max_value = items[0][1]
    min_value = items[size - 1][1]
    print(f"Most abundant: {items[0][0]} ({items[0][1]} {unit_label})")
    print(f"Least abundant: {items[size -1][0]} ({items[size -1][1]} {unit_label})")


def ft_get_items_categories(inventory: dict[str, int]) -> None:
    """Create nested dictionaries in order to handle and display abundancy"""
    categories = {
        "Abundant" : {},        
        "Moderate" : {},
        "Scarce" : {}        
    }
    
    for name, qty in inventory.items():
        if qty < 5:
            category = "Scarce"
        elif qty < 10:
            category = "Moderate"
        else:
            category = "Abundant"
        categories[category][name] = qty
    
    print("\n=== Item Categories ===")    
    for category, items_dict in categories.items():
        if len(items_dict) > 0:
            print(f"{category}: {items_dict}")

# TODO
#  === Management Suggestions ===
# Restock needed: ['sword', 'helmet']
# === Dictionary Properties Demo ===
# Dictionary keys: sword, potion, shield, armor, helmet
# Dictionary values: 1, 5, 2, 3, 1
# Sample lookup - 'sword' in inventory: True 

def ft_inventory_system(inventory: dict[str, int]):
    """Display an analysis and some statistics about inventory system"""
    print("=== Inventory System Analysis ===")
    total = 0
    for value in inventory.values():
        total += value
    print(f"Total items in inventory: {total}")     
    print(f"Unique item types: {len(inventory)}")
    
    ft_sort_by_abundance(inventory)
    
               
if __name__ == "__main__":
    inventory = ft_parsing_args()
    ft_inventory_system(inventory)
    ft_get_items_categories(inventory)