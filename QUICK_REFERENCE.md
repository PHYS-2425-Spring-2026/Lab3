# Lab 3 Quick Reference Card
## Codespaces Cheat Sheet

---

##  Getting Started (First Time)

```
1. Click assignment link → Accept assignment
2. Go to your repo → Code → Codespaces → Create
3. Wait 1-2 minutes for setup
4. Terminal opens → See "Setup complete!"
5. Open lab3_starter.ipynb
6. Select Python 3.10 kernel
7. Start working!
```

---

## Keyboard Shortcuts

### Notebook
- `Shift+Enter` - Run cell and move to next
- `Ctrl+Enter` - Run cell and stay
- `Esc` then `A` - Insert cell above
- `Esc` then `B` - Insert cell below
- `Esc` then `DD` - Delete cell
- `Esc` then `M` - Convert to markdown
- `Esc` then `Y` - Convert to code

### VS Code
- `Ctrl+`` - Toggle terminal
- `Ctrl+Shift+P` - Command palette
- `Ctrl+Shift+G` - Source control (Git)
- `Ctrl+S` - Save (but auto-save is on)
- `Ctrl+F` - Find
- `Ctrl+/` - Comment/uncomment line

---

##  Important Commands

### Terminal Commands
```bash
# Test environment
python test_setup.py

# Install missing package
pip install package-name

# List files
ls -la

# Create directory
mkdir my_experiments

# Remove file
rm filename.png

# Check git status
git status

# Push changes
git add .
git commit -m "Progress update"
git push
```

### Notebook Commands
```python
# In a code cell:

# See variable value
print(variable)

# Check tensor shape
print(x.shape)

# Check if requires grad
print(x.requires_grad)

# See all variables
%whos

# Time a cell
%%time

# Load matplotlib
%matplotlib inline
```

---

## Git Workflow

### Every 30 Minutes
```bash
git add lab4_starter.ipynb
git add *.png
git commit -m "Completed Part X"
git push
```

### Before Submitting
```bash
git add .
git commit -m "Final submission"
git push
```

### First Time Setup (if asked)
```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

---

##  Quick Fixes

### Kernel Not Found
```
1. Click "Select Kernel" (top-right)
2. Choose "Python 3.10.x"
3. Wait 10 seconds
```

### Module Not Found
```bash
pip install torch numpy matplotlib
```

### Cell Won't Run
```
1. Kernel → Restart Kernel
2. Run cells again from top
```

### Plot Not Showing
```python
# Add at end of cell:
plt.show()
```

### Git Push Fails
```bash
git config --global user.email "your.email"
git config --global user.name "Your Name"
git push
```

---

##  PyTorch Essentials

### Create Tensor with Gradients
```python
x = torch.tensor([2.0], requires_grad=True)
```

### First Derivative
```python
u_x = torch.autograd.grad(
    u, x,
    grad_outputs=torch.ones_like(u),
    create_graph=True,  # IMPORTANT!
    retain_graph=True
)[0]
```

### Second Derivative
```python
u_xx = torch.autograd.grad(
    u_x, x,
    grad_outputs=torch.ones_like(u_x),
    create_graph=True,
    retain_graph=True
)[0]
```

### Neural Network Template
```python
model = nn.Sequential(
    nn.Linear(input_size, hidden_size),
    nn.Tanh(),
    nn.Linear(hidden_size, hidden_size),
    nn.Tanh(),
    nn.Linear(hidden_size, output_size)
)
```

### Training Loop
```python
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

for epoch in range(epochs):
    optimizer.zero_grad()
    loss = compute_loss(...)
    loss.backward()
    optimizer.step()
```

---

##  Plotting Essentials

### Basic Plot
```python
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Data')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Title')
plt.legend()
plt.grid(True)
plt.savefig('plot.png')
plt.show()
```

### Heatmap
```python
plt.contourf(X, T, u_pred, levels=50, cmap='hot')
plt.colorbar()
plt.xlabel('Position')
plt.ylabel('Time')
plt.title('Solution')
plt.savefig('heatmap.png')
plt.show()
```

### Multiple Subplots
```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].plot(x, y1)
axes[1].plot(x, y2)
axes[2].plot(x, y3)
plt.tight_layout()
plt.savefig('comparison.png')
plt.show()
```

---



##  Pre-Submission Checklist

```bash
# 1. Restart & Run All
# Kernel → Restart & Run All

# 2. Check all figures created
ls *.png
# Should see 5 PNG files

# 3. Verify all exercises answered
# Scroll through notebook

# 4. Write reflection
# Create reflection.md

# 5. Commit everything
git add .
git commit -m "Final submission"
git push

# 6. Download files
# Right-click files → Download

# 7. Upload to Canvas
```

---
