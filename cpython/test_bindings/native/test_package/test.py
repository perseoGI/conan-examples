"""
Test script for the spam CPython extension module.
This script tests the native CPython bindings for the spam C++ library.
"""

def test_spam_module():
    try:
        import spam
        print("✓ Successfully imported spam module")
        
        # Test add function
        result = spam.add(5, 3)
        print(f"✓ spam.add(5, 3) = {result}")
        assert result == 8, f"Expected 8, got {result}"
        
        # Test multiply function
        result = spam.multiply(4, 7)
        print(f"✓ spam.multiply(4, 7) = {result}")
        assert result == 28, f"Expected 28, got {result}"
        
        # Test get_version function
        version = spam.get_version()
        print(f"✓ spam.get_version() = '{version}'")
        assert isinstance(version, str), f"Expected string, got {type(version)}"
        
        # Test print_message function
        print("✓ Testing spam.print_message():")
        spam.print_message("Hello from Python!")
        
        print("\n✅ All tests passed! The spam module is working correctly.")
        return True
        
    except ImportError as e:
        print(f"❌ Failed to import spam module: {e}")
        print("Make sure the module is built and available in the Python path.")
        return False
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        return False

if __name__ == "__main__":
    print("Testing CPython bindings for spam C++ library")
    print("=" * 50)
    
    success = test_spam_module()
    
    if success:
        print("\n🎉 All tests completed successfully!")
        exit(0)
    else:
        print("\n💥 Tests failed!")
        exit(1)
