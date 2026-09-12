# merge-conflict-lab

Session 3 · LAB 2 · MSA-DATI07-01

Two branches — `main` and `feature/log-returns` — implemented `metrics.py`
in different, incompatible ways. Your job: merge them and resolve the conflicts by hand.

## What to do

```bash
# 1. Fork this repo on GitHub, then clone YOUR fork
git clone https://github.com/<your-username>/merge-conflict-lab.git
cd merge-conflict-lab

# 2. Try the merge — it will fail with conflicts
git switch main
git merge feature/log-returns

# 3. Open metrics.py — you will find 3 conflict blocks. Resolve each one.

# 4. Verify no markers remain
grep -n '<<<<<<<' metrics.py    # should print nothing

# 5. Finish the merge
git add metrics.py
git commit -m "Resolve conflicts, adopt log returns"

# 6. Verify the tests pass
pip install -r requirements.txt
python -m pytest

# 7. Push to your fork
git push origin main
```

## Which version should win?

The branch is called `feature/log-returns` — it moves the module to log returns.
The tests only pass if you adopt the log-return version everywhere. Green tests = correct resolution.
