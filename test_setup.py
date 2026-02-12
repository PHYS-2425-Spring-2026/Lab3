#!/usr/bin/env python3
"""
Test script to verify Lab 3 environment setup
Run this after creating your Codespace to ensure everything works!
"""

import sys

def test_imports():
    """Test that all required packages can be imported"""
    print("Testing package imports...")
    
    packages = {
        'torch': 'PyTorch',
        'numpy': 'NumPy',
        'matplotlib': 'Matplotlib',
        'scipy': 'SciPy',
        'jupyter': 'Jupyter'
    }
    
    failed = []
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"  ✓ {name} imported successfully")
        except ImportError:
            print(f"  ✗ {name} FAILED to import")
            failed.append(name)
    
    return len(failed) == 0

def test_torch():
    """Test PyTorch functionality"""
    print("\nTesting PyTorch...")
    
    try:
        import torch
        
        # Test tensor creation
        x = torch.tensor([1.0, 2.0, 3.0])
        print(f"  ✓ Created tensor: {x}")
        
        # Test autograd
        x = torch.tensor([2.0], requires_grad=True)
        y = x**2
        y.backward()
        print(f"  ✓ Autograd works: d(x²)/dx at x=2 is {x.grad.item()}")
        
        # Test neural network
        model = torch.nn.Sequential(
            torch.nn.Linear(2, 10),
            torch.nn.Tanh(),
            torch.nn.Linear(10, 1)
        )
        test_input = torch.randn(5, 2)
        output = model(test_input)
        print(f"  ✓ Neural network forward pass works: output shape {output.shape}")
        
        return True
    except Exception as e:
        print(f"  ✗ PyTorch test failed: {e}")
        return False

def test_plotting():
    """Test matplotlib"""
    print("\nTesting Matplotlib...")
    
    try:
        import matplotlib
        matplotlib.use('Agg')  # Non-interactive backend
        import matplotlib.pyplot as plt
        import numpy as np
        
        x = np.linspace(0, 2*np.pi, 100)
        y = np.sin(x)
        
        plt.figure()
        plt.plot(x, y)
        plt.savefig('test_plot.png')
        plt.close()
        
        print(f"  ✓ Created test plot (test_plot.png)")
        return True
    except Exception as e:
        print(f"  ✗ Matplotlib test failed: {e}")
        return False

def main():
    print("="*60)
    print("PHYS 2425 Lab 4 - Environment Setup Test")
    print("="*60)
    
    # Test Python version
    print(f"\nPython version: {sys.version}")
    
    # Run tests
    all_pass = True
    all_pass &= test_imports()
    all_pass &= test_torch()
    all_pass &= test_plotting()
    
    # Summary
    print("\n" + "="*60)
    if all_pass:
        print("✓ ALL TESTS PASSED!")
        print("Your environment is ready for Lab 4.")
        print("\nNext steps:")
        print("  1. Open lab4_starter.ipynb")
        print("  2. Select Python kernel")
        print("  3. Start working!")
    else:
        print("✗ SOME TESTS FAILED")
        print("Please contact your instructor or TA.")
    print("="*60)
    
    return 0 if all_pass else 1

if __name__ == "__main__":
    sys.exit(main())
