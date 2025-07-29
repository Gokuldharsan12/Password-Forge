#!/usr/bin/env python3
"""
Password Forge - Command Line Interface
A simple CLI version of the password generator
"""

import argparse
import string
import random
import sys

def generate_password(length=12, uppercase=True, digits=True, symbols=True):
    """
    Generate a password with specified criteria
    
    Args:
        length (int): Password length (4-64)
        uppercase (bool): Include uppercase letters
        digits (bool): Include digits
        symbols (bool): Include symbols
    
    Returns:
        str: Generated password
    """
    if length < 4 or length > 64:
        raise ValueError("Password length must be between 4 and 64 characters")
    
    characters = string.ascii_lowercase
    
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character type must be selected")
    
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(
        description="🔐 Password Forge - Generate secure passwords from command line",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py                    # Generate default password (12 chars, all types)
  python cli.py -l 16             # Generate 16-character password
  python cli.py -l 8 --no-symbols # Generate 8-char password without symbols
  python cli.py -l 20 --only-lowercase # Generate 20-char lowercase-only password
        """
    )
    
    parser.add_argument(
        '-l', '--length',
        type=int,
        default=12,
        help='Password length (4-64, default: 12)'
    )
    
    parser.add_argument(
        '--no-uppercase',
        action='store_true',
        help='Exclude uppercase letters'
    )
    
    parser.add_argument(
        '--no-digits',
        action='store_true',
        help='Exclude digits'
    )
    
    parser.add_argument(
        '--no-symbols',
        action='store_true',
        help='Exclude symbols'
    )
    
    parser.add_argument(
        '--only-lowercase',
        action='store_true',
        help='Generate lowercase-only password'
    )
    
    parser.add_argument(
        '-c', '--count',
        type=int,
        default=1,
        help='Number of passwords to generate (default: 1)'
    )
    
    parser.add_argument(
        '--show-settings',
        action='store_true',
        help='Show password generation settings'
    )
    
    args = parser.parse_args()
    
    # Handle --only-lowercase flag
    if args.only_lowercase:
        args.no_uppercase = True
        args.no_digits = True
        args.no_symbols = True
    
    # Determine character types
    uppercase = not args.no_uppercase
    digits = not args.no_digits
    symbols = not args.no_symbols
    
    try:
        # Show settings if requested
        if args.show_settings:
            print("🔐 Password Forge - Settings")
            print("=" * 40)
            print(f"Length: {args.length} characters")
            print(f"Uppercase letters: {'✓' if uppercase else '✗'}")
            print(f"Digits: {'✓' if digits else '✗'}")
            print(f"Symbols: {'✓' if symbols else '✗'}")
            print("=" * 40)
            print()
        
        # Generate passwords
        for i in range(args.count):
            password = generate_password(
                length=args.length,
                uppercase=uppercase,
                digits=digits,
                symbols=symbols
            )
            
            if args.count > 1:
                print(f"{i+1:2d}. {password}")
            else:
                print(password)
        
        # Show password strength info
        if args.count == 1:
            char_count = len(set(string.ascii_lowercase))
            if uppercase:
                char_count += len(set(string.ascii_uppercase))
            if digits:
                char_count += len(set(string.digits))
            if symbols:
                char_count += len(set(string.punctuation))
            
            possible_combinations = char_count ** args.length
            print(f"\n💡 Password strength: {possible_combinations:,} possible combinations")
            
    except ValueError as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main() 