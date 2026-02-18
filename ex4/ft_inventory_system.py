# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 10:48:13 by stmaire         #+#    #+#               #
#  Updated: 2026/02/18 10:51:20 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def ft_parsing_args() -> dict[str, int] | None:
    """Check the arguments received in command line and return a dictionnary"""

    if len(sys.argv) < 2:
        print("No argument provided. "
              "Usage: python3 ft_inventory_system.py "
              "<category1>:<quantity1> <category2>:<quantity2> ...")
        return None

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
            print("Usage: python3 ft_inventory_system.py "
                  "<category1>:<quantity1> <category2>:<quantity2> ...")
            return None
    return inventory


def ft_inventory_system(inventory: dict[str, int]) -> None:
    """Display an analysis and some statistics about inventory system"""
    print("=== Inventory System Analysis ===")
    total = 0
    for value in inventory.values():
        total += value
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}")


def ft_sort_by_abundance(inventory: dict[str, int]) -> None:
    """Sort and display inventory based on resource quantities

    Uses a bubble sort algorithm.
    Sort the inventory by quantity (descending) and then by name (ascending)
    for items with the same quantity
    """

    print("\n=== Current Inventory ===")
    items = list(inventory.items())

    size = len(items)
    for i in range(size):
        for j in range(0, size - i - 1):
            if items[j][1] < items[j+1][1]:
                items[j], items[j+1] = items[j+1], items[j]
            elif items[j][1] == items[j+1][1]:
                if items[j][0] > items[j+1][0]:
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
    if max_value > 1:
        max_unit_label = "units"
    else:
        max_unit_label = "unit"
    min_value = items[size - 1][1]
    if min_value > 1:
        min_unit_label = "units"
    else:
        min_unit_label = "unit"

    print(f"Most abundant: {items[0][0]} ({max_value} {max_unit_label})")
    print(f"Least abundant: {items[size -1][0]} "
          f"({min_value} {min_unit_label})")


def ft_get_items_categories(inventory: dict[str, int]) -> None:
    """Create nested dictionaries

    handle and display abundancy
    """

    categories: dict[str, dict[str, int]] = {
        "Abundant": {},
        "Moderate": {},
        "Scarce": {}
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

    print("\n=== Management Suggestions ===")
    restock_needed = []
    for name, qty in categories["Scarce"].items():
        if qty < 2:
            restock_needed += [name]
    print(f"Restock needed: {restock_needed} ")


def ft_properties_demo(inventory: dict[str, int]) -> None:
    """Displays dictionary properties"""

    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary keys: ", end="")
    size = len(inventory)
    count = 0
    for key in inventory.keys():
        count += 1
        if count == size:
            print(f"{key}")
        else:
            print(f"{key}, ", end="")

    print("Dictionary values: ", end="")
    count = 0
    for value in inventory.values():
        count += 1
        if count == size:
            print(f"{value}")
        else:
            print(f"{value}, ", end="")

    lookup = False
    name = "sword"
    if name in inventory:
        lookup = True
    print(f"Sample lookup - '{name}' in inventory: {lookup}")


if __name__ == "__main__":
    inventory = ft_parsing_args()
    if inventory is not None:
        ft_inventory_system(inventory)
        ft_sort_by_abundance(inventory)
        ft_get_items_categories(inventory)
        ft_properties_demo(inventory)
