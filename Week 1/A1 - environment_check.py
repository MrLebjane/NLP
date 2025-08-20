#environment check
import sys
import platform

print(f'Python version: {sys.version}')
print(f'Platform: {platform.platform()}')
print(f'python executable: {sys.executable}')

test_text = 'python is working for NLP!'
print(f'\nTest string: {test_text}')
print(f"Lenght: {len(test_text)}")
print(f'Words: {test_text.split()}')
print("\n Environment setup successful!")