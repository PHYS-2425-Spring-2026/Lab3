# Lab 3: Physics-Informed Neural Networks
## PHYS 2425 - Computational Physics

**Due:** Feb 19, 2026

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new)

---

## Quick Start with GitHub Codespaces

### Getting Started (2 minutes)

1. **Accept the Assignment**
   - Click the invitation link from your instructor
   - Your personal repository will be created

2. **Launch Codespace**
   - Click the green **"Code"** button
   - Select **"Codespaces"** tab
   - Click **"Create codespace on main"**
   - Wait 1-2 minutes for setup

3. **Verify Setup**
   - Terminal opens automatically
   - You should see "Setup complete!" message
   - Or manually run: `python test_setup.py`

4. **Start Working**
   - Open `lab3_starter.ipynb`
   - Select Python kernel when prompted
   - Begin Part 1!

---

##  What You'll Learn

In this lab, you will:
-  Implement Physics-Informed Neural Networks (PINNs) from scratch
-  Use automatic differentiation to solve PDEs without finite differences
-  Train neural networks to satisfy physics equations
-  Compare PINNs to traditional numerical methods
- Gain hands-on experience for Project 1

**Problem:** We'll solve the 1D heat equation using a neural network!

$$\frac{\partial u}{\partial t} = 0.1 \frac{\partial^2 u}{\partial x^2}$$

---

##  Lab Structure

| Part | Topic | Time |
|------|-------|------|
| 1 | Understanding the Heat Equation | 20 min |
| 2 | Building a PINN from Scratch | 40 min |
| 3 | Evaluation and Comparison | 30 min |
| 4 | Experimentation | 20 min |

**Total:** ~2 hours in lab + 1 hour outside

---

##  Using Codespaces

### Running the Notebook

**Open the notebook:**
1. Click `lab3_starter.ipynb` in file explorer
2. Select kernel: **"Python 3.10.x"** (top-right)
3. Run cells with `Shift+Enter` or click 

**Run all cells:**
- Click "Run All" in toolbar
- Or: Ctrl+Shift+P → "Run All Cells"

### Saving Your Work

**Auto-save is enabled**, but also commit regularly:

```bash
# Every 30 minutes or after completing a part:
git add lab3_starter.ipynb *.png
git commit -m "Completed Part 2"
git push
```

Or use the **Source Control** panel (Ctrl+Shift+G).

### Viewing Plots

Plots appear **inline** in the notebook automatically. To save:
- Code includes `plt.savefig('filename.png')`
- Figures saved in your workspace
- Right-click file → "Download" to save locally

### Opening Terminal

Press **Ctrl+`** (backtick) or Terminal → New Terminal

```bash
# Install additional packages if needed
pip install package-name

# Run Python scripts
python test_setup.py

# Check files
ls -la
```

### Stopping Your Codespace

 **Important:** Codespaces count against your free hours!

- **Pause:** Close browser tab (auto-pauses after 30 min)
- **Stop:** Click your name (top-right) → "Stop codespace"  
- **Delete:** After submitting, delete to free resources

**You get 60 free hours/month** (more than enough for all labs!)

---

---

## Learning Goals

### Part 1: Heat Equation Fundamentals
- Understand physical meaning of terms
- Visualize analytical solution
- Predict behavior from equations

### Part 2: PINN Implementation
- Build neural network in PyTorch
- Use `torch.autograd` for derivatives
- Design physics-informed loss
- Train network to satisfy PDE

### Part 3: Analysis
- Compare PINN vs analytical solution
- Calculate error metrics
- Visualize results with heatmaps

### Part 4: Experiments
- Test different architectures
- Explore hyperparameters
- Understand trade-offs

### Part 5: Reflection
- Connect to Project 1
- Plan PDE choice
- Identify challenges

---

## Submission

### What to Submit (via Canvas)

1. **Completed notebook** 
   - Rename: `lab3_[YourLastNames].ipynb`
   - All cells executed
   - All exercises answered


3. **Report** 
   - Submit on Canvas

### How to Download Files

**Method 1: Right-click files**
- Right-click in file explorer
- Select "Download"

**Method 2: Bulk download**
```bash
# Create a zip file
zip lab4_submission.zip lab3_starter.ipynb *.png reflection.md

