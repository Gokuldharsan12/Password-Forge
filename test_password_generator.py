#!/usr/bin/env python3
"""
Test script for Password Forge
Tests the password generation functionality
"""

import string
import random
from cli import generate_password

def test_password_generation():
    """Test password generation with various settings"""
    print("🧪 Testing Password Forge Generation")
    print("=" * 50)
    
    test_cases = [
        {
            "name": "Default settings (12 chars, all types)",
            "length": 12,
            "uppercase": True,
            "digits": True,
            "symbols": True
        },
        {
            "name": "Short password (6 chars, all types)",
            "length": 6,
            "uppercase": True,
            "digits": True,
            "symbols": True
        },
        {
            "name": "Long password (20 chars, all types)",
            "length": 20,
            "uppercase": True,
            "digits": True,
            "symbols": True
        },
        {
            "name": "Lowercase only (16 chars)",
            "length": 16,
            "uppercase": False,
            "digits": False,
            "symbols": False
        },
        {
            "name": "Letters only (no symbols, 14 chars)",
            "length": 14,
            "uppercase": True,
            "digits": False,
            "symbols": False
        },
        {
            "name": "Alphanumeric only (no symbols, 18 chars)",
            "length": 18,
            "uppercase": True,
            "digits": True,
            "symbols": False
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{i}. {test_case['name']}")
        print("-" * 40)
        
        try:
            password = generate_password(
                length=test_case['length'],
                uppercase=test_case['uppercase'],
                digits=test_case['digits'],
                symbols=test_case['symbols']
            )
            
            print(f"Generated: {password}")
            print(f"Length: {len(password)} characters")
            
            # Verify character types
            has_upper = any(c.isupper() for c in password)
            has_lower = any(c.islower() for c in password)
            has_digit = any(c.isdigit() for c in password)
            has_symbol = any(c in string.punctuation for c in password)
            
            print(f"Contains uppercase: {'✓' if has_upper else '✗'}")
            print(f"Contains lowercase: {'✓' if has_lower else '✗'}")
            print(f"Contains digits: {'✓' if has_digit else '✗'}")
            print(f"Contains symbols: {'✓' if has_symbol else '✗'}")
            
            # Verify expected character types
            if test_case['uppercase'] and not has_upper:
                print("❌ ERROR: Expected uppercase but not found!")
            if test_case['digits'] and not has_digit:
                print("❌ ERROR: Expected digits but not found!")
            if test_case['symbols'] and not has_symbol:
                print("❌ ERROR: Expected symbols but not found!")
            if not test_case['uppercase'] and has_upper:
                print("❌ ERROR: Unexpected uppercase found!")
            if not test_case['digits'] and has_digit:
                print("❌ ERROR: Unexpected digits found!")
            if not test_case['symbols'] and has_symbol:
                print("❌ ERROR: Unexpected symbols found!")
                
        except Exception as e:
            print(f"❌ ERROR: {e}")
    
    print("\n" + "=" * 50)
    print("✅ Testing completed!")

def test_edge_cases():
    """Test edge cases and error conditions"""
    print("\n🧪 Testing Edge Cases")
    print("=" * 30)
    
    edge_cases = [
        {
            "name": "Minimum length (4 chars)",
            "length": 4,
            "uppercase": True,
            "digits": True,
            "symbols": True
        },
        {
            "name": "Maximum length (64 chars)",
            "length": 64,
            "uppercase": True,
            "digits": True,
            "symbols": True
        },
        {
            "name": "Only lowercase (minimum complexity)",
            "length": 8,
            "uppercase": False,
            "digits": False,
            "symbols": False
        }
    ]
    
    for i, test_case in enumerate(edge_cases, 1):
        print(f"\n{i}. {test_case['name']}")
        print("-" * 30)
        
        try:
            password = generate_password(
                length=test_case['length'],
                uppercase=test_case['uppercase'],
                digits=test_case['digits'],
                symbols=test_case['symbols']
            )
            
            print(f"Generated: {password}")
            print(f"Length: {len(password)} characters")
            print("✅ Success")
            
        except Exception as e:
            print(f"❌ ERROR: {e}")

def test_error_conditions():
    """Test error conditions"""
    print("\n🧪 Testing Error Conditions")
    print("=" * 30)
    
    error_cases = [
        {
            "name": "Length too short (3 chars)",
            "length": 3,
            "uppercase": True,
            "digits": True,
            "symbols": True,
            "should_fail": True
        },
        {
            "name": "Length too long (65 chars)",
            "length": 65,
            "uppercase": True,
            "digits": True,
            "symbols": True,
            "should_fail": True
        },
        {
            "name": "No character types selected",
            "length": 12,
            "uppercase": False,
            "digits": False,
            "symbols": False,
            "should_fail": True
        }
    ]
    
    for i, test_case in enumerate(error_cases, 1):
        print(f"\n{i}. {test_case['name']}")
        print("-" * 30)
        
        try:
            password = generate_password(
                length=test_case['length'],
                uppercase=test_case['uppercase'],
                digits=test_case['digits'],
                symbols=test_case['symbols']
            )
            
            if test_case['should_fail']:
                print("❌ ERROR: Should have failed but didn't!")
            else:
                print(f"Generated: {password}")
                print("✅ Success")
                
        except Exception as e:
            if test_case['should_fail']:
                print(f"✅ Expected error: {e}")
            else:
                print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    test_password_generation()
    test_edge_cases()
    test_error_conditions() 