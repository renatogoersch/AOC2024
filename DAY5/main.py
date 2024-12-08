import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from login import get_input

def is_valid_order(pages, rules):
    relevant_rules = {(x, y) for (x, y) in rules if x in pages and y in pages}
    for before, after in relevant_rules:
        if pages.index(before) > pages.index(after):
            return False
    return True

def correct_update_order(pages, rules):
    relevant_rules = {(x, y) for (x, y) in rules if x in pages and y in pages}
    graph = {page: {'before': set(), 'after': set()} for page in pages}
    
    for before, after in relevant_rules:
        graph[before]['after'].add(after)
        graph[after]['before'].add(before)
    
    corrected = []
    remaining = set(pages)
    
    while remaining:
        for page in list(remaining):
            if not (graph[page]['before'] & remaining):
                corrected.append(page)
                remaining.remove(page)
                break
    
    return corrected

def solve_print_queue_part1(input_text):
    lines = input_text.splitlines()
    rules = set()
    i = 0
    while i < len(lines) and lines[i].strip():
        before, after = map(int, lines[i].split("|"))
        rules.add((before, after))
        i += 1
    
    updates = [list(map(int, line.split(","))) for line in lines[i+1:] if line.strip()]
    
    result = 0
    for update in updates:
        if is_valid_order(update, rules):
            result += update[len(update)//2]
    
    return result

def solve_print_queue_part2(input_text):
    lines = input_text.splitlines()
    rules = set()
    i = 0
    while i < len(lines) and lines[i].strip():
        before, after = map(int, lines[i].split("|"))
        rules.add((before, after))
        i += 1
    
    updates = [list(map(int, line.split(","))) for line in lines[i+1:] if line.strip()]
    
    result = 0
    for update in updates:
        if not is_valid_order(update, rules):
            corrected_update = correct_update_order(update, rules)
            result += corrected_update[len(corrected_update)//2]
    
    return result

input_text = get_input(5)
print("Part 1:", solve_print_queue_part1(input_text))
print("Part 2:", solve_print_queue_part2(input_text))