# Download the zip (right-click → Download)
```

### Verification Before Submitting

 **Run this checklist:**

```bash
# 1. Restart kernel and run all
# In notebook: Kernel → Restart & Run All

# 2. Check all files exist
ls lab3_starter.ipynb *.png reflection.md

# 3. Verify figures look correct
# Open each PNG in preview

# 4. Make sure git is up to date
git status
git push
```

---

## Troubleshooting

### "Kernel not found" error
1. Click **"Select Kernel"** (top-right)
2. Choose **"Python 3.10.x"**
3. Wait 10 seconds for kernel to start

### "Module not found" error
```bash
# In terminal:
pip install torch numpy matplotlib scipy
```

### Codespace won't start
1. **Wait 2-3 minutes** (initial setup takes time)
2. Check status in bottom-left corner
3. If stuck >5 min, try:
   - Refresh page
   - Create new codespace
   - Contact instructor

### Plots not showing
- Make sure cell has `plt.show()` at end
- Try restarting kernel
- Check that `%matplotlib inline` is set (should be automatic)

### Training very slow
- Expected: ~30-60 seconds on Codespaces
- If much slower:
  - Reduce epochs (try 2000 instead of 5000)
  - Reduce collocation points
  - Check no other heavy processes running

### Ran out of Codespace hours
**Options:**
1. Work locally (install Python, Jupyter, PyTorch)
2. Request more hours from GitHub Education
3. Use school lab computers
4. Ask instructor for extension

### Git push fails
```bash
# Configure git (first time only)
git config --global user.email "your.email@example.com"
git config --global user.name "Your Name"

# Then push
git push
```

---

## Resources

### PyTorch
- [PyTorch Documentation](https://pytorch.org/docs/)
- [Autograd Tutorial](https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html)
- [Neural Networks Tutorial](https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html)

### PINNs
- [Original Paper](https://www.sciencedirect.com/science/article/pii/S0021999118307125) (Raissi et al., 2019)
- [DeepXDE Library](https://deepxde.readthedocs.io/)
- [Maziar Raissi's Website](https://maziarraissi.github.io/)

### Git & GitHub
- [GitHub Docs](https://docs.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [GitHub Codespaces Docs](https://docs.github.com/en/codespaces)

### Getting Help
- **Office Hours:** Tuesdays 2-4pm, Thursdays 10-12pm
- **Canvas Discussion Board:** Post questions
- **Email Instructor:** [instructor email]
- **GitHub Issues:** For technical problems with this template

---

## 🎓 Tips for Success

### Time Management
- **Part 1-2:** Can be done in lab session
- **Part 3-4:** Finish during lab or at home
- **Part 5:** Reflection after completing main work

### Debugging Strategy
1. **Read error messages carefully**
2. **Check tensor shapes** (print `x.shape`)
3. **Verify gradients enabled** (`requires_grad=True`)
4. **Start simple, add complexity gradually**
5. **Ask for help if stuck >15 minutes**

### Common Mistakes to Avoid
- Forgetting `create_graph=True` for second derivatives
- Not committing work (lose everything if Codespace times out)
- Not testing that notebook runs from scratch
- Submitting without restarting kernel

### Best Practices
- Commit every 20-30 minutes
- Add comments to explain your code
- Test code on small examples first
- Compare results to analytical solution frequently


---



---

##  You're Ready!

Everything you need is in this repository:
- Pre-configured environment
-  Starter notebook with all instructions
-  Test script to verify setup
- This comprehensive README

**Next step:** Open `lab3_starter.ipynb` and begin Part 1!

**Questions?** Check Canvas or come to office hours.

**Good luck and have fun with PINNs!**

---

*Last updated: February 2026*
